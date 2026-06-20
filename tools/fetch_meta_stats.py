'''
Fetch current Pokemon Champions meta usage statistics from Pikalytics.

Saves a dated snapshot to docs/snapshots/meta_stats_YYYY-MM-DD.json.

Usage:
    python tools/fetch_meta_stats.py                   # fetch Champions stats
    python tools/fetch_meta_stats.py --top 30          # limit to top-N Pokemon
    python tools/fetch_meta_stats.py --detail          # also fetch per-Pokemon detail pages
    python tools/fetch_meta_stats.py --output path.json

Data source: Pikalytics machine-readable AI endpoint
    https://www.pikalytics.com/ai/pokedex/championstournaments  (markdown)
which exposes a stable 'Best 50 Pokemon by Usage' table plus per-Pokemon detail
pages. Preferred over scraping the HTML page, whose CSS classes change without
notice.
'''

import argparse
import json
import re
import sys
import time
from datetime import date
from pathlib import Path

try:
    import requests
except ImportError:
    print('Missing dependency: requests. Run: pip install requests')
    sys.exit(1)


PIKALYTICS_CHAMPIONS = 'https://www.pikalytics.com/champions'
# Machine-readable markdown overview (exposes a 'Best 50 Pokemon by Usage' table).
# Used instead of scraping the HTML page, whose markup is unstable.
PIKALYTICS_CHAMPIONS_AI = 'https://www.pikalytics.com/ai/pokedex/championstournaments'
PIKALYTICS_POKEMON_BASE = 'https://www.pikalytics.com/pokedex/championstournaments'
PIKALYTICS_POKEMON_AI_BASE = 'https://www.pikalytics.com/ai/pokedex/championstournaments'
PIKALYTICS_LLMS = 'https://www.pikalytics.com/llms-full.txt'
OUTPUT_DIR = Path(__file__).parent.parent / 'docs' / 'snapshots'
POKEMON_DIR = Path(__file__).parent.parent / 'docs' / 'pokemon' / 'champions'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; competitive-pokemon-research/1.0)',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9',
}


def fetchHtml(url: str, delay: float = 0.5) -> str | None:
    '''Fetch raw HTML from a URL with a polite delay.'''
    try:
        time.sleep(delay)
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f'  Warning: failed to fetch {url}: {e}')
        return None


def parsePercent(text: str) -> float | None:
    '''Parse a '38.73%' style table cell into a float; None for blanks / 'N/A'.'''
    cleaned = (text or '').strip().rstrip('%')
    try:
        return float(cleaned)
    except ValueError:
        return None


def extractUrl(cell: str) -> str | None:
    '''Pull the first URL out of a markdown link cell like [View](https://...).'''
    match = re.search(r'\((https?://[^)]+)\)', cell or '')
    return match.group(1) if match else None


def parseUsageTable(md: str) -> list[dict]:
    '''
    Parse the 'Best 50 Pokemon by Usage' markdown table from the AI overview
    endpoint into usage dicts matching the snapshot schema.

    The table columns are: Rank | Pokemon | Usage % | Win Rate | Record | links.
    We anchor on the section heading and read pipe-delimited rows until the next
    section, skipping the header and the |---| separator.
    '''
    lines = md.splitlines()
    start = next(
        (i for i, ln in enumerate(lines)
         if ln.strip().lower().startswith('##') and 'by usage' in ln.lower()),
        None,
    )
    if start is None:
        return []

    results: list[dict] = []
    headerSeen = False
    for line in lines[start + 1:]:
        stripped = line.strip()
        if stripped.startswith('## '):
            break  # reached the next section
        if not stripped.startswith('|'):
            continue
        cells = [c.strip() for c in stripped.strip('|').split('|')]
        joined = ' '.join(cells).lower()
        if 'rank' in joined and 'usage' in joined:
            headerSeen = True  # column-header row
            continue
        if not headerSeen or set(''.join(cells)) <= set('-: '):
            continue  # rows before the header, or the |---| separator
        if len(cells) < 3:
            continue
        name = cells[1].replace('**', '').strip()
        if not name:
            continue
        profileUrl = extractUrl(cells[5]) if len(cells) > 5 else None
        key = profileUrl.rstrip('/').split('/')[-1] if profileUrl else slugifyName(name)
        results.append({
            'rank': cells[0],
            'name': name,
            'usage_pct': parsePercent(cells[2]),
            'win_rate': parsePercent(cells[3]) if len(cells) > 3 else None,
            'record': cells[4] if len(cells) > 4 else None,
            'profile_url': profileUrl,
            'pokemon_key': key,
        })
    return results


