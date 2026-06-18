# Build: Mega Dragonite Rain Offense — v1

**Format:** Pokemon Champions — Double Battles (VGC)
**Status:** BUILD — active development document
**Created:** 2026-04-14
**Seed Reference:** [../seeds/mega_dragonite_seed.md](../seeds/mega_dragonite_seed.md)
**Win Condition:** Whimsicott Prankster Tailwind + Pelipper Drizzle (Rain) set up on turn 1 → Mega Dragonite Hurricane (100% accuracy, fast) + Archaludon Electro Shot (instant in Rain) fire simultaneously → Incineroar Fake Out enables safe Mega Evo → Basculegion closes late game

---

## Team Philosophy

This team is built around a **Rain double-attacker core**: Mega Dragonite and Archaludon both require Rain to reach their full potential, and that's the design constraint every slot is evaluated against.

**What Rain does for this team:**

- Hurricane: 70% → 100% accuracy, 110 BP STAB off 145 SpAtk
- Electro Shot: skips charge turn entirely in Rain, fires at 130 BP immediately
- Surf: spread Water damage boosted x1.5
- Basculegion Wave Crash: Water boosted x1.5

**Core (4 slots — almost always brought):**

1. Mega Dragonite — primary attacker, win condition
2. Pelipper — Rain setter; Tailwind offloaded to Whimsicott
3. Archaludon — secondary Rain attacker, Steel/Dragon covers Dragonite's counters (Ice x0.25, Fairy x0.5, Dragon x0.5)
4. Incineroar — Fake Out enables Mega Evo on turn 1; Intimidate + Parting Shot pivot

**Flex (2 slots — chosen at team preview based on opponent):**

5. Whimsicott — near-core; Prankster Tailwind guaranteed T1 regardless of Speed; Encore answers Trick Room at +1 priority
6. Basculegion — brought when late-game attrition favors the team; Last Respects scales with fainted teammates; Wave Crash boosted in Rain

**Why Kingambit was cut:** Kingambit pairs with Sneasler at 60% in usage data — it belongs to Sneasler offense teams, not Rain teams. Its Defiant + Sucker Punch value is generically strong but has no Rain synergy. A flex slot on a Rain team should either directly abuse Rain or patch a specific matchup gap. Basculegion does both; Kingambit does neither.

**Speed control — Whimsicott (Prankster):** Pelipper's dual role as Rain setter AND Tailwind user was a structural bottleneck — at 65 base Speed it frequently moved last, failing to get Tailwind up. Whimsicott (Prankster) solves this cleanly:

- **Prankster Tailwind** (+1 priority) fires before any non-priority move regardless of Speed — Tailwind is guaranteed T1
- **Prankster Encore** locks Trick Room setters into repeating TR (toggling it off) at +1 priority
- Pelipper is freed from Tailwind duty and now runs Protect, surviving longer to keep Rain active

Whimsicott is near-core: Tailwind and Encore are useful in almost every game.

---

## Team Summary

> Item Clause: no duplicate items permitted per team. See [competitive_pokemon_overview.md](../../competitive_pokemon_overview.md).

| # | Role | Pokemon | Item | Ability | Move 1 | Move 2 | Move 3 | Move 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Rain attacker (core) | Mega Dragonite | Dragonitite | Multiscale | Hurricane | Surf | Draco Meteor | Protect |
| 2 | Rain setter (core) | Pelipper | Focus Sash | Drizzle | Hurricane | Weather Ball | Protect | Wide Guard |
| 3 | Rain attacker 2 (core) | Archaludon | Leftovers | Stamina | Electro Shot | Flash Cannon | Draco Meteor | Protect |
| 4 | Enabler (core) | Incineroar | Chople Berry | Intimidate | Fake Out | Parting Shot | Flare Blitz | Throat Chop |
| 5 | Speed control / TR disruption (near-core) | Whimsicott | Mental Herb | Prankster | Tailwind | Moonblast | Encore | Protect |
| 6 | Flex B — late game | Basculegion | Choice Scarf | Adaptability | Last Respects | Wave Crash | Aqua Jet | Flip Turn |

