'''
Fetch complete Pokemon data from PokeAPI and save as JSON.

Usage:
    python tools/fetch_pokemon_data.py <pokemon_name>
    python tools/fetch_pokemon_data.py dragonite
    python tools/fetch_pokemon_data.py garchomp --output docs/pokemon/garchomp.json

Output saved to docs/pokemon/<name>.json by default.

Notes:
    - PokeAPI covers all mainline Pokemon through Generation 9.
    - Newly introduced forms (e.g., Mega Dragonite from Legends: Z-A, 2025) may not yet
      be in PokeAPI. This script will print a warning and skip missing entries.
    - Run with --supplement to open a prompt for manually adding Mega form data after fetch.
'''

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

try:
    import requests
except ImportError:
    print('requests not installed. Run: pip install requests')
    sys.exit(1)


POKEAPI_BASE = 'https://pokeapi.co/api/v2'
OUTPUT_DIR = Path(__file__).parent.parent / 'docs' / 'pokemon'


def fetchJson(url: str) -> dict | None:
    '''Fetch JSON from a URL; return None on any error.'''
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        print(f'  Warning: failed to fetch {url}: {e}')
        return None


def fetchBaseStats(pokemonData: dict) -> dict:
    '''Extract base stats from PokeAPI pokemon response.'''
    statMap = {
        'hp': 'hp',
        'attack': 'atk',
        'defense': 'def',
        'special-attack': 'spa',
        'special-defense': 'spd',
        'speed': 'spe',
    }
    stats = {}
    for entry in pokemonData.get('stats', []):
        name = entry['stat']['name']
        if name in statMap:
            stats[statMap[name]] = entry['base_stat']
    return stats


def fetchTypes(pokemonData: dict) -> list[str]:
    '''Extract type names from PokeAPI pokemon response.'''
    return [t['type']['name'] for t in pokemonData.get('types', [])]


def fetchAbilities(pokemonData: dict) -> dict:
    '''Extract abilities (normal + hidden) from PokeAPI pokemon response.'''
    abilities = {'normal': [], 'hidden': None}
    for entry in pokemonData.get('abilities', []):
        name = entry['ability']['name']
        if entry['is_hidden']:
            abilities['hidden'] = name
        else:
            abilities['normal'].append(name)
    return abilities


def fetchMoves(pokemonData: dict) -> dict:
    '''
    Organize full learnset by learn method.
    Returns dict keyed by method name, each containing a sorted list of move names.
    '''
    methods: dict[str, list[str]] = {}
    for entry in pokemonData.get('moves', []):
        moveName = entry['move']['name']
        for versionDetail in entry['version_group_details']:
            method = versionDetail['move_learn_method']['name']
            if method not in methods:
                methods[method] = []
            if moveName not in methods[method]:
                methods[method].append(moveName)
    # Sort each method's move list alphabetically
    return {method: sorted(moves) for method, moves in sorted(methods.items())}


def fetchSpeciesData(speciesUrl: str) -> dict:
    '''Fetch species-level data (evolution chain, egg groups, etc.).'''
    data = fetchJson(speciesUrl)
    if not data:
        return {}
    return {
        'egg_groups': [eg['name'] for eg in data.get('egg_groups', [])],
        'gender_rate': data.get('gender_rate'),  # -1 = genderless, 0-8 = female ratio
        'base_happiness': data.get('base_happiness'),
        'capture_rate': data.get('capture_rate'),
        'is_legendary': data.get('is_legendary', False),
        'is_mythical': data.get('is_mythical', False),
        'evolves_from': data.get('evolves_from_species', {}).get('name') if data.get('evolves_from_species') else None,
    }


def fetchPokemon(name: str) -> dict | None:
    '''
    Fetch complete Pokemon data from PokeAPI.
    Returns structured dict or None if the Pokemon is not found.
    '''
    url = f'{POKEAPI_BASE}/pokemon/{name.lower().strip()}'
    print(f'Fetching {name} from PokeAPI...')
    pokemonData = fetchJson(url)

    if pokemonData is None:
        print(f'  {name} not found in PokeAPI.')
        print('  This may be a recently introduced Pokemon (e.g., new Mega form from Legends: Z-A).')
        print('  Consider supplementing manually: see docs/pokemon/ for JSON format.')
        return None

    print(f'  Found: {pokemonData["name"]} (ID #{pokemonData["id"]})')

    print('  Fetching species data...')
    speciesData = fetchSpeciesData(pokemonData['species']['url'])

    result = {
        'name': pokemonData['name'],
        'id': pokemonData['id'],
        'base_stats': fetchBaseStats(pokemonData),
        'types': fetchTypes(pokemonData),
        'abilities': fetchAbilities(pokemonData),
        'weight_kg': pokemonData.get('weight', 0) / 10,
        'height_m': pokemonData.get('height', 0) / 10,
        'species': speciesData,
        'moves': fetchMoves(pokemonData),
        'source': f'{POKEAPI_BASE}/pokemon/{name.lower()}',
        'fetched': str(date.today()),
    }

    return result


def saveResult(data: dict, outputPath: Path) -> None:
    '''Save fetched data to JSON file.'''
    outputPath.parent.mkdir(parents=True, exist_ok=True)
    with open(outputPath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f'  Saved to {outputPath}')


def printSummary(data: dict) -> None:
    '''Print a compact summary of the fetched Pokemon to stdout.'''
    stats = data.get('base_stats', {})
    bst = sum(stats.values())
    print(f'\n=== {data["name"].upper()} ===')
    print(f'  Types:   {" / ".join(data["types"])}')
    print(f'  Ability: {data["abilities"]["normal"]}  |  Hidden: {data["abilities"]["hidden"]}')
    print(f'  Stats:   HP {stats.get("hp")} / Atk {stats.get("atk")} / Def {stats.get("def")} '
          f'/ SpA {stats.get("spa")} / SpD {stats.get("spd")} / Spe {stats.get("spe")}  (BST: {bst})')
    moveCounts = {method: len(moves) for method, moves in data.get('moves', {}).items()}
    print(f'  Moves:   {moveCounts}')


def main() -> None:
    parser = argparse.ArgumentParser(description='Fetch Pokemon data from PokeAPI')
    parser.add_argument('pokemon', help='Pokemon name (e.g., dragonite, garchomp)')
    parser.add_argument(
        '--output', '-o',
        help='Output JSON path (default: docs/pokemon/<name>.json)',
        default=None,
    )
    args = parser.parse_args()

    outputPath = Path(args.output) if args.output else OUTPUT_DIR / f'{args.pokemon.lower()}.json'

    data = fetchPokemon(args.pokemon)
    if data is None:
        sys.exit(1)

    saveResult(data, outputPath)
    printSummary(data)


if __name__ == '__main__':
    main()
