'''
Refresh helpers that reuse the existing CLI scrapers in tools/.

These wrap tools.fetch_meta_stats and tools.fetch_pokemon_data so the Streamlit
refresh button can pull fresh data on demand. Calls are blocking and run inside a
st.spinner — adequate for a single-user portfolio app; no background job system.

Network failures degrade gracefully: fetchOverview returns [] on error, which we
surface as a warning while the app keeps reading the last committed snapshot.
'''

from datetime import date
from pathlib import Path

from app import dataAccess
from tools import fetch_meta_stats as metaTool
from tools import fetch_pokemon_data as pokemonTool


def refreshMeta(topN: int = 30, fetchDetail: bool = True) -> dict:
    '''
    Scrape the current Champions meta and write a dated snapshot.

    Reuses metaTool.fetchOverview / buildSnapshot / saveSnapshot (the latter two
    also write per-Pokemon docs/pokemon/champions/<slug>_champions.json when
    fetchDetail is True). Returns a result dict for the UI.
    '''
    usageList = metaTool.fetchOverview(topN=topN)
    if not usageList:
        return {'ok': False, 'message': 'Fetch failed — showing last committed snapshot.'}

    snapshot = metaTool.buildSnapshot(usageList, fetchDetail=fetchDetail)
    outputPath = dataAccess.SNAPSHOT_DIR / f'meta_stats_{date.today()}.json'
    metaTool.saveSnapshot(snapshot, outputPath)
    return {
        'ok': True,
        'message': f'Saved {outputPath.name} with {len(snapshot["pokemon"])} Pokemon.',
        'path': str(outputPath),
        'count': len(snapshot['pokemon']),
    }


def refreshProfile(name: str) -> dict:
    '''
    Fetch a single PokeAPI profile and write docs/pokemon/<name>.json.

    Returns a result dict; ok is False when PokeAPI lacks the Pokemon (common for
    Mega forms not yet in the API).
    '''
    data = pokemonTool.fetchPokemon(name)
    if data is None:
        return {'ok': False, 'message': f'{name} not found in PokeAPI (e.g. a new Mega form).'}

    outputPath = dataAccess.POKEMON_DIR / f'{dataAccess.slugify(name)}.json'
    pokemonTool.saveResult(data, Path(outputPath))
    return {'ok': True, 'message': f'Saved {Path(outputPath).name}.', 'path': str(outputPath)}