**Item clause check:** Dragonitite / Focus Sash / Leftovers / Chople Berry / Mental Herb / Choice Scarf — all unique.

---

## Core Roster

### 1. Mega Dragonite @ Dragonitite

```text
Ability: Multiscale -> Multiscale (Mega)
Type: Dragon / Flying
EVs: 252 SpAtk / 252 HP / 4 SpDef
Nature: Modest
- Hurricane
- Surf
- Draco Meteor
- Protect
```

**Verified usage (Pikalytics 2026-04-14):** Hurricane 52% · Draco Meteor 43% · Protect 81% · Extreme Speed 39% · Tailwind 34% · Thunder 18% | Item: Mega Stone 65% · Lum Berry 14% | Ability: Multiscale 72% · Inner Focus 28%

**Note on usage percentages:** The Hurricane 52% figure covers all Dragonite builds, not just Mega Rain. Many Dragonite run physical sets (Extreme Speed + Scale Shot) or Tailwind support. The Rain Hurricane variant is a niche but viable archetype.

**Role:** Primary offensive threat and Mega slot. Hurricane at 100% accuracy in Rain is the main damage dealer — 110 BP with STAB off 145 SpAtk. Surf provides spread Water damage boosted x1.5 in Rain, covering Rock/Fire/Ground types and hitting both opponents. Draco Meteor is the nuke for targets that resist Flying. Protect enables safe Mega Evolution on turn 1 behind Incineroar's Fake Out.

**EV rationale:** 252 SpAtk + Modest for max damage output. Speed EVs dropped entirely — under Tailwind even 0 Speed EVs results in a doubled stat that outruns all non-Tailwind threats; without Tailwind, Dragonite cannot outspeed Sneasler (110) or Aerodactyl (130) regardless of EVs. 252 HP replaces Speed EVs: HP investment strengthens Multiscale (first hit is halved off a larger HP pool) and improves survivability when Multiscale is broken. **TODO:** Benchmark 252 HP vs specific attacks (Tyranitar Rock Slide, Sneasler Close Combat) to verify survival thresholds.

**Multiscale management:** Get Dragonite in at full HP whenever possible. Default lead (Incineroar Fake Out + Dragonite Protect) buys a free turn. Multiscale restoration via Hospitality is no longer available (Sinistcha removed) — preserve HP through positioning rather than relying on a recovery mechanic.

---

### 2. Pelipper @ Focus Sash

```text
Ability: Drizzle
Type: Water / Flying
EVs: 248 HP / 8 Def / 252 SpAtk
Nature: Modest
- Hurricane
- Weather Ball
- Protect
- Wide Guard
```

**Verified usage (Pikalytics 2026-04-14):** Hurricane 97% · Weather Ball 87% · Tailwind 77% · Protect 65% · Wide Guard 33% · Muddy Water 12% | Item: Focus Sash 75% · Choice Scarf 9% | Ability: Drizzle 99%

**Role:** Pure Rain setter and secondary attacker. Drizzle sets Rain on switch-in with no turn cost. Focus Sash at 75% guarantees Rain is set even if Pelipper is targeted. Weather Ball in Rain is 150 effective power Water STAB. Wide Guard blocks spread moves (Tyranitar Rock Slide, Garchomp Earthquake) for the whole team.

**Tailwind removed from Pelipper:** Whimsicott handles Tailwind via Prankster (+1 priority). Pelipper previously had to burn a slow move action on Tailwind — often failing because it moves last at 65 base Speed. Protect replaces Tailwind, letting Pelipper survive an extra turn to keep Rain active and re-enter for Rain resets.

**Re-entry:** Rain expires after 5 turns (Focus Sash, not Damp Rock). Incineroar's Parting Shot is the primary way to pivot Pelipper back in for a full 5-turn Rain reset.

---

### 3. Archaludon @ Leftovers

```text
Ability: Stamina
Type: Steel / Dragon
EVs: 252 HP / 4 SpAtk / 252 SpDef
Nature: Calm
- Electro Shot
- Flash Cannon
- Draco Meteor
- Protect
```