def fetchOverview(topN: int | None = None) -> list[dict]:
    '''
    Fetch and parse the Pikalytics Champions usage ranking.

    Reads the machine-readable AI overview endpoint (markdown) rather than scraping
    the HTML page, whose markup changes without notice. Returns a list of usage
    dicts, optionally limited to topN.
    '''
    print(f'Fetching {PIKALYTICS_CHAMPIONS_AI} ...')
    md = fetchHtml(PIKALYTICS_CHAMPIONS_AI)
    if not md:
        return []

    results = parseUsageTable(md)
    print(f'  Parsed {len(results)} Pokemon from the usage table')

    if topN:
        results = results[:topN]

    return results


def slugifyName(displayName: str) -> str:
    '''
    Convert a display name to a Pikalytics URL slug.
    e.g. 'Rotom-Wash' -> 'rotom-wash', 'Incineroar' -> 'incineroar'
    '''
    return displayName.lower().replace(' ', '-')


def parseMarkdownSection(md: str, heading: str) -> list[dict]:
    '''
    Extract bullet list entries from a markdown section with the given heading.
    Expected format (from Pikalytics /ai/ endpoint):
        ## Heading
        - **Name**: 99.0%
        - **Name**: 45.2%
    Returns list of {'name': str, 'pct': float}.
    '''
    entries = []
    inSection = False
    for line in md.splitlines():
        stripped = line.strip()
        if stripped.startswith('## ') and heading.lower() in stripped.lower():
            inSection = True
            continue
        if inSection:
            if stripped.startswith('## '):
                break  # reached next section
            if stripped.startswith('- '):
                # format: - **Move Name**: 99.025%  OR  - Move Name: 99.025%
                content = stripped[2:]
                if '**' in content:
                    content = content.replace('**', '')
                if ':' in content:
                    namePart, pctPart = content.split(':', 1)
                    name = namePart.strip()
                    try:
                        pct = float(pctPart.strip().rstrip('%'))
                        entries.append({'name': name, 'pct': pct})
                    except ValueError:
                        pass
    return entries


def fetchPokemonDetail(pokemonKey: str, displayName: str = '') -> dict:
    '''
    Fetch per-Pokemon Champions data from the Pikalytics /ai/pokedex/ endpoint.
    Returns moves, items, abilities, and teammates as lists of {name, pct} dicts.

    Uses the machine-readable markdown endpoint (/ai/pokedex/championstournaments/<name>)
    which returns English names regardless of viewer locale: more reliable than
    HTML scraping the standard detail page.

    Falls back to display name if the pokemonKey URL 404s (e.g. Rotom-Wash vs rotomwash).
    '''
    # Prefer display name for the AI endpoint (it uses proper capitalisation)
    candidates: list[str] = []
    if displayName:
        candidates.append(displayName)
    if pokemonKey and pokemonKey != slugifyName(displayName):
        candidates.append(pokemonKey)

    md = None
    usedUrl = None
    for key in candidates:
        url = f'{PIKALYTICS_POKEMON_AI_BASE}/{key}'
        md = fetchHtml(url, delay=1.0)
        if md:
            usedUrl = url
            break

    if not md:
        return {}

    detail: dict = {'detail_url': usedUrl}
    detail['moves'] = parseMarkdownSection(md, 'Common Moves')
    detail['items'] = parseMarkdownSection(md, 'Common Items')
    detail['abilities'] = parseMarkdownSection(md, 'Common Abilities')
    detail['teammates'] = parseMarkdownSection(md, 'Common Teammates')

    return detail


