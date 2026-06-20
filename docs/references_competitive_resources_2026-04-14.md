# Competitive Pokemon Research Resources -- Annotated Bibliography

**Session:** 2026-04-14  
**Purpose:** Persistent reference catalogue for competitive Pokemon team building and meta game analysis. Intended to be read by Claude agents operating in this repository to guide research and tool targeting. Entries are grouped by category and marked with intended use cases.

---

## Category 1: Pokemon Champions -- Official

### Pokemon Champions Official Site
- **URL:** https://champions.pokemon.com/en-us/
- **Accessed:** 2026-04-14
- **Relevance:** The official landing page for Pokemon Champions, the new free-to-play competitive battling game launched April 8, 2026. Primary authoritative source for game announcements, format updates, and official ruleset documents.
- **Key findings:**
  - Pokemon Champions is free-to-start on Nintendo Switch and Switch 2, with mobile releases planned for 2026
  - Game is exclusively focused on competitive battling: no exploration, story, or catching
  - 186 Pokemon available at launch; players can import Pokemon via Pokemon HOME
  - Supports Single Battles and Double Battles
  - As of 2026, all official VGC tournaments are played on Pokemon Champions, replacing Scarlet/Violet

### Nintendo -- Pokemon Champions Announcement
- **URL:** https://www.nintendo.com/us/whatsnew/get-battling-with-the-new-free-to-start-game-pokemon-champions/
- **Accessed:** 2026-04-14
- **Relevance:** Nintendo's official announcement page covering launch details, platform availability, and game overview.
- **Key findings:**
  - Launched April 8, 2026 on Nintendo Switch and Switch 2
  - Free-to-start model with optional cosmetic purchases
  - Monetization is cosmetic-only; all competitive items earnable in-game
  - Monthly membership subscription and seasonal battle passes available

---

## Category 2: Meta Analysis -- Pokemon Champions Specific

### Pikalytics Champions
- **URL:** https://www.pikalytics.com/champions
- **Accessed:** 2026-04-14
- **Relevance:** The primary statistical usage tracker for Pokemon Champions. Tracks which Pokemon, moves, items, abilities, and teammates appear most frequently at high ranks. Updated in near-real-time from ladder data. This is the first resource to check for current meta snapshots.
- **Key findings:**
  - Provides per-Pokemon usage percentages across the Champions ranked ladder
  - Shows common move spreads, item distributions, and ability selections
  - Teammate correlation data useful for identifying meta cores
  - The `tools/fetch_meta_stats.py` utility in this repository is designed to scrape this source

### ChampionsLab Meta Analysis and Team Builder
- **URL:** https://championslab.xyz/meta
- **Accessed:** 2026-04-14
- **Relevance:** Community-built meta analysis hub for Pokemon Champions. Aggregates team compositions, win rates, and meta tier assessments.
- **Key findings:**
  - Provides team submission and sharing functionality
  - Tier list and meta narrative updated by community contributors
  - Useful for finding sample teams around specific cores or win conditions
  - Supplements Pikalytics usage stats with qualitative meta analysis

### Game8 Pokemon Champions Coverage
- **URL:** https://game8.co/games/Pokemon-Champions
- **Accessed:** 2026-04-14
- **Relevance:** Comprehensive wiki-style coverage of Pokemon Champions including individual Pokemon guides, tier lists, meta analysis, and team recommendations. Game8 is a professional game guide site with dedicated editors.
- **Key findings:**
  - Hosts the primary tier list for Pokemon Champions: https://game8.co/games/Pokemon-Champions/archives/592465
  - Individual Pokemon guides include moveset recommendations, EV spreads, and synergy notes
  - Mega Dragonite guide: https://game8.co/games/Pokemon-Champions/archives/592442
  - Best team recommendations updated regularly: https://game8.co/games/Pokemon-Champions/archives/593949

### Pokemon-Zone Champions Meta
- **URL:** https://www.pokemon-zone.com/champions/
- **Accessed:** 2026-04-14
- **Relevance:** Additional meta analysis resource specific to Pokemon Champions. Useful as a secondary source to cross-reference Pikalytics and ChampionsLab data.
- **Key findings:**
  - Covers format-specific meta developments
  - Provides team archetypes and role analysis

### StrataDex Tier List and Team Builder
- **URL:** https://stratadex.net/tierlist
- **Accessed:** 2026-04-14
- **Relevance:** Community tier list and team building tool for Pokemon Champions. Useful for quickly assessing a Pokemon's perceived viability without digging into raw usage data.
- **Key findings:**
  - Tier list is community-voted and updated regularly
  - Includes team builder with synergy checking
  - Good starting point for format viability assessments before deeper meta research

