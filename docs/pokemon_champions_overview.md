# Pokemon Champions -- Game Reference

**Audience:** Claude agents operating in this repository. This document provides specific context on Pokemon Champions to ensure advice and team building suggestions are in alignment with the game's ruleset, roster, and mechanics.

---

## What Is Pokemon Champions?

Pokemon Champions is a free-to-play competitive battling game developed by The Pokemon Company, released April 8, 2026 on Nintendo Switch and Nintendo Switch 2. Unlike mainline Pokemon games, it has no exploration, catching, or story: the game is 100% focused on competitive battles. A mobile release is planned for 2026.

**Significance:** As of the 2026 season, all official VGC (Video Game Championships) tournaments are played on Pokemon Champions. This makes it the authoritative competitive platform: results from previous seasons on Scarlet/Violet are not directly comparable.

---

## Platform and Access

| Detail | Value |
|--------|-------|
| Platforms | Nintendo Switch, Nintendo Switch 2 (mobile TBD) |
| Release Date | April 8, 2026 |
| Price | Free-to-start |
| Official Site | https://champions.pokemon.com/en-us/ |
| Formats Available | Single Battles, Double Battles |

---

## Monetization (Competitive Integrity Notes)

- **No pay-to-win:** All competitive items (held items, Mega Stones, etc.) are earnable through in-game play
- Cosmetics (trainer outfits, accessories) are available via purchase
- Seasonal battle passes and monthly subscription offer cosmetic rewards only
- Victory Points (VP) are the primary in-game currency; used to unlock Mega Stones and other items

This is relevant for team building: there are no items that require payment to access. All mechanics discussed in team building documents can be assumed accessible to any player.

---

## Roster

- **186 Pokemon available at launch**
- Players can import Pokemon they own via Pokemon HOME (for compatible mainline games)
- Pokemon can also be obtained directly within Champions through in-game progression

**Critical implication for team building:** Not all Pokemon from the full national Pokedex are available. Team building must be scoped to the Champions roster. As the game receives updates, the roster may expand. Always verify a specific Pokemon's availability in Champions before including it in a team plan.

Current roster sources:
- Official announcements: https://champions.pokemon.com/en-us/
- Game8 tier list includes full roster context: https://game8.co/games/Pokemon-Champions/archives/592465
- Pikalytics usage stats implicitly define which Pokemon are appearing on the ladder

---

## Formats

### Single Battles
Standard 1v1 format. Each player sends one Pokemon at a time. Teams of 6, all 6 used (no bring-4 selection).

### Double Battles (Primary VGC Format)
2v2 simultaneous battles. Teams of 6, select 4 to bring, pick 2 leads per game. This is the format used in all official tournaments. For team building focused on competitive play, Doubles should be assumed unless stated otherwise.

See [competitive_pokemon_overview.md](competitive_pokemon_overview.md) for a full explanation of Doubles mechanics.

---

## Mega Evolution in Pokemon Champions

Mega Evolution is a mechanic returning in Pokemon Champions. Selected Pokemon can Mega Evolve during battle using their corresponding Mega Stone.

**How to obtain Mega Stones:**
- Purchased from the in-game shop using Victory Points (VP)
- Example: Dragonitite (Mega Stone for Dragonite) costs 2,000 VP
- VP are earned through completing missions and ranked battles

**Battle mechanics:**
- Each trainer can Mega Evolve one Pokemon per battle
- Mega Evolution occurs at the start of a turn, before move execution
- The Mega-evolved form replaces the base form for the remainder of the battle
- Mega Evolutions typically gain significantly enhanced stats and sometimes a new ability or type

**Key Mega Evolutions available at launch:** Pokemon Champions includes Mega Evolutions from Pokemon Legends: Z-A (2025) in addition to classic Gen VI Megas. Mega Dragonite is one of the newly introduced Megas from Legends: Z-A, available in Champions.

---

## Competitive Mechanics

Champions uses the same fundamental battle mechanics as the mainline games:
- Turn-based battle system
- Types, abilities, moves, and items function as in Generation 9 (with any Z-A era additions)
- Speed ties resolved randomly
- Standard priority brackets (e.g., +1 priority for Fake Out, +2 for Extreme Speed when relevant)
- Full damage formula and stat calculation apply (see damage calc resources in the bibliography)

**Format-specific rules for official play:**
- Level 50 cap (all Pokemon adjusted to Level 50 for battle regardless of actual level)
- Species Clause: no duplicate Pokemon per team
- Item Clause: no duplicate items per team
- Specific banned moves or abilities may be defined per season: always check official rules at:
  https://play.pokemon.com/en-us/resources/rules/?category=vgc

---

## How to Track the Pokemon Champions Meta

Unlike Scarlet/Violet where Showdown usage stats were the primary source, Pokemon Champions has its own dedicated meta tracking tools:

### Primary Sources (in recommended order)
1. **Pikalytics Champions**: https://www.pikalytics.com/champions
   - Real-time usage statistics from the Champions ranked ladder
   - Per-Pokemon: usage %, common moves, items, abilities, teammates
   - Most up-to-date quantitative meta picture

2. **ChampionsLab**: https://championslab.xyz/meta
   - Community meta analysis and team database
   - Tier assessments and meta narrative

