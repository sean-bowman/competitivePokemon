# Build: Mega Gardevoir Spread Offense — v1

**Format:** Pokemon Champions — Double Battles (VGC)
**Status:** BUILD — active development document
**Created:** 2026-04-15
**Seed Reference:** [../seeds/mega_gardevoir_seed.md](../seeds/mega_gardevoir_seed.md)
**Win Condition:** Aerodactyl sets Tailwind → Mega Gardevoir fires Pixilate Hyper Voice as a ~162 effective power spread Fairy move at both opponents → Garchomp provides Ground/Rock coverage from back or via Rock Slide when paired → Milotic punishes Intimidate with Competitive +2 SpAtk

---

## Team Philosophy

This team applies **Pixilate Fairy spread pressure**. Mega Gardevoir's Hyper Voice becomes a Fairy-type move via Pixilate (confirmed ability), hitting both opponents at 90 × 1.2 (Pixilate) × 1.5 (STAB) = 162 effective power. That covers Dragon, Dark, and Fighting types — the three most common meta archetypes. Speed control is through Tailwind (Aerodactyl) and Icy Wind (Milotic), with no weather dependency.

**Core mechanics:**
- Pixilate Hyper Voice: 162 effective power spread Fairy move — one of the strongest spread moves in the game
- Tailwind (Aerodactyl, 89% usage) doubles Speed — Gardevoir (100), Garchomp (102), and Aerodactyl (130) all reach 200+ under Tailwind
- Competitive (Milotic, 96% usage) converts Intimidate/Parting Shot into +2 SpAtk — Incineroar at 54% meta usage means this triggers almost every game

**Ability clarification — Pixilate, not Telepathy:**
Mega Gardevoir's ability in Champions is Pixilate (confirmed Game8/Serebii, 2026-04-15). The Pikalytics data showing 43% "Telepathy" reflects players' pre-Mega base ability selection, not the Mega ability. Once Gardevoir Mega Evolves via Gardevoirite, the ability becomes Pixilate regardless. Gardevoir is **not immune to ally Earthquake** after Mega Evolution.

**Core (4 slots — almost always brought):**
1. Mega Gardevoir — spread Fairy attacker (Pixilate Hyper Voice); Psychic/Moonblast coverage
2. Garchomp — Ground/Dragon attacker; Rock Slide pairs with Gardevoir on the field; Earthquake used when Gardevoir Protects or is off-field
3. Aerodactyl — Tailwind setter; Focus Sash guarantees Tailwind even under attack
4. Incineroar — Fake Out support; enables safe lead turns; baits Milotic's Competitive

**Flex (2 slots — chosen at team preview):**
5. Milotic — Intimidate punisher; Icy Wind speed control backup; Recover
6. Sinistcha — brought when redirection or Hospitality healing is the priority

**Contrast with Dragonite Rain team:** Dragonite requires Rain — weather wars are a hard matchup. This team has no weather dependency. The Gardevoir team threatens Dragon/Dark/Fighting types that Rain teams sometimes struggle to answer directly.

---

## Team Summary

> Item Clause: no duplicate items permitted. See [competitive_pokemon_overview.md](../../competitive_pokemon_overview.md).

| # | Role | Pokemon | Item | Ability | Move 1 | Move 2 | Move 3 | Move 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Fairy spread (core) | Mega Gardevoir | Gardevoirite | Pixilate | Hyper Voice | Psychic | Moonblast | Protect |
| 2 | Ground/Dragon coverage (core) | Garchomp | White Herb | Rough Skin | Earthquake | Rock Slide | Dragon Claw | Protect |
| 3 | Speed control (core) | Aerodactyl | Focus Sash | Unnerve | Tailwind | Rock Slide | Dual Wingbeat | Protect |
| 4 | Enabler (core) | Incineroar | Chople Berry | Intimidate | Fake Out | Parting Shot | Flare Blitz | Throat Chop |
| 5 | Flex A — Intimidate punisher | Milotic | Leftovers | Competitive | Scald | Ice Beam | Icy Wind | Recover |
| 6 | Flex B — Trick Room counter / speed redundancy | Whimsicott | Mental Herb | Prankster | Tailwind | Moonblast | Encore | Taunt |