---

## Category 3: Smogon / Pokemon Showdown (Singles Competitive)

### Smogon University
- **URL:** https://www.smogon.com/
- **Accessed:** 2026-04-14
- **Relevance:** The definitive hub for singles competitive Pokemon. Smogon maintains the most widely used tier system (Ubers, OU, UU, RU, NU, PU), publishes moveset analyses for every relevant Pokemon, and runs the Pokemon Showdown simulator. Essential background reading for understanding singles team building philosophy.
- **Key findings:**
  - Tiers based on usage: Pokemon with >4.52% usage are OU; those below fall to lower tiers
  - Publishes community-vetted sets with EV spreads, natures, and move justifications
  - Hosts the Rate My Team (RMT) forum for public team feedback
  - Viability ranking threads track tier placement changes as the meta evolves
  - Note: Smogon formats are separate from official VGC/Champions formats; useful for theory and movepool research but not directly applicable to Pokemon Champions

### Smogon Rate My Team Forum
- **URL:** https://www.smogon.com/forums/forums/rate-my-team.52/
- **Accessed:** 2026-04-14
- **Relevance:** Community team critique forum. Useful for learning team building methodology by reading critique threads, even for non-Smogon formats.
- **Key findings:**
  - Organized by format (OU, VGC, etc.)
  - Responses typically identify type/speed/role weaknesses and suggest specific replacements
  - Reading a few high-quality RMT threads is one of the fastest ways to internalize meta team building logic

### Pokemon Showdown
- **URL:** https://pokemonshowdown.com/
- **Accessed:** 2026-04-14
- **Relevance:** The primary online battle simulator for competitive Pokemon. Free, browser-based, no EVs/IVs grinding required. Used for practicing teams and testing builds before committing to official ladders. Also hosts usage statistics updated monthly.
- **Key findings:**
  - Supports all Smogon tiers plus VGC formats
  - Built-in team builder with legality checking and damage calculator
  - Monthly usage stats published at https://www.smogon.com/stats/ (gen9ou, gen9vgc, etc.)
  - Battle replays stored at https://replay.pokemonshowdown.com/

### Pokemon Showdown Competitive Pokedex
- **URL:** https://dex.pokemonshowdown.com/
- **Accessed:** 2026-04-14
- **Relevance:** Competitive-oriented Pokedex maintained by the Showdown team. Shows learnsets, base stats, and tier placements in a format optimized for team building research.
- **Key findings:**
  - Faster to navigate than Bulbapedia for pure competitive data lookups
  - Shows all legal moves, abilities, and items with competitive context
  - Links directly to Smogon analysis pages

---

## Category 4: VGC (Video Game Championships) Resources

### Victory Road
- **URL:** https://victoryroad.pro/
- **Accessed:** 2026-04-14
- **Relevance:** The most comprehensive VGC community resource hub. Covers tournament results, team breakdowns, usage data, and rental teams for the current VGC season. Since Pokemon Champions is now the VGC platform, this site will cover Champions meta directly.
- **Key findings:**
  - Archives team sheets from major VGC events with full 6-Pokemon + item + move details
  - Rental team database allows importing championship-level teams directly to practice
  - Post-event coverage explains why winning teams were built the way they were
  - VGC coverage: https://victoryroad.pro/sv-rental-teams/

### Limitless VGC
- **URL:** https://limitlessvgc.com/
- **Accessed:** 2026-04-14
- **Relevance:** Tournament database covering regional, national, and world championships. Tracks player records, team usage across tournaments, and tournament brackets.
- **Key findings:**
  - Complete tournament results with team compositions for top finishers
  - Useful for identifying which Pokemon appear consistently at the top tables
  - Player profiles track individual competitive histories

### VGC Guide
- **URL:** https://www.vgcguide.com/
- **Accessed:** 2026-04-14
- **Relevance:** Educational VGC resource with guides on mechanics, formats, and team building specifically for the VGC ruleset (restricted/unrestricted formats, 4-of-6 team preview, etc.).
- **Key findings:**
  - Explains VGC-specific mechanics that differ from singles (e.g., Doubles positioning, spread moves, redirection)
  - Good onboarding resource for players transitioning from singles to VGC
  - Covers seasonal format changes and restricted Pokemon rules

### Play! Pokemon Official Rules
- **URL:** https://play.pokemon.com/en-us/resources/rules/?category=vgc
- **Accessed:** 2026-04-14
- **Relevance:** Official tournament rules and regulations from The Pokemon Company. The authoritative source for format legality, banned Pokemon/moves, and ruleset documents.
- **Key findings:**
  - Defines the current VGC format ruleset
  - Lists all banned moves, abilities, and items
  - Updated each season; always verify against this source before submitting to official tournaments