3. **Game8 Pokemon Champions**: https://game8.co/games/Pokemon-Champions
   - Individual Pokemon guides with recommended EV spreads and movesets
   - Best team recommendations updated by professional game guide editors
   - Tier list: https://game8.co/games/Pokemon-Champions/archives/592465

4. **Victory Road**: https://victoryroad.pro/
   - Tournament team sheets from regional and national events
   - Most reliable source for what's actually winning official tournaments

5. **StrataDex**: https://stratadex.net/tierlist
   - Community tier list for quick viability checks

### Automated Snapshot Tool
The `tools/fetch_meta_stats.py` script in this repository can snapshot current Pikalytics data to `docs/snapshots/` for offline reference.

---

## Differences From Previous VGC Seasons (Scarlet/Violet)

Players familiar with Gen 9 VGC (Scarlet/Violet) should note the following key differences:

| Aspect | Scarlet/Violet VGC | Pokemon Champions |
|--------|---------------------|-------------------|
| Platform | Nintendo Switch mainline games | Dedicated battle-only app |
| Roster | Full Paldea + HOME transfers | 186 Pokemon (curated) |
| Mega Evolution | Not available (Tera mechanic instead) | Available; Mega Stones purchasable |
| Terastallization | Core mechanic | Not available |
| Official tournament platform | Yes (until 2026) | Yes (from 2026 onward) |

**The most significant mechanic shift:** Terastallization (the defining mechanic of S/V) is replaced by Mega Evolution as the primary battle transformation mechanic. This fundamentally changes team building philosophy:

- **Tera** allowed any Pokemon to change type once per battle: enabling defensive pivots or STAB coverage changes mid-game
- **Mega Evolution** permanently transforms one Pokemon into a pre-defined enhanced form for the rest of the battle: the choice of which Pokemon to Mega is strategic but the outcome (typing, stats, ability) is predictable and known to the opponent

Teams built around abusing Tera should be completely reconceived. Teams built around a strong Mega user have a more fixed but potentially more powerful transformation available.

---

## Item and Move Availability -- Critical Constraint

Pokemon Champions launched with a **curated, limited item and move pool** that differs from mainline games. Do not assume items or moves available in Scarlet/Violet or other games are legal in Champions. This is one of the most common sources of error when building teams.

### Confirmed Unavailable Items (at launch)

| Item | Notes |
|------|-------|
| Assault Vest | Very common in mainline VGC; not in Champions |
| Life Orb | Not available |
| Choice Band | Not available |
| Choice Specs | Not available |
| Heavy-Duty Boots | Not available |
| Eviolite | Not available |

### Confirmed Available Items (at launch)

Choice Scarf, Focus Sash, Rocky Helmet, Damp Rock, Sitrus Berry, Lum Berry, Cheri Berry, type-resist berries (Roseli, Occa, etc.), Weakness Policy, Booster Energy, Throat Spray, Safety Goggles, Loaded Dice, Scope Lens, Terrain Extender, Utility Umbrella, Charcoal and other type-boosting held items, Black Sludge, Mental Herb, Protective Pads.

**Item pool is expected to expand via live service updates.** Always verify before finalizing a team.

**Source:** [Game8 full items list](https://game8.co/games/Pokemon-Champions/archives/588871)

### Move Availability Per Pokemon

Champions uses a curated learnset per Pokemon: moves are selected from a defined list rather than inherited from mainline games. **Moves available in Scarlet/Violet may not be in a Pokemon's Champions learnset.**

Notable example: Incineroar cannot learn Knock Off in Champions despite the move existing in the game for other Pokemon.

**Rule for Claude agents:** When writing a team build set for any Pokemon, verify the moveset against a Champions-specific source:

- Game8 individual Pokemon guides: `https://game8.co/games/Pokemon-Champions/archives/<id>`
- Pikalytics per-Pokemon usage page: `https://www.pikalytics.com/pokedex/championstournaments/<name>`

Do not copy movesets from Smogon analyses or Scarlet/Violet VGC references without verification.

---

## Team Building Workflow for Pokemon Champions

1. **Verify the target format**: Singles or Doubles? Current season's restricted Pokemon list?
2. **Check current Pikalytics Champions usage**: What are the top 20 Pokemon appearing? What are common archetypes?
3. **Identify a win condition**: Which Pokemon will be your primary threat? (e.g., Mega Dragonite as a Doubles wallbreaker/sweeper)
4. **Check Game8 guide** for that Pokemon's recommended sets in the Champions meta specifically: do not use Smogon or S/V sets without verifying Champions availability
5. **Verify every item and move** against Champions-specific sources before writing a build document
6. **Build support structure** around the win condition: speed control, redirection, hazard setting (if Singles), type coverage
7. **Cross-reference Victory Road** for similar team compositions that have placed well in events
8. **Document the team** in `docs/teams/` with full details for future reference

---

## Research Session Documentation

Each time meta research is conducted, save a snapshot to `docs/snapshots/` using the fetch script, and consider saving a session summary to `docs/` as a new annotated bibliography entry. This builds an archive of how the meta evolved over time: useful for understanding trends and revisiting past decisions.
