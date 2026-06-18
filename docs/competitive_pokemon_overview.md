# Competitive Pokemon — Reference Overview

**Audience:** Claude agents operating in this repository. This document provides foundational context on competitive Pokemon battling to enable informed team building assistance.

---

## Core Mechanics

### Stats
Every Pokemon has six base stats: HP, Attack, Defense, Special Attack, Special Defense, and Speed. In battle, these base stats are modified by:

- **IVs (Individual Values):** Hidden values from 0–31 per stat, set when a Pokemon is obtained. Competitive Pokemon target 31 IVs in all stats (or 0 in certain cases, e.g., 0 Speed for Trick Room teams).
- **EVs (Effort Values):** Trained values up to 252 per stat and 510 total. Competitive spreads almost always max two stats (252/252) with 4 leftover, though custom spreads are used to hit specific speed benchmarks or survive certain damage calculations.
- **Natures:** Each nature multiplies one stat by 1.1x and another by 0.9x (neutral natures have no effect). Natures are chosen to amplify the Pokemon's primary role.
- **Level:** Competitive formats almost universally use Level 50 (VGC/official) or Level 100 (Smogon). This matters for stat calculations.

### Types
There are 18 types. Type matchups determine damage multipliers:
- **Super effective (2x):** Attacker's type is strong against defender's type
- **Resisted (0.5x):** Attacker's type is weak against defender's type
- **Immune (0x):** Defender is immune (e.g., Ghost is immune to Normal/Fighting)
- Dual-typed Pokemon apply both multipliers (can result in 4x weakness or 4x resistance)

Understanding type matchups is the foundation of every defensive and offensive decision.

### Abilities
Each Pokemon has 1–3 possible abilities (1 active at a time). Abilities passively modify battle behavior — they can boost damage, alter type matchups, activate effects on switch-in, or fundamentally change how a Pokemon functions. Examples:
- **Multiscale** (Dragonite): Halves damage taken while at full HP — transforms Dragonite from a pokemon that fears being one-shotted to a reliable setup sweeper or wallbreaker
- **Intimidate**: Lowers opponent's Attack by 1 stage on switch-in — premier support ability in Doubles
- **Levitate**: Makes the user immune to Ground moves — changes defensive type coverage entirely

### Items
Each Pokemon holds one item. Items are central to competitive team building.

**Item Clause:** In all official competitive formats (VGC, Pokemon Champions), no two Pokemon on the same team may hold the same item. This is a hard rule enforced in every official battle. Always verify the full team's item list before finalizing — a team summary table listing all 6 Pokemon with their items is the recommended way to catch violations early.
- **Choice items** (Choice Band/Specs/Scarf): Lock the user into one move but boost Attack, Sp. Atk, or Speed by 1.5x respectively
- **Leftovers/Black Sludge**: Passive HP recovery each turn — enables defensive longevity
- **Life Orb**: 1.3x damage boost at the cost of 10% HP per attacking move
- **Mega Stones**: Trigger Mega Evolution when held; Pokemon Champions uses Victory Points to purchase these
- **Focus Sash**: Survive any single hit at 1 HP (if starting at full HP) — guarantees a revenge KO or hazard set
- **Eviolite**: Doubles Defense and Sp. Def of unevolved Pokemon — makes some NFEs bulkier than their evolutions

---

## Battle Formats

### Singles vs. Doubles
**Singles** (Smogon formats): 1v1 at a time, 6-Pokemon teams, each player sends 1 Pokemon. The primary format for Smogon competitive play and Pokemon Showdown laddering.

**Doubles (VGC/Pokemon Champions)**: 2v2 at a time, 6-Pokemon teams, each player sends 2 Pokemon per turn. The official competitive format used in VGC and Pokemon Champions. Doubles introduces:
- Spread moves (Earthquake, Surf, Heat Wave) that hit both opposing Pokemon simultaneously
- Support moves (Helping Hand, Tailwind, Follow Me) that have no place in Singles
- Positioning: field effects, terrain, and weather interact with both your Pokemon and both opponents simultaneously
- Turn order becomes more complex (4 Pokemon acting per turn, each at their own Speed)

**Team preview:** In official formats, both players see all 6 opposing Pokemon before selecting which 4 to bring. This makes team building more complex — your team must be able to handle a wide variety of leads and back-team compositions, not just a single opponent.

### Singles Tier System (Smogon)
Smogon tiers determine which Pokemon are legal in each format based on usage statistics compiled monthly from Pokemon Showdown ladder data:

| Tier | Description |
|------|-------------|
| **Ubers** | Banned from standard OU — too powerful for balanced play. Includes most legendaries. |
| **OU (OverUsed)** | Standard competitive tier. Pokemon used in >4.52% of high-ladder games. |
| **UU (UnderUsed)** | Pokemon too weak for OU but strong enough to dominate lower tiers. |
| **RU (RarelyUsed)** | Next tier below UU. |
| **NU (NeverUsed)** | Pokemon rarely used even in lower tiers. |
| **PU** | The lowest usage tier. |
| **Anything Goes (AG)** | No restrictions — Ubers, Z-moves, megas, everything. |

Smogon tiers are relevant for Pokemon Showdown practice and for understanding the relative power level of different Pokemon, but they do not directly map to Pokemon Champions legality.