def savePokemonDetail(name: str, data: dict, fetchedDate: str) -> None:
    '''
    Save a single Pokemon's Champions detail data to docs/pokemon/<slug>_champions.json.
    The file is a self-contained record: name, fetch date, and all detail fields.
    '''
    slug = slugifyName(name)
    outputPath = POKEMON_DIR / f'{slug}_champions.json'
    POKEMON_DIR.mkdir(parents=True, exist_ok=True)
    record = {'name': name, 'fetched': fetchedDate, 'source': 'pikalytics_champions'}
    record.update(data)
    with open(outputPath, 'w', encoding='utf-8') as f:
        json.dump(record, f, indent=2)
    print(f'  Saved detail: {outputPath.name}')


def buildSnapshot(usageList: list[dict], fetchDetail: bool = False) -> dict:
    '''
    Assemble the full snapshot dict from the usage list,
    optionally enriched with per-Pokemon detail data.
    When fetchDetail is True, each Pokemon's detail is also saved to
    docs/pokemon/<slug>_champions.json for offline per-Pokemon reference.
    '''
    today = str(date.today())
    snapshot = {
        'source': PIKALYTICS_CHAMPIONS,
        'fetched': today,
        'format': 'Pokemon Champions: Double Battles',
        'pokemon': [],
    }

    for entry in usageList:
        pokemon = dict(entry)
        if fetchDetail and entry.get('pokemon_key'):
            name = entry.get('name', '')
            print(f'  Fetching detail: {name} ...')
            detail = fetchPokemonDetail(entry['pokemon_key'], displayName=name)
            pokemon.update(detail)
            if detail and name:
                savePokemonDetail(name, detail, today)
        snapshot['pokemon'].append(pokemon)

    return snapshot


def saveSnapshot(snapshot: dict, outputPath: Path) -> None:
    '''Save snapshot JSON to disk.'''
    outputPath.parent.mkdir(parents=True, exist_ok=True)
    with open(outputPath, 'w', encoding='utf-8') as f:
        json.dump(snapshot, f, indent=2)
    print(f'\nSnapshot saved to {outputPath}')


def printSummary(snapshot: dict) -> None:
    '''Print a ranked usage table to stdout.'''
    pokemon = snapshot.get('pokemon', [])
    print(f'\n=== {snapshot["format"]}: Usage Rankings ({snapshot["fetched"]}) ===')
    print(f'  {"Rank":<6} {"Pokemon":<20} {"Usage":>7}  Role')
    print(f'  {"-"*60}')
    for p in pokemon:
        rank = f'#{p.get("rank", "?")}'
        name = p.get('name', 'Unknown')
        pct = f'{p.get("usage_pct", 0):.1f}%' if p.get('usage_pct') is not None else 'N/A'
        role = p.get('role_label', '')
        print(f'  {rank:<6} {name:<20} {pct:>7}  {role}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Fetch Pokemon Champions meta stats from Pikalytics')
    parser.add_argument(
        '--top', '-n',
        type=int,
        default=None,
        help='Limit to top-N Pokemon (default: all)',
    )
    parser.add_argument(
        '--detail', '-d',
        action='store_true',
        help='Also fetch per-Pokemon detail pages (moves, items, teammates). Slower.',
    )
    parser.add_argument(
        '--output', '-o',
        default=None,
        help='Output JSON path (default: docs/snapshots/meta_stats_YYYY-MM-DD.json)',
    )
    args = parser.parse_args()

    outputPath = (
        Path(args.output)
        if args.output
        else OUTPUT_DIR / f'meta_stats_{date.today()}.json'
    )

    usageList = fetchOverview(topN=args.top)
    if not usageList:
        print('No data fetched. Check your internet connection or the Pikalytics URL.')
        sys.exit(1)

    snapshot = buildSnapshot(usageList, fetchDetail=args.detail)
    saveSnapshot(snapshot, outputPath)
    printSummary(snapshot)


if __name__ == '__main__':
    main()
