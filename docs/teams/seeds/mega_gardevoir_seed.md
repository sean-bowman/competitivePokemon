# Team Seed: Mega Gardevoir Offense

**Format:** Pokemon Champions: Double Battles (VGC)
**Created:** 2026-04-15
**Build Document:** [../builds/gardevoir_offense_v1.md](../builds/gardevoir_offense_v1.md)

---

## Win Condition

Mega Gardevoir (Pixilate) fires Hyper Voice as a ~130 BP spread Fairy move at both opponents. Aerodactyl sets Tailwind for speed control. Garchomp provides Ground/Rock coverage from the back or via Rock Slide when paired with Gardevoir. Milotic punishes Intimidate with Competitive (+2 SpAtk per stat drop).

Unlike the Dragonite Rain team, this team has **no weather dependency**. Speed control is through Tailwind and Icy Wind rather than Rain.

---

## Research -- Gardevoir in Champions Meta (Pikalytics 2026-04-15)

### Mega Gardevoir

- **Gardevoirite: 65.7%**: Mega is the dominant build
- Choice Scarf: 29.4%: non-Mega Scarf set exists as separate archetype
- **Ability: Telepathy 43%, Trace 37%, Pixilate 10%**
  - **Confirmed (Game8/Serebii 2026-04-15): Mega Gardevoir's ability in Champions is Pixilate**: identical to mainline Gen VI. The Pikalytics ability percentages reflect pre-Mega base ability selection, not the Mega ability. Telepathy (43%) and Trace (37%) are the base abilities players choose before Mega Evolving.
  - Once Mega Evolved via Gardevoirite, the ability becomes Pixilate regardless of base ability.
  - Trace (37%) is useful for the non-Mega Choice Scarf set: copies the opponent's ability on switch-in.
  - Telepathy as base ability does NOT provide Earthquake immunity after Mega Evolution.
- **Top moves:** Protect 67% · Hyper Voice 64% · Psychic 54% · Moonblast 45% · Psyshock 36% · Trick Room 32% · Dazzling Gleam 29% · Calm Mind 14% · Icy Wind 13%
- **Top teammates:** Garchomp 61% · Incineroar 58% · Sneasler 32% · Sinistcha 29% · Charizard 27% · Milotic 27%

### Garchomp (Gardevoir's primary partner)

- Rough Skin: 88% | Choice Scarf: 30% · White Herb: 17% · Soft Sand: 13%
- **Top moves:** Earthquake 89% · Dragon Claw 85% · Rock Slide 72% · Protect 67% · Stomping Tantrum 51%
- **Top teammates:** Incineroar 53% · Sneasler 47% · Charizard 34% · Rotom-Wash 27% · Whimsicott 26%

### Aerodactyl (Tailwind setter)

- Unnerve: 85% | Focus Sash: 69% · Aerodactylite: 23%
- **Top moves:** Rock Slide 99% · Protect 95% · Dual Wingbeat 94% · **Tailwind 89%** · Wide Guard 8%
- **Top teammates:** Incineroar 59% · Sneasler 57% · Floette 52% · Garchomp 52% · Sinistcha 36%
- Role: dedicated Tailwind setter. Focus Sash guarantees it survives one hit to set Tailwind.

### Milotic (Competitive punisher)

- **Competitive: 96%** | Leftovers: 76% · Sitrus Berry: 13%
- **Top moves:** Scald 89% · Protect 86% · Ice Beam 54% · **Icy Wind 53%** · Recover 46% · Life Dew 19%
- **Top teammates:** Incineroar 53% · Garchomp 50% · Sneasler 37% · Charizard 37% · Sinistcha 30%
- Role: Intimidate punisher. Every Incineroar on the field (54% meta usage) drops a stat and triggers Competitive (+2 SpAtk). Icy Wind provides speed control as a second layer after Tailwind.

---

## Team Skeleton

| # | Role | Pokemon | Item | Notes |
| --- | --- | --- | --- | --- |
| 1 | Fairy/Psychic spread (core) | Mega Gardevoir | Gardevoirite | Telepathy: immune to ally Earthquake |
| 2 | Ground spread (core) | Garchomp | White Herb | Earthquake + Rock Slide; White Herb vs Intimidate |
| 3 | Speed control (core) | Aerodactyl | Focus Sash | Tailwind setter; Unnerve blocks berries |
| 4 | Fake Out support (core) | Incineroar | Sitrus Berry | Enabler; also baits Milotic's Competitive |
| 5 | Flex A: Intimidate punisher | Milotic | Leftovers | Competitive; Icy Wind speed control; Recover |
| 6 | Flex B: late game | TBD | TBD | Basculegion or Sinistcha depending on testing |

**Item clause check (skeleton):** Gardevoirite / White Herb / Focus Sash / Sitrus Berry / Leftovers: all unique. Flex B item TBD.

---

## Key Synergies and Design Logic

