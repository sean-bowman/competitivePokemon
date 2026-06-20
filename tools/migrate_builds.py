'''
One-shot migration: parse the markdown build documents in docs/teams/builds/
into the structured team JSON schema under docs/teams/data/.

The `## Team Summary` pipe table is authoritative for each slot's role, Pokemon,
item, ability, and four moves. Per-Pokemon EVs and nature come from the fenced
```text``` block under each `### N. <Pokemon> @ <Item>` heading.

Usage:
    python tools/migrate_builds.py            # migrate all builds
    python tools/migrate_builds.py --dry-run  # print parsed JSON without writing
'''

import argparse
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
BUILD_DIR = REPO_ROOT / 'docs' / 'teams' / 'builds'
DATA_DIR = REPO_ROOT / 'docs' / 'teams' / 'data'
DEFAULT_SNAPSHOT = 'meta_stats_2026-04-14.json'

EV_ORDER = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
# Token -> canonical stat key. Order matters: check longer tokens first.
EV_TOKEN_MAP = {
    'hp': 'hp',
    'atk': 'atk', 'attack': 'atk',
    'def': 'def', 'defense': 'def', 'defence': 'def',
    'spatk': 'spa', 'spa': 'spa', 'spatt': 'spa', 'spattack': 'spa', 'specialattack': 'spa',
    'spdef': 'spd', 'spd': 'spd', 'spdefense': 'spd', 'specialdefense': 'spd',
    'spe': 'spe', 'speed': 'spe', 'spd.': 'spd',
}


def slugifyTeam(name: str) -> str:
    '''Lowercase team name with non-alphanumerics collapsed to underscores.'''
    slug = re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')
    return slug or 'team'


def parseMetadata(md: str) -> dict:
    '''Extract title and the **Field:** header lines.'''
    meta: dict = {}
    titleMatch = re.search(r'^#\s*Build:\s*(.+)$', md, re.MULTILINE)
    if titleMatch:
        meta['name'] = titleMatch.group(1).strip()
    fieldMap = {
        'Format': 'format',
        'Created': 'created',
        'Updated': 'updated',
        'Win Condition': 'winCondition',
        'Seed Reference': 'seedReference',
    }
    for label, key in fieldMap.items():
        match = re.search(rf'^\*\*{re.escape(label)}:\*\*\s*(.+)$', md, re.MULTILINE)
        if match:
            value = match.group(1).strip()
            if key == 'seedReference':
                # Pull the path out of a [text](path) markdown link if present
                linkMatch = re.search(r'\]\(([^)]+)\)', value)
                if linkMatch:
                    value = linkMatch.group(1)
            meta[key] = value
    return meta


def parseSummaryTable(md: str) -> list[dict]:
    '''Parse the Team Summary pipe table into ordered slot dicts.'''
    lines = md.splitlines()
    rows: list[dict] = []
    inTable = False
    for line in lines:
        stripped = line.strip()
        # Header row signals the start; the separator row is skipped
        if stripped.startswith('| #') and 'Pokemon' in stripped:
            inTable = True
            continue
        if inTable:
            if not stripped.startswith('|'):
                break
            if set(stripped) <= set('|- :'):
                continue  # separator row
            cells = [c.strip() for c in stripped.strip('|').split('|')]
            if len(cells) < 9 or not cells[0].isdigit():
                continue
            rows.append({
                'slot': int(cells[0]),
                'role': cells[1],
                'pokemon': cells[2],
                'item': cells[3],
                'ability': cells[4],
                'moves': [cells[5], cells[6], cells[7], cells[8]],
                'evs': {k: 0 for k in EV_ORDER},
                'nature': '',
                'notes': '',
            })
    return rows


def parseEvString(evString: str) -> dict:
    '''Parse '252 SpAtk / 252 HP / 4 SpDef' into a canonical EV dict.'''
    evs = {k: 0 for k in EV_ORDER}
    for part in evString.split('/'):
        match = re.match(r'\s*(\d+)\s*([A-Za-z.]+)', part.strip())
        if not match:
            continue
        value = int(match.group(1))
        token = match.group(2).lower().replace('.', '')
        stat = EV_TOKEN_MAP.get(token)
        if stat:
            evs[stat] = value
    return evs


def parseRosterBlocks(md: str) -> dict:
    '''
    Map each '### N. <Pokemon> @ <Item>' section to its parsed EV/nature data.

    Returns {pokemonName: {'evs': {...}, 'nature': str}}.
    '''
    blocks: dict = {}
    # Heading forms: '### 1. Pokemon @ Item' and '### 5 (Near-core). Pokemon @ Item'
    pattern = re.compile(r'^###\s*\d+[^.\n]*\.\s*(.+?)\s*@', re.MULTILINE)
    for match in pattern.finditer(md):
        pokemon = match.group(1).strip()
        start = match.end()
        nextMatch = pattern.search(md, start)
        section = md[start: nextMatch.start()] if nextMatch else md[start:]
        evMatch = re.search(r'EVs:\s*(.+)', section)
        natureMatch = re.search(r'Nature:\s*(.+)', section)
        blocks[pokemon] = {
            'evs': parseEvString(evMatch.group(1)) if evMatch else {k: 0 for k in EV_ORDER},
            'nature': natureMatch.group(1).strip() if natureMatch else '',
        }
    return blocks


def parseBuild(path: Path) -> dict:
    '''Parse a single build markdown file into a team dict.'''
    md = path.read_text(encoding='utf-8')
    meta = parseMetadata(md)
    slots = parseSummaryTable(md)
    blocks = parseRosterBlocks(md)

    for slot in slots:
        block = blocks.get(slot['pokemon'])
        if block:
            slot['evs'] = block['evs']
            slot['nature'] = block['nature']

    name = meta.get('name', path.stem)
    team = {
        'schemaVersion': 1,
        'name': name,
        'slug': slugifyTeam(name),
        'format': meta.get('format', 'Pokemon Champions: Double Battles (VGC)'),
        'winCondition': meta.get('winCondition', ''),
        'created': meta.get('created', ''),
        'updated': meta.get('updated', ''),
        'metaSnapshot': DEFAULT_SNAPSHOT,
        'seedReference': meta.get('seedReference', ''),
        'notes': '',
        'slots': slots,
    }
    return team


def main() -> None:
    parser = argparse.ArgumentParser(description='Migrate markdown builds to structured team JSON')
    parser.add_argument('--dry-run', action='store_true', help='Print parsed JSON without writing')
    args = parser.parse_args()

    builds = sorted(BUILD_DIR.glob('*.md'))
    if not builds:
        print(f'No build files found in {BUILD_DIR}')
        return

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for path in builds:
        team = parseBuild(path)
        outputPath = DATA_DIR / f'{team["slug"]}.json'
        filled = sum(1 for s in team['slots'] if s.get('pokemon'))
        if args.dry_run:
            print(f'\n=== {path.name} -> {outputPath.name} ({filled} slots) ===')
            print(json.dumps(team, indent=2))
        else:
            with open(outputPath, 'w', encoding='utf-8') as f:
                json.dump(team, f, indent=2)
            print(f'{path.name} -> {outputPath} ({filled} slots)')


if __name__ == '__main__':
    main()