### VGC Format Rules (Official)
VGC uses a distinct ruleset from Smogon:
- **4-of-6:** Teams of 6, bring 4 to each game, select 2 leads and keep 2 back
- **Level 50:** All Pokemon set to Level 50 for the battle
- **Species clause:** No duplicate Pokemon on a team
- **Item clause:** No duplicate items on a team
- **Restricted Pokemon:** Each season defines which legendary/mythical Pokemon are legal, and often limits how many "restricted" Pokemon can appear on a single team
- **Banned moves/abilities:** Certain mechanics (Swagger + flinch loops, one-hit KO moves, some abilities) are banned

As of 2026, Pokemon Champions is the official platform for all VGC events.

---

## Team Building Concepts

### Win Condition
The core question of team building: how does this team actually win games? Common win conditions:
- **Offensive sweeper:** Set up (Dragon Dance, Swords Dance, Nasty Plot), then sweep with boosted stats
- **Wallbreaker:** Hit too hard for the opponent to sustain — wear down defensive cores without needing setup
- **Stall:** Win via attrition — entry hazards, status, recovery, and chip damage outlast the opponent's team
- **Trick Room:** Reverse Speed priority for 5 turns; your "slow" Pokemon now moves first
- **Weather/Terrain teams:** Leverage Rain, Sun, Sand, or Hail for passive damage, Speed boosts, or move power boosts

### Team Cores
A core is two or more Pokemon that synergize to handle each other's weaknesses. Classic example: a Dragon/Fire core, where the Fire type handles Ice/Steel moves that Dragon fears, and the Dragon type handles Water moves that Fire fears. Identifying your primary core and its common checks is the first step in team building around any particular Pokemon.

### Speed Tiers
Speed determines turn order in battle. The competitive meta is organized around speed tiers — the Speed stat values at which Pokemon naturally outspeed or are outsped by key threats. Common benchmarks in Generation 9 formats include 100 Speed (base Dragonite), 110 (many Fast Pokemon), 120 (Weavile), 130 (Regieleki), etc. Setting EVs to hit or exceed a specific speed tier is a key optimization decision.

Speed can be modified by:
- **Priority moves** (Extreme Speed, Sucker Punch, Fake Out): Act before normal moves regardless of Speed
- **Choice Scarf:** 1.5x Speed — allows slower Pokemon to outspeed fast threats
- **Tailwind (Doubles):** Doubles team Speed for 4 turns — enables otherwise too-slow teams
- **Trick Room (Doubles):** Reverses Speed priority — enables "slow" bulky Pokemon to move first

### Role Compression
In a 6-Pokemon team, each slot must justify itself. Role compression means choosing a Pokemon that fills multiple roles simultaneously — a Pokemon that is both a speed control setter AND a physical attacker, for example. Leaning too hard on hyper-specialized Pokemon can leave the team vulnerable to specific threats it has no answer for.

### Entry Hazards (Singles)
Hazards are less central in Doubles/VGC but are important in Singles formats:
- **Stealth Rock:** Rock-type damage based on type effectiveness when opponent's Pokemon switches in (12.5% to 25% to 50% depending on type)
- **Spikes:** Ground-level damage on opposing Pokemon (no effect on Levitate/Flying types)
- **Toxic Spikes:** Poisons switching-in grounded Pokemon

### Status Conditions
- **Burn:** Halves physical Attack; causes 1/16 HP loss per turn
- **Paralysis:** 25% chance of moving; halves Speed
- **Poison/Toxic:** HP loss per turn (accelerating for Toxic)
- **Sleep:** Cannot move (limited to 1–3 turns by modern sleep mechanics)
- **Freeze:** Cannot move (less common in recent games)

---

## Research Tools

### Damage Calculator
Smogon's damage calculator (calc.pokemonshowdown.com) and similar tools allow precise calculation of whether a Pokemon can survive a specific attack or KO a specific defender at given EV spreads. Evaluating matchup safety with the damage calc before finalizing a team is standard practice.

### Usage Statistics
Pokemon Showdown publishes monthly usage statistics at smogon.com/stats. These stats show which Pokemon appear most often at high ladder ranks, along with their most common moves, items, abilities, and teammates. For Pokemon Champions, Pikalytics (pikalytics.com/champions) is the equivalent resource.

### Pokemon Showdown as Practice Environment
Running teams on Pokemon Showdown before investing in a final build is standard. Showdown allows instant team deployment without any grinding. Replays can be saved and analyzed. Showdown laddering is considered the standard way to test a team's viability before tournament play.

---

## Key Distinctions Between Formats

| Attribute | Smogon Singles (OU) | VGC / Pokemon Champions |
|-----------|---------------------|-------------------------|
| Simultaneous Pokemon | 1v1 | 2v2 |
| Team size | 6 (bring all 6) | 6 (bring 4) |
| Level | 100 | 50 |
| Hazards | Central | Rarely used |
| Speed control | Primarily Scarf/priority | Tailwind, Trick Room, Scarf |
| Support moves | Minor role | Critical (Follow Me, Helping Hand, etc.) |
| Weather/terrain | Important | Very Important |
| Legendaries | Mostly banned | Often allowed (by season rules) |
| Platform | Pokemon Showdown | Pokemon Champions (official) |

---

## Recommended Learning Sequence for an Agent

1. Identify the format being targeted (Singles vs. Doubles, which season ruleset)
2. Check current usage stats via Pikalytics (Champions) or Showdown stats (Smogon)
3. Identify top-tier threats the team must answer
4. Build around the intended win condition or core Pokemon
5. Fill remaining slots to cover type/speed/role weaknesses
6. Verify spreads with damage calculator for key matchups
7. Test on Showdown (Singles) or Pokemon Champions (Doubles/VGC)