**Pixilate Hyper Voice:**
Mega Gardevoir's Pixilate converts Hyper Voice from Normal-type to Fairy-type and boosts it by 20%. With STAB: 90 BP × 1.2 (Pixilate) × 1.5 (STAB) = 162 effective power as a spread move hitting both opponents. This is one of the most powerful spread moves in the game. It covers Dragon, Dark, and Fighting types: the three most common meta archetypes.

**Garchomp pairing: coverage synergy, not Earthquake immunity:**
Mega Gardevoir does not have Telepathy: the ability is Pixilate after Mega Evolution. Garchomp pairs with Gardevoir for type coverage: Garchomp's Ground/Dragon covers Steel types that resist Fairy; Gardevoir's Fairy covers Dragon types that threaten Garchomp. When paired on the field, Garchomp uses Rock Slide (hits both opponents safely) alongside Gardevoir's Hyper Voice. Earthquake is reserved for turns when Gardevoir Protects or is not on the field.

**Tailwind + high base Speed:**
Gardevoir (100), Garchomp (102), Aerodactyl (130). All three have 100+ base Speed. Under Tailwind they reach 200/204/260 effective Speed: faster than everything in the meta. Speed control enables the team to attack before most threats without relying on choice items.

**Competitive bait:**
Incineroar is on 54% of teams in the meta. Every game, someone will drop stats via Intimidate or Parting Shot. Milotic with Competitive converts those drops into +2 SpAtk: opponent punishes themselves for using their best support Pokemon.

**No weather dependency:**
Unlike the Dragonite Rain team, this team does not need a specific weather condition. It functions from turn 1 regardless of weather. This removes the weather war counterplay and makes the team more robust against Sand (Tyranitar) and Sun (Charizard) teams.

---

## Potential Weaknesses

- **Trick Room:** This team is Speed-based and Tailwind-dependent. Trick Room inverts the advantage entirely: Gardevoir and Garchomp become the slowest. Need a Trick Room answer.
- **Steel types:** Gardevoir's Hyper Voice (Normal, without Pixilate) is blocked by Normal-immune Ghost types. Flash Cannon, Iron Head, and similar Steel moves threaten Gardevoir's Fairy typing. Garchomp's Earthquake covers Steel types.
- **Aerodactyl as single point of failure for speed control:** If Aerodactyl is KO'd before setting Tailwind, the team's Speed advantage collapses. Milotic's Icy Wind provides a backup speed control layer.
- **Dragon types:** Gardevoir handles Dragons via Fairy coverage. Garchomp is Dragon itself and neutral to Dragon. Adequate but not dominant.

---

## Draft Sets

### Mega Gardevoir

```text
Ability: Pixilate (confirmed: Mega ability)
Item: Gardevoirite
EVs: TBD (see TODO)
Nature: Timid
- Hyper Voice
- Psychic
- Moonblast
- Protect
```

Hyper Voice is the primary spread move: Pixilate converts it to Fairy-type at 90 × 1.2 × 1.5 (STAB) = 162 effective power hitting both opponents. Moonblast is the single-target Fairy nuke. Psychic for Poison/Fighting coverage.

### Garchomp

```text
Ability: Rough Skin
Item: White Herb
EVs: TBD
Nature: Jolly or Adamant
- Earthquake
- Rock Slide
- Dragon Claw
- Protect
```

### Aerodactyl

```text
Ability: Unnerve
Item: Focus Sash
EVs: 252 Atk / 4 Def / 252 Speed
Nature: Jolly
- Rock Slide
- Dual Wingbeat
- Tailwind
- Protect
```

### Incineroar

```text
Ability: Intimidate
Item: Sitrus Berry
EVs: 252 HP / 4 Atk / 252 SpDef
Nature: Careful
- Fake Out
- Parting Shot
- Flare Blitz
- Throat Chop
```

### Milotic

```text
Ability: Competitive
Item: Leftovers
EVs: 252 HP / 4 SpAtk / 252 SpDef
Nature: Calm
- Scald
- Ice Beam
- Icy Wind
- Recover
```

---

## Research TODOs Before Draft A

- [x] **Verified: Mega Gardevoir ability in Champions is Pixilate** (Game8 + Serebii, 2026-04-15). Hyper Voice = spread Fairy move. Telepathy/Trace in usage data reflect pre-Mega base ability, not the Mega ability.
- [ ] **Verify Garchomp EV spread**: Choice Scarf 30% suggests some players prefer raw Speed; without Scarf under Tailwind, what spread is optimal?
- [ ] **Evaluate 6th slot**: Basculegion (more Rain-style late-game) vs Sinistcha (redirection) vs something team-specific
- [ ] **Check Trick Room answer**: Incineroar Taunt or a separate Pokemon?
- [ ] **Verify Gardevoir learnset in Champions**: confirm Hyper Voice, Moonblast, Psyshock, Calm Mind are all in the Champions learnset
