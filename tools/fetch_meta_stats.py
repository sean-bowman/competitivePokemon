'''
Fetch current Pokemon Champions meta usage statistics from Pikalytics.

Saves a dated snapshot to docs/snapshots/meta_stats_YYYY-MM-DD.json.

Usage:
    python tools/fetch_meta_stats.py                   # fetch Champions stats
    python tools/fetch_meta_stats.py --top 30          # limit to top-N Pokemon
    python tools/fetch_meta_stats.py --detail          # also fetch per-Pokemon detail pages
    python tools/fetch_meta_stats.py --output path.json

Data source: https://www.pikalytics.com/champions
Page is server-rendered; no JavaScript execution required.
The site also exposes llms-full.txt at pikalytics.com/llms-full.txt for structured text access.
'''

import argparse
import json
import sys
import time
from datetime import date
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError as e:
    missing = str(e).split("'")[1]
    pkg = 'beautifulsoup4' if 'bs4' in missing else missing
    print(f'Missing dependency: {missing}. Run: pip install requests beautifulsoup4')
    sys.exit(1)


PIKALYTICS_CHAMPIONS = 'https://www.pikalytics.com/champions'
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


def parseUsageCard(card) -> dict:
    '''Extract structured data from a single .usage-card BeautifulSoup element.'''
    result = {}

    rankEl = card.find(class_='usage-rank')
    result['rank'] = rankEl.get_text(strip=True).lstrip('#') if rankEl else None

    nameEl = card.find('h3')
    result['name'] = nameEl.get_text(strip=True) if nameEl else None

    pctEl = card.find(class_='usage-percent')
    pctText = pctEl.get_text(strip=True) if pctEl else None
    result['usage_pct'] = float(pctText.rstrip('%')) if pctText else None

    labelEl = card.find(class_='usage-label')
    result['role_label'] = labelEl.get_text(strip=True) if labelEl else None

    descEl = card.find('p')
    result['description'] = descEl.get_text(strip=True) if descEl else None

    # Derive profile URL and sprite path from the card's href
    href = card.get('href', '')
    result['profile_url'] = f'https://www.pikalytics.com{href}' if href else None
    result['pokemon_key'] = href.split('/')[-1] if href else None

    return result


def fetchOverview(topN: int | None = None) -> list[dict]:
    '''
    Fetch and parse the Pikalytics Champions overview page.
    Returns a list of usage card dicts, optionally limited to topN.
    '''
    print(f'Fetching {PIKALYTICS_CHAMPIONS} ...')
    html = fetchHtml(PIKALYTICS_CHAMPIONS)
    if not html:
        return []

    soup = BeautifulSoup(html, 'html.parser')
    cards = soup.find_all(class_='usage-card')

    print(f'  Found {len(cards)} usage cards')

    results = []
    for card in cards:
        data = parseUsageCard(card)
        if data.get('name'):
            results.append(data)

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
    which returns English names regardless of viewer locale — more reliable than
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
        'format': 'Pokemon Champions — Double Battles',
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
    print(f'\n=== {snapshot["format"]} — Usage Rankings ({snapshot["fetched"]}) ===')
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