---

## Category 5: Pokemon Databases

### Bulbapedia
- **URL:** https://bulbapedia.bulbagarden.net/wiki/Main_Page
- **Accessed:** 2026-04-14
- **Relevance:** The most comprehensive Pokemon encyclopedia. Best source for complete learnsets (including egg moves and tutor moves), ability descriptions, item interactions, and game-specific mechanic changes across generations.
- **Key findings:**
  - Individual Pokemon pages include full learnsets organized by method (level-up, TM, egg, tutor)
  - Ability and item pages include all edge cases and interactions
  - Covers all games including Pokemon Champions and Legends: Z-A where Mega Dragonite was introduced
  - Mega Dragonite: https://bulbapedia.bulbagarden.net/wiki/Dragonite_(Pok%C3%A9mon)
  - Dragonitite (Mega Stone): https://bulbapedia.bulbagarden.net/wiki/Dragoninite

### Pokemon Database
- **URL:** https://pokemondb.net/pokedex
- **Accessed:** 2026-04-14
- **Relevance:** Clean, fast Pokemon database covering base stats, type charts, move listings, and evolution chains. Easier to navigate than Bulbapedia for quick stat lookups.
- **Key findings:**
  - Excellent type effectiveness calculator
  - Clear visualization of base stat distributions
  - Dragonite page: https://pokemondb.net/pokedex/dragonite
  - Does not always reflect the most recent game releases immediately

### Serebii.net
- **URL:** https://www.serebii.net/
- **Accessed:** 2026-04-14
- **Relevance:** Long-running Pokemon site known for fast coverage of new game releases and competitive news. Often has information on new games (including Pokemon Champions) faster than Bulbapedia due to Joe Merrick's update cadence.
- **Key findings:**
  - Comprehensive competitive data including event distributions, held items, and format changes
  - Serebii Pokedex: https://www.serebii.net/pokemon/
  - Often first to report on new Pokemon forms, moves, and abilities in new releases

---

## Category 6: Replay Analysis

### Pokemon Showdown Replay Database
- **URL:** https://replay.pokemonshowdown.com/
- **Accessed:** 2026-04-14
- **Relevance:** Official repository for all saved Pokemon Showdown battles. Searchable by format, player, and Pokemon. Watching high-ladder replays is one of the best ways to understand how top teams actually function in practice.
- **Key findings:**
  - Replays are automatically saved and shareable via URL
  - Filter by format to find current high-ranked battles
  - Useful for studying how specific cores play out across multiple games

### Clodbot Battle Analyzer
- **URL:** https://clodbot.com/analyze.html
- **Accessed:** 2026-04-14
- **Relevance:** Quick statistical analysis tool for Pokemon Showdown replays. Paste a replay URL and get kill/death data, damage dealt, and performance metrics for each Pokemon.
- **Key findings:**
  - Identifies which Pokemon in a team carried vs. underperformed across a session
  - Useful for evaluating whether a team member is pulling its weight
  - Works with any Showdown replay URL

---

## Category 7: Content Creators and Community

### WolfeyVGC (Wolfe Glick)
- **URL:** https://www.youtube.com/@WolfeyVGC
- **Accessed:** 2026-04-14
- **Relevance:** Wolfe Glick is a 2016 Pokemon World Champion and one of the most influential figures in the VGC community. His content covers cutting-edge team building, innovative strategies that often shape the meta, and high-level tournament play analysis.
- **Key findings:**
  - 1 million+ YouTube subscribers; widely regarded as the best English-language VGC analyst
  - Known for finding off-meta strategies that later become widely adopted
  - Content is primarily Doubles/VGC focused
  - Following his channel provides real-time meta reads from a top player's perspective

---

## Usage Notes for Claude Agents

When researching the current Pokemon Champions meta for team building:

1. **Start with Pikalytics** (`pikalytics.com/champions`) for quantitative usage data
2. **Cross-reference Game8** for move set recommendations and individual Pokemon guides
3. **Check Victory Road** for full team sheets from recent tournament events
4. **Verify legality** against the official Play! Pokemon rules page
5. **Use Bulbapedia** for complete learnset and ability interaction data
6. The `tools/fetch_meta_stats.py` script can automate Pikalytics snapshots
7. The `tools/fetch_pokemon_data.py` script can pull PokeAPI data for mainline Pokemon (note: Mega Dragonite may not yet be in PokeAPI as it was introduced in Legends: Z-A in 2025)
