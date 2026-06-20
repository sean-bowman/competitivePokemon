# Team Seed: Mega Dragonite -- Pokemon Champions

**Format:** Pokemon Champions: Double Battles (VGC)
**Status:** SEED: initial research document, not a finalized team
**Created:** 2026-04-14  
**Win Condition:** Mega Dragonite as the primary offensive threat; team built to enable and protect its setup/sweep

---

## Core Pokemon: Mega Dragonite

### Base Profile
| Stat | Base (Normal) | Base (Mega) |
|------|---------------|-------------|
| HP | 91 | 91 |
| Attack | 134 | 124 |
| Defense | 95 | 115 |
| Sp. Atk | 100 | 145 |
| Sp. Def | 100 | 125 |
| Speed | 80 | 100 |
| **BST** | **600** | **700** |

**Type:** Dragon / Flying (unchanged on Mega Evolution)  
**Ability (Mega):** Multiscale: damage taken is halved when Dragonite is at full HP

> Note: The Mega form shifts the damage focus from physical (134 Atk) to special (145 SpAtk), and the bulk gains (+20 Def, +25 SpDef, +20 Speed) are substantial. The Mega is clearly intended as a specially offensive tank/sweeper.

### How to Obtain Mega Stone
Purchase the Dragonitite from the in-game shop for 2,000 Victory Points.

---

## Role Assessment

**Primary role:** Specially offensive wallbreaker / late-game sweeper  
**Secondary role:** Bulk pivot with Multiscale (survives hits that would faint standard attackers)

### Why Mega Dragonite?
- 145 Special Attack is elite-tier offense; Dragon/Flying STAB hits a large swath of the meta for neutral or better
- Multiscale makes Dragonite very difficult to KO in a single hit when healthy: it can survive a super effective Ice-type attack at full HP (normally 4x weakness)
- 100 Speed is a useful benchmark in Doubles: not the fastest, but with Tailwind support it becomes extremely threatening
- 700 BST places it among the strongest non-legendary Pokemon available in the game

### Primary Weaknesses (Type)
| Type | Multiplier | Notes |
|------|-----------|-------|
| Ice | 4x (2x mitigated by Multiscale at full HP → effectively 2x) | Still the most dangerous threat; priority ice moves (if any exist in format) bypass Multiscale |
| Rock | 4x | Stealth Rock, Rock Slide: dangerous in Singles; less common in Doubles |
| Dragon | 2x | Opposing Dragon types; Fairy types immune to Dragon and KO back |
| Fairy | 2x | Fairy resists/is immune to Dragon; Moonblast/Dazzling Gleam are common |

**Note on Multiscale:** It only functions when Dragonite is at 100% HP. Chip damage (e.g., from Fake Out, Protect turns with Poison/Burn, or entry hazards in Singles) removes Multiscale entirely. Keeping Dragonite healthy is a team-wide priority.

---

## Moveset Options

### STAB (Dragon/Flying)
| Move | Type | Cat | Power | Notes |
|------|------|-----|-------|-------|
| Draco Meteor | Dragon | Sp | 130 | -2 SpAtk drop; use once then pivot out |
| Dragon Pulse | Dragon | Sp | 85 | No drawback; primary sustained STAB |
| Hurricane | Flying | Sp | 110 | 70% accuracy in normal weather; 100% in Rain |
| Air Slash | Flying | Sp | 75 | Higher accuracy; 30% flinch rate |

### Coverage
| Move | Type | Cat | Power | Notes |
|------|------|-----|-------|-------|
| Thunderbolt | Electric | Sp | 90 | Covers opposing Water and Flying types |
| Ice Beam | Ice | Sp | 90 | Coverage; hits Fairy and Grass types not covered by Dragon |
| Surf | Water | Sp | 90 | Doubles-friendly spread move; also covers Rock/Fire |
| Fire Blast | Fire | Sp | 110 | Covers Steel types that resist Dragon/Flying |
| Focus Blast | Fighting | Sp | 120 | Covers Steel, Rock, Ice, Dark: important defensive counters |

### Support / Utility
| Move | Type | Notes |
|------|------|-------|
| Roost | Flying | Restores 50% HP; restores Multiscale: can be slow in Doubles but viable in Singles |
| Extreme Speed | Normal | Physical priority +2; useful for cleaning weakened targets |
| Dragon Dance | Dragon | +1 Atk/Spe per use; less valuable on the specially-oriented Mega form |

### Recommended Starting Sets (Pending Meta Research)

**Doubles Set A: Bulky Wallbreaker**
```
Mega Dragonite @ Dragonitite
Ability: Multiscale
EVs: TBD (likely 252 SpAtk / 4 Def or SpDef / 252 Speed, or modified for specific bulk benchmarks)
Nature: Modest or Timid
- Draco Meteor
- Hurricane
- Thunderbolt or Fire Blast
- Protect
```