**Verified usage (Pikalytics 2026-04-14):** Electro Shot 96% · Flash Cannon 90% · Protect 73% · Draco Meteor 58% · Dragon Pulse 32% · Aura Sphere 23% | Item: Leftovers 50% · Magnet 15% · White Herb 11% | Ability: Stamina 74% · Sturdy 22%

**Teammate data (Pikalytics 2026-04-14):** Pelipper 72% · Basculegion 60% · Incineroar 52% · Sinistcha 42% · Dragonite 37%

**Role:** Secondary Rain attacker and Dragonite's defensive partner. Archaludon pairs with Pelipper at 72% — the highest single-pair rate in the Rain team archetype. This is the meta-confirmed Rain partner.

**Electro Shot in Rain:** The charge turn is skipped entirely — Archaludon fires a 130 BP Special Electric move on turn 1 with no setup. Combined with Dragonite's Hurricane, both attackers threaten at full power simultaneously from turn 1.

**Typing as Dragonite insurance:** Steel/Dragon resists Ice x0.25, Fairy x0.5, Dragon x0.5 — Dragonite's three primary counters. When Dragonite is threatened by Ice Beam or a Fairy attack, Archaludon can take the hit and respond. Flash Cannon hits Fairy types for 2x. Archaludon does not need to be paired with Dragonite to be useful — it can operate alongside Pelipper, Incineroar, or either flex Pokemon.

**Stamina + Leftovers:** Stamina gives +1 Defense on every hit. Over a game, Archaludon becomes progressively harder to KO through physical damage. Leftovers recovers HP each turn, extending presence. Combined, Archaludon is the team's long-term anchor.

**EV rationale:** Max HP / Max SpDef Calm is a starting point — covers the specially offensive meta (Whimsicott, Floette, opposing Dragonite). Physical bulk is handled by Stamina stacking. TODO: verify against Game8 or Limitless tournament sets.

---

### 4. Incineroar @ Chople Berry

```text
Ability: Intimidate
Type: Fire / Dark
EVs: 252 HP / 4 Atk / 252 SpDef
Nature: Careful
- Fake Out
- Parting Shot
- Flare Blitz
- Throat Chop
```

**Verified usage (Pikalytics 2026-04-14):** Fake Out 99% · Parting Shot 96% · Flare Blitz 85% · Throat Chop 43% · Darkest Lariat 39% | Item: Sitrus Berry 56% · Chople Berry 15% | Ability: Intimidate 98%

**Role:** Enabler for the entire core. Turn 1: Fake Out flinches the opponent's faster/bigger threat — Dragonite gets a free Protect to Mega Evolve safely. Intimidate on switch-in softens physical attackers. Parting Shot is the primary reset tool — pivot to bring Pelipper back in and reset Rain. Chople Berry halves Fighting-type damage, directly addressing Sneasler's Close Combat — the most common source of Incineroar KOs at higher levels of play.

**Throat Chop** (43%) over Darkest Lariat (39%): blocks sound moves (Parting Shot, Snarl, Hyper Voice) on the target for 2 turns — disrupts opposing Incineroar and Snarl users.

