# Pokemon Champions Meta Lab

An interactive meta explorer and team builder for [Pokemon Champions](https://www.pokemon.com/us/pokemon-video-games/pokemon-champions) VGC, built with Streamlit.

It turns a folder of competitive research, Pikalytics usage snapshots, per-Pokemon data, and hand-written team documents, into a browsable app: explore the current meta, drill into any Pokemon's moves/items/abilities/teammates, and assemble teams in a six-slot editor that enforces the Item Clause, Species Clause, Champions item legality, and EV caps as you build.

## Features

- **Meta Explorer**: sortable usage table, per-Pokemon detail charts (moves, items, abilities, teammates), base-stat bars, and a teammate-correlation heatmap.
- **Team Builder**: six editable slots with usage-ranked, free-text dropdowns for Pokemon, items, abilities, and moves; per-stat EV inputs with a 508 total; live validation panel.
- **Legality checks**: Item Clause (no duplicate held items), Species Clause (base and Mega forms count as one), Champions item/move legality against a curated pool, and EV caps. Soft warnings, never hard blocks.
- **Structured team store**: teams are saved as JSON in `docs/teams/data/` and exported to a markdown build document in `docs/teams/builds/` so the human-readable artifact stays in sync.
- **On-demand meta refresh**: a button re-scrapes Pikalytics Champions and writes a new dated snapshot, reusing the CLI tools in `tools/`. The app reads committed snapshots by default.

## Quickstart

```bash
pip install -r requirements.txt
streamlit run app/Home.py
```

Run from the repository root. The app reads the latest committed snapshot in `docs/snapshots/`; no network access is needed to explore or build.

## Architecture

```
app/                       Streamlit multipage app
├─ Home.py                 landing + snapshot status + refresh
├─ pages/
│  ├─ 1_Meta_Explorer.py   usage browsing + per-Pokemon detail + teammate heatmap
│  ├─ 2_Team_Builder.py    six-slot editor with live validation
│  └─ 3_Saved_Teams.py     list / preview / export saved teams
├─ dataAccess.py           cached loaders for snapshots, profiles, legal pool
├─ teamStore.py            team JSON load/save + markdown export
├─ legality.py             Item/Species clause, legality, EV checks
├─ charts.py               plotly chart helpers
├─ refresh.py              wrappers over tools/ scrapers for the refresh button
└─ theme.py                shared dark copper-amber styling

docs/                      data layer (read by the app)
├─ snapshots/              dated Pikalytics meta snapshots
├─ pokemon/                PokeAPI profiles
│  └─ champions/           per-Pokemon Champions usage data
├─ teams/data/             structured team JSON (the working store)
├─ teams/builds/           markdown build docs (exported from JSON)
└─ champions_legal_pool.json   curated item/move legality

tools/                     CLI data fetchers
├─ fetch_meta_stats.py     Pikalytics Champions usage scraper
├─ fetch_pokemon_data.py   PokeAPI profile fetcher
└─ migrate_builds.py       one-shot markdown build -> team JSON migration
```

Data flows one direction: `tools/` scrapers write JSON into `docs/`, `dataAccess.py` loads it (cached), and the pages render it. The Team Builder writes back to `docs/teams/`.

## Refreshing data

The in-app **Refresh from Pikalytics** button (Home page) scrapes the live Champions meta and writes a new `docs/snapshots/meta_stats_<date>.json` plus per-Pokemon files. The equivalent CLI calls:

```bash
python tools/fetch_meta_stats.py --detail        # usage snapshot + per-Pokemon detail
python tools/fetch_pokemon_data.py dragonite      # a PokeAPI profile
```

The refresh button scrapes a third-party site and writes files into your local clone: it is a convenience for the maintainer, not a shared service.

## Data model

- **Team JSON**: `schemaVersion`, team metadata (`name`, `format`, `winCondition`, `metaSnapshot`, …), and six `slots`, each with `pokemon`, `item`, `ability`, four `moves`, an `evs` dict (`hp/atk/def/spa/spd/spe`), `nature`, `role`, and `notes`.
- **Legal pool** (`docs/champions_legal_pool.json`): curated `items.available` / `items.unavailable` lists, per-Pokemon `moveOverrides`, and `rules` (level cap, EV caps, clauses). This is **hand-maintained** and carries a `lastReviewed` date; the Champions item pool expands via live-service updates, so verify against the [Game8 items list](https://game8.co/games/Pokemon-Champions/archives/588871) before trusting a result.

## Limitations

- Per-Pokemon Champions detail exists only for the Pokemon that have been fetched (the explorer and builder dropdowns reflect that set and grow as you fetch more).
- PokeAPI lacks the newest Mega forms (e.g. Mega Dragonite); those Pokemon have no base-stat/learnset profile, and the builder falls back to usage data plus free text.
- Legality is advisory, not authoritative: see the legal-pool note above.

## Data sources & attribution

- [Pikalytics](https://www.pikalytics.com/champions): Champions usage statistics.
- [PokeAPI](https://pokeapi.co/): base stats, typing, learnsets.
- [Game8](https://game8.co/games/Pokemon-Champions): Champions-specific legality (items, learnsets).

See `docs/references_competitive_resources_2026-04-14.md` for the full annotated bibliography.

## Conventions

Python: camelCase functions/variables, PascalCase classes, single quotes, type hints, triple-single-quoted docstrings.

## License

MIT: see `LICENSE`.
