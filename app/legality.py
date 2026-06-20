'''
Team validation against Pokemon Champions rules.

Checks are intentionally soft, they return messages, never block saving, because
the curated legal pool (docs/champions_legal_pool.json) is incomplete and expected
to expand. Each check yields {level, message} where level is 'error' | 'warning'.
'''

from app import dataAccess

_LEVEL_ERROR = 'error'
_LEVEL_WARNING = 'warning'

# Known Pikalytics spelling variants normalised to the canonical item name
_ITEM_ALIASES = {
    'dragoninite': 'dragonitite',
}


def _normItem(name: str) -> str:
    '''Lowercase, trim, and resolve known scraped-name typos for tolerant matching.'''
    key = (name or '').strip().lower()
    return _ITEM_ALIASES.get(key, key)


def _filledSlots(team: dict) -> list[dict]:
    '''Return slots that have a Pokemon assigned.'''
    return [s for s in team.get('slots', []) if s.get('pokemon')]


def checkSpeciesClause(team: dict) -> list[dict]:
    '''Flag duplicate species. Base and Mega forms count as the same species.'''
    seen: dict[str, int] = {}
    for slot in _filledSlots(team):
        species = dataAccess.stripMega(slot['pokemon']).lower()
        seen[species] = seen.get(species, 0) + 1
    return [
        {'level': _LEVEL_ERROR, 'message': f'Species Clause: {name.title()} appears {count} times.'}
        for name, count in seen.items() if count > 1
    ]


def checkItemClause(team: dict) -> list[dict]:
    '''Flag duplicate held items across the team.'''
    seen: dict[str, list[str]] = {}
    for slot in _filledSlots(team):
        item = slot.get('item')
        if item:
            seen.setdefault(_normItem(item), []).append(item)
    out = []
    for variants in seen.values():
        if len(variants) > 1:
            out.append({
                'level': _LEVEL_ERROR,
                'message': f'Item Clause: "{variants[0]}" is held by {len(variants)} Pokemon.',
            })
    return out


def checkItemLegality(team: dict, legalPool: dict) -> list[dict]:
    '''Warn on items in the unavailable list or absent from the available pool.'''
    items = legalPool.get('items', {})
    available = {_normItem(i) for i in items.get('available', [])}
    unavailable = {_normItem(i) for i in items.get('unavailable', [])}
    out = []
    for slot in _filledSlots(team):
        item = slot.get('item')
        if not item:
            continue
        norm = _normItem(item)
        if norm in unavailable:
            out.append({'level': _LEVEL_ERROR,
                        'message': f'{slot["pokemon"]}: "{item}" is not available in Champions.'})
        elif available and norm not in available:
            out.append({'level': _LEVEL_WARNING,
                        'message': f'{slot["pokemon"]}: "{item}" is not in the known legal pool: verify.'})
    return out


def checkMoveLegality(team: dict, legalPool: dict) -> list[dict]:
    '''Warn on moves explicitly banned for a Pokemon in the legal pool overrides.'''
    overrides = legalPool.get('moveOverrides', {})
    out = []
    for slot in _filledSlots(team):
        species = dataAccess.stripMega(slot['pokemon'])
        banned = {m.lower() for m in overrides.get(species, {}).get('banned', [])}
        for move in slot.get('moves', []):
            if move and move.lower() in banned:
                out.append({'level': _LEVEL_WARNING,
                            'message': f'{slot["pokemon"]}: "{move}" is not in its Champions learnset.'})
    return out


def checkEvs(team: dict, legalPool: dict) -> list[dict]:
    '''Flag EV spreads exceeding the per-stat (252) or total (508) caps.'''
    rules = legalPool.get('rules', {})
    totalCap = rules.get('evTotalCap', 508)
    perStatCap = rules.get('evPerStatCap', 252)
    out = []
    for slot in _filledSlots(team):
        evs = slot.get('evs') or {}
        total = sum(int(v or 0) for v in evs.values())
        if total > totalCap:
            out.append({'level': _LEVEL_ERROR,
                        'message': f'{slot["pokemon"]}: EV total {total} exceeds {totalCap}.'})
        for stat, value in evs.items():
            if int(value or 0) > perStatCap:
                out.append({'level': _LEVEL_WARNING,
                            'message': f'{slot["pokemon"]}: {stat.upper()} EVs {value} exceed {perStatCap}.'})
    return out


def validateTeam(team: dict, legalPool: dict) -> list[dict]:
    '''Run all checks and return a flat list of {level, message} findings.'''
    findings: list[dict] = []
    findings += checkSpeciesClause(team)
    findings += checkItemClause(team)
    findings += checkItemLegality(team, legalPool)
    findings += checkMoveLegality(team, legalPool)
    findings += checkEvs(team, legalPool)
    return findings
