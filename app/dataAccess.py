'''
Data-access layer for the Streamlit app.

Loads committed JSON artifacts from docs/ and exposes them to the pages:
    - meta usage snapshots      (docs/snapshots/meta_stats_YYYY-MM-DD.json)
    - per-Pokemon Champions data (docs/pokemon/champions/<slug>_champions.json)
    - PokeAPI profiles           (docs/pokemon/<name>.json)
    - the curated legal pool     (docs/champions_legal_pool.json)

All disk reads are cached with @st.cache_data keyed on a `cacheBust` token so the
refresh button can invalidate them by bumping the token in session state.
'''

import json
import re
from pathlib import Path

import streamlit as st

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_DIR = REPO_ROOT / 'docs' / 'snapshots'
CHAMPIONS_DIR = REPO_ROOT / 'docs' / 'pokemon' / 'champions'
POKEMON_DIR = REPO_ROOT / 'docs' / 'pokemon'
TEAM_DIR = REPO_ROOT / 'docs' / 'teams' / 'data'
BUILD_DIR = REPO_ROOT / 'docs' / 'teams' / 'builds'
LEGAL_POOL_PATH = REPO_ROOT / 'docs' / 'champions_legal_pool.json'

# Matches meta_stats_2026-04-14.json -> ('2026', '04', '14')
_SNAPSHOT_DATE = re.compile(r'meta_stats_(\d{4})-(\d{2})-(\d{2})\.json$')


def cacheBust() -> int:
    '''
    Return the current cache-bust token from session state.

    Pages pass this into the cached loaders; the refresh button increments it
    (see app/refresh.py) so the next read re-hits disk instead of the cache.
    '''
    return int(st.session_state.get('cacheBust', 0))


def bumpCacheBust() -> None:
    '''Invalidate cached reads by advancing the cache-bust token.'''
    st.session_state['cacheBust'] = cacheBust() + 1


def slugify(name: str) -> str:
    '''
    Convert a display name to the Champions file slug used on disk.

    Mirrors the scraper's rule (lowercase, spaces -> hyphens) and strips a
    leading 'Mega ' so 'Mega Dragonite' resolves to dragonite_champions.json.
    '''
    base = stripMega(name)
    return base.lower().strip().replace(' ', '-')


def stripMega(name: str) -> str:
    '''Drop a leading 'Mega ' prefix so base and Mega forms compare equal.'''
    if name and name.lower().startswith('mega '):
        return name[5:].strip()
    return name.strip() if name else name


def _readJson(path: Path) -> dict | None:
    '''Read a JSON file, returning None if it is missing or malformed.'''
    if not path.exists():
        return None
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


@st.cache_data(show_spinner=False)
def listSnapshots(cacheBust: int = 0) -> list[str]:
    '''Return snapshot file paths (as strings) sorted newest-first by filename date.'''
    if not SNAPSHOT_DIR.exists():
        return []

    def sortKey(path: Path) -> tuple:
        match = _SNAPSHOT_DATE.search(path.name)
        if match:
            return (1, match.group(0), path.name)
        # Files without a parseable date fall back to mtime, ranked below dated ones
        return (0, f'{path.stat().st_mtime:020.0f}', path.name)

    paths = sorted(SNAPSHOT_DIR.glob('meta_stats_*.json'), key=sortKey, reverse=True)
    return [str(p) for p in paths]


@st.cache_data(show_spinner=False)
def loadSnapshot(path: str | None = None, cacheBust: int = 0) -> dict | None:
    '''
    Load a meta snapshot. Defaults to the latest by filename date.

    Returns the on-disk structure: {source, fetched, format, pokemon[...]}.
    '''
    if path is None:
        snapshots = listSnapshots(cacheBust)
        if not snapshots:
            return None
        path = snapshots[0]
    return _readJson(Path(path))


@st.cache_data(show_spinner=False)
def loadChampionsDetail(name: str, cacheBust: int = 0) -> dict | None:
    '''Load per-Pokemon Champions data ({moves, items, abilities, teammates}).'''
    return _readJson(CHAMPIONS_DIR / f'{slugify(name)}_champions.json')


@st.cache_data(show_spinner=False)
def loadAllChampionsDetail(cacheBust: int = 0) -> dict[str, dict]:
    '''Load every Champions detail file, keyed by display name.'''
    if not CHAMPIONS_DIR.exists():
        return {}
    out: dict[str, dict] = {}
    for path in sorted(CHAMPIONS_DIR.glob('*_champions.json')):
        data = _readJson(path)
        if data and data.get('name'):
            out[data['name']] = data
    return out


@st.cache_data(show_spinner=False)
def availableChampionsPokemon(cacheBust: int = 0) -> list[str]:
    '''Display names that have committed Champions detail data, sorted A-Z.'''
    return sorted(loadAllChampionsDetail(cacheBust).keys())


@st.cache_data(show_spinner=False)
def loadPokemonProfile(name: str, cacheBust: int = 0) -> dict | None:
    '''
    Load a PokeAPI profile (base_stats/types/abilities/moves) for a Pokemon.

    Returns None when no profile is committed (e.g. Mega forms PokeAPI lacks).
    '''
    return _readJson(POKEMON_DIR / f'{slugify(name)}.json')


@st.cache_data(show_spinner=False)
def loadLegalPool(cacheBust: int = 0) -> dict:
    '''Load the curated Champions legal pool, or an empty skeleton if absent.'''
    data = _readJson(LEGAL_POOL_PATH)
    if data is None:
        return {'items': {'available': [], 'unavailable': []}, 'moveOverrides': {}, 'rules': {}}
    return data