**Item clause check:** Gardevoirite / White Herb / Focus Sash / Chople Berry / Leftovers / Mental Herb — all unique.

---

## Core Roster

### 1. Mega Gardevoir @ Gardevoirite

```text
Ability: Pixilate (Mega ability — confirmed)
Type: Psychic / Fairy
EVs: 252 SpAtk / 252 HP / 4 SpDef
Nature: Modest
- Hyper Voice
- Psychic
- Moonblast
- Protect
```

**Verified usage (Pikalytics 2026-04-15):** Protect 67% · Hyper Voice 64% · Psychic 54% · Moonblast 45% · Psyshock 36% · Trick Room 32% · Dazzling Gleam 29% · Calm Mind 14% · Icy Wind 13% | Item: Gardevoirite 66% · Choice Scarf 29% | Ability (pre-Mega): Telepathy 43% · Trace 37% · Pixilate 10%

**Role:** Primary offensive threat. Hyper Voice is the core move — Pixilate converts it to Fairy-type and boosts it 20%, giving 90 × 1.2 × 1.5 (STAB) = 162 effective power as a spread move hitting both opponents. This threatens Dragon, Dark, and Fighting types simultaneously. Psychic is single-target coverage for Poison and Fighting. Moonblast is the single-target Fairy nuke (95 BP, 30% SpDef drop). Protect buys positioning turns and covers while Aerodactyl sets Tailwind.

**On Hyper Voice vs Dazzling Gleam:** Hyper Voice (90 BP, hits through Substitute) is the standard spread Fairy move with Pixilate. Dazzling Gleam (29% usage, 80 BP) is the non-Pixilate alternative for non-Mega sets. With Mega Gardevoir and Pixilate, Hyper Voice is strictly superior.

**EV rationale:** 252 SpAtk + Modest for max damage output. Speed EVs dropped — this team is Tailwind-dependent, and under Tailwind even 0 Speed EVs result in a doubled stat that outruns all non-Tailwind threats. Without Tailwind, Gardevoir (100 base) cannot outspeed Sneasler (110) or Aerodactyl (130) regardless of EVs. Timid → Modest gives a free SpAtk boost at no functional cost. 252 HP replaces Speed EVs for real bulk improvement.

**Move 4 alternatives:**
- **Moonblast** (current, 45%): reliable single-target Fairy nuke, SpDef drop chance
- **Psyshock** (36%): Psychic-type hitting physical Defense — counters SpDef walls specifically
- **Calm Mind** (14%): +1 SpAtk/SpDef; viable if free turns are available
- **Icy Wind** (13%): speed control; useful if Milotic is not brought

---

### 2. Garchomp @ White Herb

```text
Ability: Rough Skin
Type: Dragon / Ground
EVs: 252 Atk / 220 HP / 32 Speed / 4 Def
Nature: Jolly
- Earthquake
- Rock Slide
- Dragon Claw
- Protect
```

**Verified usage (Pikalytics 2026-04-15):** Earthquake 89% · Dragon Claw 85% · Rock Slide 72% · Protect 67% · Stomping Tantrum 51% | Item: Choice Scarf 30% · White Herb 17% · Soft Sand 13% · Lum Berry 10% | Ability: Rough Skin 88%

**Role:** Ground/Dragon attacker and Steel-type answer. Gardevoir's Hyper Voice is blocked by Steel types (resisted) — Garchomp's Earthquake covers Steel, Fire, and Rock types that threaten the team. **When on the field alongside Gardevoir:** use Rock Slide (spread, hits both opponents safely) + Gardevoir Hyper Voice for dual spread. **When Gardevoir Protects or is off-field:** Earthquake freely. Garchomp does not need to be the active Gardevoir partner — it often comes in from the back after Incineroar pivots.

**EV rationale:** 252 Atk for max damage. 32 Speed EVs Jolly reaches ~177 Speed, outspeeding sub-100 base threats (Incineroar, Slowbro, etc.) without Tailwind while freeing 220 EVs into HP. Under Tailwind the Speed doubles anyway — max Speed investment is wasted on a Tailwind team. 4 Def dump stat.