**Doubles Set B: Rain Abuse**
```
Mega Dragonite @ Dragonitite
Ability: Multiscale
EVs: 252 SpAtk / 4 SpDef / 252 Speed
Nature: Timid
- Hurricane  (100% accuracy in Rain)
- Surf       (spread damage; synergy with Rain)
- Draco Meteor
- Protect
```

> **TODO:** Pull actual EV spread recommendations from Game8 guide after live data access. These sets are starting templates.

---

## Live Meta Snapshot -- 2026-04-14

Data from `tools/fetch_meta_stats.py` (source: pikalytics.com/champions). Full JSON at `docs/snapshots/meta_stats_2026-04-14.json`.

| Rank | Pokemon | Usage | Role Label | Notes for Dragonite team |
|------|---------|-------|-----------|--------------------------|
| #1 | Incineroar | 54.4% | Tempo king | Intimidate + Fake Out support: natural Dragonite partner |
| #2 | Sneasler | 45.1% | Fast disruption | Fast physical attacker; Unburden/Speed boost; check with bulk |
| #3 | Garchomp | 37.1% | Ground pressure | Competing Dragon; 102 base Speed: beats Dragonite in straight race; partner with Fairy check |
| #4 | Sinistcha | 34.6% | Redirection glue | Ghost/Grass; Rage Powder redirector: could be Dragonite's bodyguard |
| #5 | Kingambit | 27.0% | Late-game cleaner | Dark/Steel; Supreme Overlord; physical sweeper: Steel resists Fairy for our team |
| #6 | Basculegion | 22.1% | Rain payoff | Ghost/Water; confirms Rain teams are prevalent: Hurricane 100% accuracy opportunity |
| #7 | Whimsicott | 20.1% | Speed control | Fairy/Grass, Prankster Tailwind: opponent's Whimsicott threatens with Moonblast; our own Whimsicott sets Tailwind |
| #8 | Charizard | 17.8% | Mega pressure | Mega Charizard (likely Y for Sun, X for physical): common Mega slot; confirms Megas are relevant |
| #9 | Floette | 17.8% | Special tech | Fairy type with special coverage: immune to Dragonite's Dragon STAB, dangerous if packing Moonblast |
| #10 | Rotom-Wash | 16.0% | Pivot utility | Electric/Water; WiLL-O-WISP and pivoting; Levitate; not a hard counter to Dragonite |
| #11 | Pelipper | 16.0% | Weather setter | Drizzle; confirms Rain teams viable: Rain enables Hurricane 100% accuracy |
| #12 | Tyranitar | 15.4% | Sand breaker | Rock/Dark; Sand Stream; Rock Slide in doubles: major Dragonite threat (4x Rock weakness) |

### Key Meta Reads

