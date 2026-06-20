'''
Team persistence: load/save structured team JSON and export a markdown build doc.

Teams live in docs/teams/data/<slug>.json. The markdown export reproduces the
existing build-doc layout (summary table + per-Pokemon EV/nature blocks) so the
human-readable artifacts in docs/teams/builds/ stay in sync on save.
'''

import json
import re
from datetime import date

from app import dataAccess

# EV stat keys in canonical display order
EV_ORDER = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
EV_LABELS = {'hp': 'HP', 'atk': 'Atk', 'def': 'Def', 'spa': 'SpAtk', 'spd': 'SpDef', 'spe': 'Spe'}


def emptyEvs() -> dict:
    '''Return a zeroed EV dict.'''
    return {k: 0 for k in EV_ORDER}


def emptySlot(index: int) -> dict:
    '''Return a blank team slot.'''
    return {
        'slot': index,
        'role': '',
        'pokemon': None,
        'item': None,
        'ability': None,
        'moves': ['', '', '', ''],
        'evs': emptyEvs(),
        'nature': '',
        'notes': '',
    }


def emptyTeam(name: str = 'New Team') -> dict:
    '''Return a blank six-slot team.'''
    return {
        'schemaVersion': 1,
        'name': name,
        'slug': slugifyTeam(name),
        'format': 'Pokemon Champions: Double Battles (VGC)',
        'winCondition': '',
        'created': str(date.today()),
        'updated': '',
        'metaSnapshot': '',
        'seedReference': '',
        'notes': '',
        'slots': [emptySlot(i + 1) for i in range(6)],
    }


def slugifyTeam(name: str) -> str:
    '''Lowercase team name with non-alphanumerics collapsed to underscores.'''
    slug = re.sub(r'[^a-z0-9]+', '_', (name or 'team').lower()).strip('_')
    return slug or 'team'


def listTeams() -> list[dict]:
    '''Return metadata for all saved teams: {slug, name, path, format, created}.'''
    if not dataAccess.TEAM_DIR.exists():
        return []
    out = []
    for path in sorted(dataAccess.TEAM_DIR.glob('*.json')):
        try:
            with open(path, encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue
        out.append({
            'slug': data.get('slug', path.stem),
            'name': data.get('name', path.stem),
            'path': str(path),
            'format': data.get('format', ''),
            'created': data.get('created', ''),
        })
    return out


def loadTeam(slug: str) -> dict | None:
    '''Load a team by slug from docs/teams/data/.'''
    path = dataAccess.TEAM_DIR / f'{slug}.json'
    if not path.exists():
        return None
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def saveTeam(team: dict, exportMarkdownDoc: bool = True) -> dict:
    '''
    Write a team to docs/teams/data/<slug>.json (and optionally a markdown build doc).

    Returns {jsonPath, markdownPath}. The slug is derived from the team name.
    '''
    team = dict(team)
    team['slug'] = slugifyTeam(team.get('name', 'team'))
    dataAccess.TEAM_DIR.mkdir(parents=True, exist_ok=True)
    jsonPath = dataAccess.TEAM_DIR / f'{team["slug"]}.json'
    with open(jsonPath, 'w', encoding='utf-8') as f:
        json.dump(team, f, indent=2)

    result = {'jsonPath': str(jsonPath), 'markdownPath': None}
    if exportMarkdownDoc:
        dataAccess.BUILD_DIR.mkdir(parents=True, exist_ok=True)
        mdPath = dataAccess.BUILD_DIR / f'{team["slug"]}.md'
        with open(mdPath, 'w', encoding='utf-8') as f:
            f.write(exportMarkdown(team))
        result['markdownPath'] = str(mdPath)
    return result


def _formatEvs(evs: dict) -> str:
    '''Render an EV dict as '252 SpAtk / 252 HP / 4 SpDef', omitting zeros.'''
    parts = [f'{evs.get(k, 0)} {EV_LABELS[k]}' for k in EV_ORDER if int(evs.get(k, 0) or 0) > 0]
    return ' / '.join(parts) if parts else ': '


def exportMarkdown(team: dict) -> str:
    '''Render a team as a markdown build document matching the existing format.'''
    lines: list[str] = []
    lines.append(f'# Build: {team.get("name", "Untitled")}')
    lines.append('')
    lines.append(f'**Format:** {team.get("format", ": ")}')
    if team.get('created'):
        lines.append(f'**Created:** {team["created"]}')
    if team.get('updated'):
        lines.append(f'**Updated:** {team["updated"]}')
    if team.get('metaSnapshot'):
        lines.append(f'**Meta Snapshot:** {team["metaSnapshot"]}')
    if team.get('seedReference'):
        lines.append(f'**Seed Reference:** {team["seedReference"]}')
    if team.get('winCondition'):
        lines.append(f'**Win Condition:** {team["winCondition"]}')
    lines.append('')
    if team.get('notes'):
        lines.append('## Team Philosophy')
        lines.append('')
        lines.append(team['notes'])
        lines.append('')

    lines.append('## Team Summary')
    lines.append('')
    lines.append('| # | Role | Pokemon | Item | Ability | Move 1 | Move 2 | Move 3 | Move 4 |')
    lines.append('| --- | --- | --- | --- | --- | --- | --- | --- | --- |')
    for slot in team.get('slots', []):
        if not slot.get('pokemon'):
            continue
        moves = (slot.get('moves', []) + ['', '', '', ''])[:4]
        row = [
            str(slot.get('slot', '')),
            slot.get('role', '') or '',
            slot.get('pokemon', '') or '',
            slot.get('item', '') or '',
            slot.get('ability', '') or '',
            *[m or '' for m in moves],
        ]
        lines.append('| ' + ' | '.join(row) + ' |')
    lines.append('')

    lines.append('## Roster')
    lines.append('')
    for slot in team.get('slots', []):
        if not slot.get('pokemon'):
            continue
        lines.append(f'### {slot.get("slot")}. {slot.get("pokemon")} @ {slot.get("item") or ": "}')
        lines.append('')
        lines.append('```text')
        lines.append(f'Ability: {slot.get("ability") or ": "}')
        lines.append(f'EVs: {_formatEvs(slot.get("evs", {}))}')
        lines.append(f'Nature: {slot.get("nature") or ": "}')
        for move in slot.get('moves', []):
            if move:
                lines.append(f'- {move}')
        lines.append('```')
        lines.append('')
        if slot.get('notes'):
            lines.append(slot['notes'])
            lines.append('')

    return '\n'.join(lines).rstrip() + '\n'