**Item — White Herb over Choice Scarf:** Under Tailwind, Garchomp reaches 354+ effective Speed — Choice Scarf is redundant. White Herb restores one stat drop (most commonly Intimidate's -1 Atk), neutralizing the most common support move in the meta. Soft Sand (13%) is a consistent +20% Earthquake boost if stat recovery isn't needed.

**Rough Skin** (88%): chips any Pokemon that makes contact. In Doubles this punishes U-turn, physical priority, and body-contact moves.

---

### 3. Aerodactyl @ Focus Sash

```text
Ability: Unnerve
Type: Rock / Flying
EVs: 252 Atk / 4 Def / 252 Speed
Nature: Jolly
- Tailwind
- Rock Slide
- Dual Wingbeat
- Protect
```

**Verified usage (Pikalytics 2026-04-15):** Rock Slide 99% · Protect 95% · Dual Wingbeat 94% · Tailwind 89% · Wide Guard 8% | Item: Focus Sash 69% · Aerodactylite 23% | Ability: Unnerve 85%

**Role:** Speed control anchor. Aerodactyl at 130 base Speed outspeeds most leads. Focus Sash guarantees it survives at least one hit to set Tailwind — the team's Speed advantage is entirely contingent on Tailwind going up. After Tailwind is set, Rock Slide (spread, flinch chance) and Dual Wingbeat (breaks Focus Sash on opposing speed control) provide offensive pressure. Rock Slide paired with Garchomp's Rock Slide creates dual flinch spread from Rock-type moves.

**Unnerve** (85%): prevents opponents from activating held Berries. Disables Sitrus Berry, Chople Berry, and resist Berries during the critical turns when Aerodactyl is on the field.

**Wide Guard note (8%):** Blocks spread moves for the whole team — relevant against Tyranitar Rock Slide and Garchomp Earthquake from opposing teams. Not currently on this set but worth considering if spread-move matchups are consistently problematic.

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

**Verified usage (Pikalytics 2026-04-15):** Fake Out 99% · Parting Shot 96% · Flare Blitz 85% · Throat Chop 43% · Darkest Lariat 39% | Item: Sitrus Berry 56% · Chople Berry 15% | Ability: Intimidate 98%

**Role:** Fake Out enables the lead — most commonly flinches the opponent's faster threat so Aerodactyl sets Tailwind safely on turn 2. Parting Shot is the pivot and Milotic Competitive bait — Parting Shot drops both Atk and SpAtk, triggering Competitive twice (+4 SpAtk total). Incineroar's Intimidate on switch-in also triggers Competitive on any Milotic that's on the field.

**Chople Berry over Sitrus Berry:** Sneasler (#2 meta, 45% usage) Close Combat is a consistent Incineroar KO threat at higher levels. Chople Berry halves Fighting damage, which is more reliable than Sitrus Berry's one-time HP recovery when Sneasler is on the opponent's team. Meta shows 15% Chople Berry usage on Incineroar.

---

## Flex Slots

### 5 (Flex A). Milotic @ Leftovers

```text
Ability: Competitive
Type: Water
EVs: 252 HP / 4 SpAtk / 252 SpDef
Nature: Calm
- Scald
- Ice Beam
- Icy Wind
- Recover
```

**Verified usage (Pikalytics 2026-04-15):** Scald 89% · Protect 86% · Ice Beam 54% · Icy Wind 53% · Recover 46% · Life Dew 19% | Item: Leftovers 76% · Sitrus Berry 13% | Ability: Competitive 96%

**Bring when:** Opponent has Incineroar, Parting Shot, or Snarl users. Each stat drop on Milotic is +2 SpAtk. With Incineroar at 54% meta usage, Competitive triggers nearly every game. Parting Shot (-1 Atk, -1 SpAtk) triggers Competitive twice (+4 SpAtk). By turn 2-3, Milotic commonly has +4 to +6 SpAtk — Scald and Ice Beam become genuine threats at that stage.

**Icy Wind:** Speed control after Tailwind expires (4 turns). Drops both opponents' Speed, maintaining the team's relative speed advantage across a full game.

**Skip when:** Opponent team lacks stat-lowering moves; Sinistcha's immediate redirection is more critical.

---

### 6 (Flex B). Whimsicott @ Mental Herb

```text
Ability: Prankster
Type: Fairy / Grass
EVs: 252 HP / 4 SpAtk / 252 Speed
Nature: Timid
- Tailwind
- Moonblast
- Encore
- Taunt
```

**Verified usage (Pikalytics 2026-04-14):** Tailwind 98% · Moonblast 95% · Encore 73% · Protect 44% · Taunt 10% | Item: Focus Sash 72% · Mental Herb 10% | Ability: Prankster 99%

**Role:** Trick Room counter and backup speed control. Prankster grants +1 priority to all status moves — Taunt (+1 priority) goes before Trick Room (-7 priority), preventing TR from being set. Encore (+1 priority) locks TR setters into repeating TR, which toggles it off on the following turn. Tailwind at +1 priority provides speed control if Aerodactyl goes down before setting it.

**Trick Room interaction detail:**

- Prankster Taunt (+1 priority) → resolves before Trick Room (-7 priority) → TR setter cannot use TR this turn
- If TR is already up: Prankster Encore after opponent uses TR → they are locked into TR → their next TR use toggles TR off

**Item — Mental Herb over Focus Sash:** Focus Sash is taken by Aerodactyl. Mental Herb cures a single use of Taunt, Encore, Disable, Infatuation, or Torment — protects Whimsicott from being Taunted before it can Taunt, which is the primary failure mode for this role. In practice, Prankster Taunt already out-priorities most Taunts, so Mental Herb mainly covers opposing Prankster Taunt users.

**Bring when:** Opponent has a Trick Room setter (Sinistcha 66% TR, Farigiraf, Porygon2, Dusclops). Also bring when Aerodactyl matchup looks risky — Whimsicott provides redundant Tailwind.

**Skip when:** Opponent team lacks Trick Room threats and Aerodactyl is safe to lead; Milotic's Competitive activation is more critical to the game plan.

---

## Lead Combinations

| Lead | Back | Matchup | Turn 1 Plan |
| --- | --- | --- | --- |
| Gardevoir + Aerodactyl | Incineroar + Garchomp | Default — can set Tailwind safely T1 | Aerodactyl Tailwind; Gardevoir Protect or Hyper Voice; T2 Gardevoir attacks at full power under Tailwind |
| Gardevoir + Incineroar | Aerodactyl + Garchomp | Opponent has faster threat; Fake Out needed first | Incineroar Fake Out faster threat; Gardevoir Protect; T2 Aerodactyl sets Tailwind; T3 Gardevoir attacks |
| Garchomp + Aerodactyl | Gardevoir + Incineroar | Opponent leads weak to Ground or Rock | Aerodactyl Tailwind; Garchomp Earthquake or Rock Slide; bring Gardevoir in T2 for Hyper Voice |
| Gardevoir + Garchomp | Aerodactyl + flex | Opponent lacks priority or Ice; want spread pressure immediately | Gardevoir Hyper Voice; Garchomp Rock Slide (safe alongside Gardevoir); Aerodactyl Tailwind T2 |

**Earthquake management:** When Gardevoir and Garchomp are both on the field, Garchomp uses Rock Slide (not Earthquake) to avoid hitting Gardevoir. Earthquake is used on turns when Gardevoir Protects or when Gardevoir has been switched out.

---

## Threat Assessment

| Threat | Pokemon | Risk | Answer |
| --- | --- | --- | --- |
| Trick Room | Various (Sinistcha 66% TR) | HIGH — inverts Speed advantage; Gardevoir/Garchomp become slowest | **Whimsicott Prankster Taunt** (+1 priority, resolves before TR's -7 priority); Encore locks setter into toggling TR off |
| Steel types | Aegislash, Archaludon, Corviknight | MEDIUM — resist or immune to Fairy; Hyper Voice resisted | Garchomp Earthquake covers most Steel types; Psychic has neutral coverage |
| Close Combat / priority | Sneasler (#2, 45%) | MEDIUM — Fake Out and CC threaten leads; breaks Aerodactyl Sash if faster | Incineroar Fake Out first; Aerodactyl Dual Wingbeat breaks Sash in mirror; Garchomp Earthquake OHKOs |
| Rock Slide spread | Tyranitar (#12) | MEDIUM — Aerodactyl 4x Rock weakness; Sash absorbs T1 | Garchomp Earthquake vs Tyranitar; Gardevoir Hyper Voice pressure; Aerodactyl survives T1 via Sash |
| Poison coverage | Various (targets Fairy types) | MEDIUM — Poison is 2x vs Fairy | Psychic covers Poison types; Garchomp Earthquake; Incineroar Flare Blitz |
| Ice coverage | Any Ice Beam | MEDIUM — Garchomp 4x Ice; Gardevoir 2x Ice | Milotic resists Ice; Aerodactyl Protect; Whimsicott Encore locks Ice Beam users |

---

## Open Questions / Build TODOs

- [x] ~~Verify Mega Gardevoir ability~~ — **Pixilate confirmed** (Game8/Serebii, 2026-04-15)
- [ ] Verify Gardevoir learnset in Champions — confirm Hyper Voice, Moonblast, Psyshock, Calm Mind are all in the Champions learnset
- [x] ~~Evaluate Gardevoir EV spread~~ — **252 SpAtk / 252 HP / 4 SpDef Modest confirmed** (2026-04-19); Speed EVs wasted on Tailwind team; benchmark bulk vs specific attacks still TODO
- [ ] Evaluate Garchomp item: White Herb (current) vs Soft Sand (+20% Ground boost) vs Lum Berry (anti-status) — depends on how often Intimidate chip is the problem vs consistent Earthquake output
- [x] ~~Trick Room answer~~ — **Whimsicott (Prankster) added as Flex B** (2026-04-15); replaces Sinistcha
- [ ] Evaluate 4th move on Gardevoir: Moonblast vs Psyshock vs Calm Mind
- [ ] Build testing — validate Aerodactyl lead timing, Rock Slide + Hyper Voice spread combination, and Competitive activation cadence

---

## Version History

**v1 — 2026-04-15:** Initial build. Core set from Pikalytics data (2026-04-15). EV spreads preliminary.

**v1.1 — 2026-04-15:** Corrected fundamental ability assumption. Mega Gardevoir ability is Pixilate (not Telepathy) — confirmed via Game8 and Serebii. Updated all references: Hyper Voice is now a Fairy-type spread move (not Normal), Garchomp pairing is type coverage synergy (not Earthquake immunity), team philosophy reframed around Pixilate Fairy spread offense. Earthquake management section added to Lead Combinations.

**v1.2 — 2026-04-15:** Replaced Sinistcha (Flex B) with Whimsicott @ Mental Herb (Prankster). Sinistcha's defensive/redirect role did not mesh with offensive spread identity. Whimsicott addresses the team's HIGH-risk Trick Room gap via Prankster Taunt (+1 priority beats TR's -7 priority) and provides redundant Tailwind if Aerodactyl goes down. Threat Assessment updated accordingly.

**v1.3 — 2026-04-19:** EV spread overhaul + Incineroar item upgrade.

- **Gardevoir EV:** 252 SpAtk / 4 SpDef / 252 Speed Timid → 252 SpAtk / 252 HP / 4 SpDef Modest. Speed EVs wasted on a Tailwind-dependent team; cannot outspeed Sneasler/Aerodactyl regardless of EVs without Tailwind. Modest over Timid for free SpAtk boost.
- **Garchomp EV:** 252 Atk / 4 Def / 252 Speed Jolly → 252 Atk / 220 HP / 32 Speed / 4 Def Jolly. 32 Speed EVs still clear sub-100 base Speed threats; 220 EVs freed into HP for bulk under Tailwind.
- **Incineroar item:** Sitrus Berry → Chople Berry. Sneasler Close Combat is a consistent KO threat at higher levels; Chople Berry halves Fighting damage more reliably than one-time Sitrus recovery.
- Item clause updated: Sitrus Berry → Chople Berry (Gardevoirite / White Herb / Focus Sash / Chople Berry / Leftovers / Mental Herb).