**Rain teams are prominent** (Pelipper #11, Basculegion #6). This is direct synergy for Mega Dragonite: Hurricane + Surf under Rain is a compelling combination. Consider building a Rain team with Dragonite as the offensive anchor.

**Incineroar is nearly mandatory** at 54.4% usage. Likely on every top team. It provides:
- Intimidate (-1 Atk on switch): protects Dragonite from physical hits
- Fake Out: free first-turn flinch, lets Dragonite set up or Protect safely
- Parting Shot: further chip to protect teammates

**Tailwind is available via Whimsicott** (#7). Prankster Tailwind (priority +1) sets speed control before opponents can respond. Whimsicott also learns Encore to lock opponents into non-threatening moves.

**Sinistcha is already the community's preferred redirector** (#4). Using Sinistcha as a Rage Powder partner shields Dragonite from targeted Ice/Rock moves.

**Tyranitar (#12) with Rock Slide is a significant threat.** Rock Slide is a common spread move in Doubles. Dragonite's 4x Rock weakness and Tyranitar's Sand Stream (which cancels Multiscale via chip?) makes this matchup dangerous. Need either a Redirect or a Fairy partner that forces Tyranitar out.

---

## Team Skeleton

6 slots total; bring 4 per game. Updated with meta-informed candidates.

### Slot 1: Mega Dragonite (Core -- filled)

### Slot 2: Support / Fake Out + Intimidate
**Role:** Enable Dragonite's safe Mega Evolution and first attack by flinching or intimidating the opponent  
**Top candidate:** **Incineroar**: 54.4% usage confirms it belongs on almost every team. Fake Out flinch + Intimidate is the premier enabler for fragile sweepers like Dragonite.
**Incineroar's key moves:** Fake Out, Parting Shot, Flare Blitz / Darkest Lariat, Knock Off

### Slot 3: Speed Control
**Role:** Double Dragonite's effective Speed via Tailwind, or set Rain for Hurricane accuracy  
**Top candidates:**
- **Whimsicott**: Prankster Tailwind (priority +1 means it almost always goes first); also Fairy type which covers Dragon weakness on the team; Moonblast coverage
- **Pelipper**: Drizzle Rain setter; pairs with Hurricane + Surf on Dragonite; also provides Tailwind

These two are not mutually exclusive: can run both for coverage or choose based on team archetype (Sun/sand vs. Rain vs. pure speed control).

### Slot 4: Redirection
**Role:** Redirect single-target Ice/Rock/Fairy moves away from Dragonite via Rage Powder or Follow Me  
**Top candidate:** **Sinistcha**: already #4 in meta usage as "Redirection glue"; Ghost/Grass typing means it is immune to Normal and Fighting; Rage Powder redirects most threats; Matcha Gotcha for recovery

### Slot 5: Steel-type Anchor / Fairy Check
**Role:** Resist Fairy and Dragon moves; handle Whimsicott/Floette threats from opponents  
**Top candidates:**
- **Kingambit**: #5 in meta; Dark/Steel; Supreme Overlord boosts as teammates faint; Sucker Punch priority; resists Dragon and Fairy; powerful late-game cleaner that complements Dragonite's opening pressure
- Steel/Fire type: resists Fairy, Dragon, Ice; covers Tyranitar (Rock) if it has Fire coverage

### Slot 6: Flexible / Coverage
**Role:** Address remaining matchup gaps after drafting slots 1–5  
**Options:** Garchomp (Ground pressure, speed), a second weather setter, a terrain setter

---

## Draft Team A: Rain Offense

```
1. Mega Dragonite @ Dragonitite: Hurricane / Surf / Draco Meteor / Protect
2. Incineroar @ Assault Vest: Fake Out / Parting Shot / Flare Blitz / Knock Off
3. Pelipper @ Damp Rock: Rain Dance / Hurricane / Scald / Tailwind
4. Sinistcha @ Rocky Helmet: Rage Powder / Matcha Gotcha / Shadow Ball / Protect
5. Kingambit @ Life Orb: Kowtow Cleave / Sucker Punch / Iron Head / Protect
6. TBD (Rotom-W? Garchomp?)
```

**Win condition:** Pelipper sets Rain → Dragonite Hurricane hits 100% and nukes threats → Sinistcha redirects incoming Ice → Incineroar cleans up with Fake Out / Parting Shot → Kingambit closes games after rain expires.

---

## Threat Analysis (Updated with Meta Data)

| Threat | Pokemon | Why Dangerous | Answer |
|--------|---------|---------------|--------|
| Rock Slide spread | Tyranitar (#12) | 4x Rock weakness; Sand Stream cancels Rain; spread hits both Pokemon | Sinistcha redirect (immune to Normal, doesn't redirect Rock: need to check) or avoid sending Dragonite vs Tyranitar |
| Fairy STAB | Whimsicott (#7), Floette (#9) | Dragon immunity; Moonblast hits Dragonite for 2x | Kingambit (resists Fairy); Incineroar (Steel if needed) |
| Fast physical sweeper | Sneasler (#2) | Extremely fast; Unburden speed; physical damage bypasses Multiscale chip | Incineroar Intimidate; Sinistcha redirect if single-target move |
| Competing Dragon | Garchomp (#3) | 102 base Speed (faster than base Dragonite); STAB Dragon hits hard | Outspeed under Tailwind; Kingambit's Fairy-immune Sucker Punch |
| Sand + Rock | Tyranitar (#12) | Sand chip removes Multiscale; Rock Slide on top is lethal | Do not bring Dragonite into Tyranitar without Sinistcha redirect buffer |

---

## Research TODOs

- [x] Run `tools/fetch_meta_stats.py`: done; top-12 captured in snapshot above
- [ ] Read Game8 Mega Dragonite guide for recommended EV spread: https://game8.co/games/Pokemon-Champions/archives/592442
- [ ] Verify Sinistcha can redirect Rock Slide (Rage Powder typically redirects most moves; confirm Rock Slide is not an exception)
- [ ] Determine Mega Charizard X vs Y prevalence: affects whether Fire coverage is needed
- [ ] Check Kingambit's specific moveset in Champions (does Supreme Overlord trigger from fainted teammates only on the same team, or all allies ever fainted?)
- [ ] Verify Pelipper's Rain vs Whimsicott's Tailwind: which archetype is more consistent at current meta stage
- [ ] Evaluate Rotom-W (#10) as Slot 6: pivot + Will-O-Wisp vs. a second offensive mon

---

## Session Log

| Date | Update |
|------|--------|
| 2026-04-14 | Seed document created. Mega Dragonite stats confirmed (91/124/115/145/125/100, Multiscale, Dragon/Flying). Team skeleton drafted. Threat analysis preliminary: pending live meta data. |