**Chople Berry over Sitrus Berry:** Meta shows 15% Chople Berry usage on Incineroar. Sneasler (#2, 45% usage) runs Close Combat — at higher levels this is a consistent Incineroar KO threat. Chople Berry halves Fighting damage, which is more reliable than Sitrus Berry's one-time HP recovery when Sneasler is on the opponent's team.

---

## Flex Slots

Slot 5 is near-core — Whimsicott is brought in almost every game since Tailwind and weather reset are universally valuable. Slot 6 (Basculegion) is the true matchup-dependent flex.

### 5 (Near-core). Whimsicott @ Mental Herb

```text
Ability: Prankster
Type: Fairy / Grass
EVs: 252 HP / 4 SpAtk / 252 Speed
Nature: Timid
- Tailwind
- Moonblast
- Encore
- Protect
```

**Verified usage (Pikalytics 2026-04-14):** Tailwind 98% · Moonblast 95% · Encore 73% · Protect 44% · Sunny Day 31% · Taunt 10% | Item: Focus Sash 72% · Mental Herb 10% | Ability: Prankster 99%

**Role:** Speed control and Trick Room disruption. Prankster grants +1 priority to all status moves — Tailwind, Encore, and Protect all fire before any non-priority move regardless of Whimsicott's Speed.

**Prankster Tailwind:** Resolves before any neutral-priority move on turn 1. Pelipper previously failed to set Tailwind because it moves last at 65 base Speed and had to spend its move action on it. Whimsicott sets Tailwind for free at +1 priority — Pelipper now only needs to set Rain (Drizzle, automatic on switch-in) and survive.

**Moonblast:** Fairy STAB off 116 base Speed. Covers Dragon and Dark types that threaten the team. Not dependent on Rain or Prankster — consistent offensive pressure.

**Encore:** Locks opponents into their last used move at +1 priority. Primary application: opponent sets Trick Room, Encore forces them to use Trick Room again (toggling it off). Secondary: locks Protect spammers, Intimidate pivots, or a weakened attacker into a non-threatening move.

**Item — Mental Herb over Focus Sash:** Focus Sash is taken by Pelipper. Mental Herb cures one Taunt, preventing opponents from shutting down Whimsicott's support moves. With Prankster, Whimsicott's Tailwind and Encore already outspeed non-Prankster Taunts — Mental Herb specifically covers opposing Prankster Taunt users (mirror matchup).

---

### 6 (Flex B). Basculegion @ Choice Scarf

```text
Ability: Adaptability
Type: Water / Ghost
EVs: 252 Atk / 4 SpDef / 252 Speed
Nature: Adamant
- Last Respects
- Wave Crash
- Aqua Jet
- Flip Turn
```

**Verified usage (Pikalytics 2026-04-14):** Last Respects 97% · Wave Crash 94% · Aqua Jet 86% · Flip Turn 74% · Protect 28% | Item: Choice Scarf 65% · Mystic Water 27% | Ability: Adaptability 68% · Swift Swim 32%

**Bring when:** Attrition matchups where the game runs long and teammates will faint, or where a single devastating late-game move closes the set. Basculegion pairs with Pelipper at 45% in usage data — it is a confirmed Rain team finisher. Last Respects: 50 base power + 50 per fainted teammate. Wave Crash in Rain with Adaptability STAB is the heavy immediate hitter.

**Adaptability over Swift Swim (68% vs 32%):** Adaptability doubles STAB on all Water moves regardless of weather. Rain still adds x1.5 on top of that — the combination is (base power) x Adaptability x Rain. Choice Scarf provides Speed independently.

**Skip when:** Opponent's team is built to eliminate Basculegion early before Last Respects scales, or when the matchup calls for a second core Pokemon over the late-game closer.

---

## Lead Combinations

| Lead | Back | Matchup | Turn 1 Plan |
| --- | --- | --- | --- |
| Dragonite + Incineroar | Pelipper + Archaludon | Default — opponent has fast physical threat | Incineroar Fake Out faster threat; Dragonite Protect + Mega Evolve; T2 bring Pelipper for Rain + Dragonite attacks |
| Dragonite + Pelipper | Incineroar + Archaludon | Opponent lacks fast Ice or priority; need Rain T1 | Drizzle activates Rain; Dragonite Hurricane immediately; Incineroar back for Fake Out if needed T2 |
| Archaludon + Incineroar | Dragonite + Pelipper | Opponent has hard Dragonite lead counter (Sneasler, Fairy, Ice) | Incineroar Fake Out threat; Archaludon Electro Shot or Flash Cannon; bring Dragonite in T2 with Rain already active |
| Whimsicott + Pelipper | Incineroar + Dragonite | Standard Tailwind lead — want Rain + speed control T1 | Drizzle activates Rain; Whimsicott Prankster Tailwind fires at +1 priority before any opponent move; T2 Dragonite enters fast and attacks |
| Whimsicott + Incineroar | Pelipper + Dragonite | Opponent has fast lead threat requiring Fake Out first | Incineroar Fake Out faster threat; Whimsicott Prankster Tailwind fires simultaneously at +1; T2 Pelipper sets Rain + Dragonite enters |
| Whimsicott + Archaludon | Pelipper + Dragonite | Opponent has Trick Room threat; need Encore ready T1 | Whimsicott Prankster Encore on Trick Room setter; Archaludon tanks and pressures; bring Pelipper T2 for Rain |

**Rain reset sequence:** Incineroar Parting Shot → Pelipper switches in → Rain resets to 5 turns. Archaludon and Basculegion can cover 1-2 turns without Rain while the pivot happens.

---

## Threat Assessment

| Threat | Pokemon | Risk | Answer |
| --- | --- | --- | --- |
| Rock Slide spread | Tyranitar (#12) | HIGH — 4x on Dragonite/Pelipper; Sand overwrites Rain | Wide Guard (Pelipper); Archaludon Flash Cannon or Draco Meteor; Surf spread pressure |
| Moonblast / Dazzling Gleam | Whimsicott (#7), Floette (#9) | MEDIUM — 2x on Dragonite | Archaludon Flash Cannon (x2 vs Fairy); Incineroar absorbs |
| Close Combat / Extreme Speed | Sneasler (#2) | MEDIUM — physical priority breaks Multiscale; CC threatens Incineroar | Incineroar Fake Out buys a turn; Intimidate softens CC; Chople Berry option on Incineroar; Rage Powder redirection is no longer available (Sinistcha removed) |
| Dragon STAB | Garchomp (#3) | MEDIUM — fast physical attacker | Archaludon (Dragon resisted x0.5); Draco Meteor; Hurricane 2HKO |
| Weather overwrite | Tyranitar, Charizard Y | MEDIUM — Rain expires in 5 turns; Pelipper must re-enter to reset | Wide Guard blocks Sand spread; Incineroar Parting Shot pivots Pelipper back in; Archaludon/Basculegion can bridge 1-2 turns without Rain |
| Trick Room | Various | MEDIUM — inverts Speed advantage; Whimsicott Encore partially answers by locking setter into repeating TR | Prankster Encore forces TR setter to toggle TR off; Incineroar Taunt (not on current set) is the proactive answer — TODO |
| Fire coverage | Charizard (#8) | LOW in Rain — Fire halved; Dragonite resists Fire | Rain is the natural answer; Whimsicott Moonblast threatens Charizard back |

---

## Open Questions / Build TODOs

- [ ] Verify Dragonite EV spread — check Game8 for bulk benchmarks (survive specific attack at less than max Speed?): [Game8 guide](https://game8.co/games/Pokemon-Champions/archives/592442)
- [ ] Verify Archaludon EV spread — current (max HP / max SpDef Calm) is a starting point, not data-verified against Champions-specific benchmarks
- [ ] Confirm Archaludon item: Leftovers (50% meta) assumed; evaluate whether Magnet (+20% Electric) or White Herb (for Draco Meteor recoil) is better for this team's specific needs
- [ ] Trick Room answer — Whimsicott Encore partially answers; evaluate whether Incineroar Taunt over Throat Chop is needed for full proactive prevention
- [ ] Verify Whimsicott EV spread — current (252 HP / 252 Speed Timid) is a standard support spread; confirm no specific bulk benchmark needed for this team
- [ ] Confirm Champions Mega Stone spelling: Pikalytics shows "Dragoninite" (65% usage) while Game8 documents "Dragonitite" — likely a Pikalytics data entry inconsistency but verify in-game
- [ ] Build testing — ladder to validate lead combinations, Rain reset timing, and flex slot selection across matchups

---

## Version History

**v1 — 2026-04-14:** Created from Draft A in seed document. Sets preliminary, EV spreads unverified.

**v1.1 — 2026-04-14:** All sets verified against Pikalytics Champions live data (fetch_meta_stats.py).

- Incineroar: Assault Vest removed (not in Champions); Knock Off removed (not in Champions learnset); Darkest Lariat -> Throat Chop; item confirmed Sitrus Berry
- Pelipper: Damp Rock -> Focus Sash; Scald -> Weather Ball; Protect -> Wide Guard
- Sinistcha: Rocky Helmet -> Sitrus Berry (then Leftovers after Item Clause fix); Shadow Ball -> Life Dew; Strength Sap added; Hospitality confirmed
- Kingambit: Supreme Overlord -> Defiant; Weakness Policy -> Black Glasses (Life Orb unavailable in Champions)
- Basculegion: role revised from Swift Swim Rain abuser to Adaptability Last Respects sweeper; Choice Scarf confirmed

**v1.2 — 2026-04-14:** Team redesigned around Rain win condition rather than meta picks.

- Added Archaludon as core slot 3: Pelipper 72% teammate in usage data; Electro Shot one-turn charge in Rain; Steel/Dragon covers Dragonite's Ice/Fairy/Dragon counters; confirmed Rain team anchor
- Removed Kingambit: belongs to Sneasler-based offense teams (60% Sneasler teammate), zero Rain synergy
- Added Team Philosophy section defining core vs flex structure and the Rain synergy design constraint
- Sinistcha and Basculegion reclassified as Flex slots with explicit bring/skip conditions
- Sinistcha item: Leftovers (Item Clause conflict with Archaludon) -> Occa Berry
- Updated Lead Combinations and Threat Assessment

**v1.3 — 2026-04-19:** Replaced Sinistcha (Flex A) with Meganium @ Meganiumite.

- Dual Mega capable: both Dragonitite and Meganiumite on team; one Mega Evolution per battle chosen at preview
- Mode A (Dragonite Megas, default): Meganium base Grass, Leaf Guard, bulk EVs — Dazzling Gleam / Weather Ball (Water) / Earth Power / Protect
- Mode B (Meganium Megas, alternate): Mega Sol, Grass/Fairy, 143 SpAtk, offense EVs — Solar Beam (1-turn) / Weather Ball (Fire) / Dazzling Gleam (STAB) / Synthesis
- Meganium Mega triggers when opponent has heavy Fairy offense, Steel walls, or concentrated Ice/Rock countering Dragonite
- Item clause updated: Occa Berry → Meganiumite

**v1.4 — 2026-04-21:** Replaced Meganium (Flex A, rarely brought) with Whimsicott @ Mental Herb (Prankster). Addresses two structural team problems.

- **Tailwind failure fixed:** Pelipper at 65 base Speed frequently failed to set Tailwind — it moves last and had to use a move action. Whimsicott Prankster Tailwind fires at +1 priority guaranteed T1 regardless of Speed. Tailwind removed from Pelipper; Protect added instead (Pelipper now solely focuses on Rain setup and surviving).
- **Weather war fixed:** Whimsicott Prankster Rain Dance resets Rain at +1 priority the same turn opponent's Tyranitar or Charizard Y enters — no longer dependent on pivoting Pelipper back in for every reset.
- Whimsicott set: Tailwind / Rain Dance / Moonblast / Encore — Prankster applies to all four.
- Item clause updated: Meganiumite → Mental Herb.
- Lead Combinations updated: Meganium Mega leads replaced with Whimsicott Tailwind and weather-reset leads.
- Threat Assessment updated: Weather overwrite downgraded from MEDIUM to LOW (Prankster Rain Dance answers it); Trick Room partially answered by Prankster Encore.

**v1.5 — 2026-04-19:** EV spread overhaul + Incineroar item upgrade + Whimsicott set correction.

- **Dragonite EV:** 252 SpAtk / 4 SpDef / 252 Speed Timid → 252 SpAtk / 252 HP / 4 SpDef Modest. Speed EVs wasted on a Tailwind-dependent team; 252 HP strengthens Multiscale bulk. Modest over Timid for free SpAtk boost.
- **Incineroar item:** Sitrus Berry → Chople Berry. At higher levels, Sneasler (#2 meta, 45% usage) Close Combat is a consistent KO threat. Chople Berry halves Fighting damage more reliably than Sitrus Berry recovery.
- **Whimsicott set:** Rain Dance → Protect. Rain Dance is not in Whimsicott's competitive moveset in Champions (confirmed in-game). Correct set: Tailwind / Moonblast / Encore / Protect.
- Removed all Prankster Rain Dance references from Team Philosophy, Pelipper section, Lead Combinations, and Threat Assessment.
- Weather overwrite risk upgraded from LOW → MEDIUM (Rain reset now requires Pelipper pivot, not Whimsicott).
- Item clause updated: Sitrus Berry → Chople Berry.
