'''
Team Builder page.

Interactive six-slot editor. Dropdowns are seeded from the committed Champions
usage data (and PokeAPI profiles where available) but accept free text, since the
dataset is incomplete. The whole working team lives in st.session_state['team'];
widget keys are namespaced with a revision counter so loading a team resets them.
Validation (Item/Species clause, Champions legality, EV caps) runs every rerun.
'''

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import streamlit as st

from app import dataAccess, legality, teamStore, theme

theme.applyTheme()

NATURES = [
    'Hardy', 'Lonely', 'Brave', 'Adamant', 'Naughty', 'Bold', 'Docile', 'Relaxed',
    'Impish', 'Lax', 'Timid', 'Hasty', 'Serious', 'Jolly', 'Naive', 'Modest',
    'Mild', 'Quiet', 'Bashful', 'Rash', 'Calm', 'Gentle', 'Sassy', 'Careful', 'Quirky',
]

bust = dataAccess.cacheBust()
roster = dataAccess.availableChampionsPokemon(cacheBust=bust)
legalPool = dataAccess.loadLegalPool(cacheBust=bust)
availableItems = legalPool.get('items', {}).get('available', [])

# --- session state init -------------------------------------------------------
if 'team' not in st.session_state:
    st.session_state['team'] = teamStore.emptyTeam()
if 'builderRev' not in st.session_state:
    st.session_state['builderRev'] = 0

rev = st.session_state['builderRev']
team = st.session_state['team']


def _loadIntoBuilder(slug: str) -> None:
    '''Replace the working team and bump the revision so widgets reset.'''
    loaded = teamStore.loadTeam(slug)
    if loaded:
        # Backfill any missing schema fields from a blank template
        base = teamStore.emptyTeam()
        base.update(loaded)
        st.session_state['team'] = base
        st.session_state['builderRev'] += 1


def editableSelect(label: str, key: str, options: list[str], current: str | None,
                   placeholder: str) -> str | None:
    '''A selectbox that pre-selects `current` and accepts new free-text options.'''
    opts = list(dict.fromkeys(([current] if current else []) + list(options)))
    index = 0 if current else None
    value = st.selectbox(label, opts, index=index, key=key, placeholder=placeholder,
                         accept_new_options=True, label_visibility='visible')
    return value or None


st.title('Team Builder')

# --- toolbar: load / new ------------------------------------------------------
saved = teamStore.listTeams()
toolbar = st.columns([3, 1, 1])
with toolbar[0]:
    options = {t['name']: t['slug'] for t in saved}
    pick = st.selectbox('Load saved team', [': '] + list(options.keys()), index=0)
with toolbar[1]:
    st.write('')
    st.write('')
    if st.button('Load', width='stretch', disabled=(pick == ': ')):
        _loadIntoBuilder(options[pick])
        st.rerun()
with toolbar[2]:
    st.write('')
    st.write('')
    if st.button('New team', width='stretch'):
        st.session_state['team'] = teamStore.emptyTeam()
        st.session_state['builderRev'] += 1
        st.rerun()

st.divider()

# --- team metadata ------------------------------------------------------------
meta = st.columns([2, 2])
with meta[0]:
    teamName = st.text_input('Team name', value=team.get('name', ''), key=f'name_{rev}')
    teamFormat = st.text_input('Format', value=team.get('format', ''), key=f'format_{rev}')
with meta[1]:
    metaSnapshot = st.text_input('Meta snapshot referenced', value=team.get('metaSnapshot', ''),
                                 key=f'snap_{rev}')
    seedRef = st.text_input('Seed reference', value=team.get('seedReference', ''), key=f'seed_{rev}')
winCondition = st.text_area('Win condition', value=team.get('winCondition', ''),
                            key=f'win_{rev}', height=80)

# --- slot editors -------------------------------------------------------------
newSlots: list[dict] = []
existing = {s['slot']: s for s in team.get('slots', [])}

st.subheader('Slots')
for i in range(1, 7):
    slot = existing.get(i, teamStore.emptySlot(i))
    label = slot.get('pokemon') or f'Slot {i} (empty)'
    with st.expander(f'Slot {i}: {label}', expanded=bool(slot.get('pokemon'))):
        top = st.columns([2, 2, 2])
        with top[0]:
            pokemon = editableSelect('Pokemon', f'poke_{rev}_{i}', roster,
                                     slot.get('pokemon'), 'Select or type…')
        # Champions detail for the chosen Pokemon drives the move/item/ability options
        detail = dataAccess.loadChampionsDetail(pokemon, cacheBust=bust) if pokemon else None
        profile = dataAccess.loadPokemonProfile(pokemon, cacheBust=bust) if pokemon else None
        moveOpts = [m['name'] for m in (detail or {}).get('moves', [])]
        itemOpts = [it['name'] for it in (detail or {}).get('items', [])]
        itemOpts = list(dict.fromkeys(itemOpts + availableItems))
        abilityOpts = [a['name'] for a in (detail or {}).get('abilities', [])]
        if profile:
            abilityOpts += [a.replace('-', ' ').title() for a in profile.get('abilities', {}).get('normal', [])]
            hidden = profile.get('abilities', {}).get('hidden')
            if hidden:
                abilityOpts.append(hidden.replace('-', ' ').title())
        abilityOpts = list(dict.fromkeys(abilityOpts))

        with top[1]:
            item = editableSelect('Item', f'item_{rev}_{i}', itemOpts, slot.get('item'), 'Item…')
        with top[2]:
            ability = editableSelect('Ability', f'abil_{rev}_{i}', abilityOpts,
                                     slot.get('ability'), 'Ability…')

        role = st.text_input('Role', value=slot.get('role', ''), key=f'role_{rev}_{i}')

        moveCols = st.columns(4)
        moves = []
        slotMoves = (slot.get('moves', []) + ['', '', '', ''])[:4]
        for j in range(4):
            with moveCols[j]:
                mv = editableSelect(f'Move {j + 1}', f'move_{rev}_{i}_{j}', moveOpts,
                                    slotMoves[j] or None, ': ')
                moves.append(mv or '')

        st.caption('EV spread (max 252 per stat, 508 total)')
        evCols = st.columns(6)
        evs = {}
        slotEvs = slot.get('evs') or teamStore.emptyEvs()
        for k, statKey in enumerate(teamStore.EV_ORDER):
            with evCols[k]:
                evs[statKey] = st.number_input(
                    teamStore.EV_LABELS[statKey], min_value=0, max_value=252, step=4,
                    value=int(slotEvs.get(statKey, 0) or 0), key=f'ev_{rev}_{i}_{statKey}',
                )
        evTotal = sum(evs.values())
        natureCols = st.columns([2, 2])
        with natureCols[0]:
            nature = editableSelect('Nature', f'nat_{rev}_{i}', NATURES, slot.get('nature') or None, ': ')
        with natureCols[1]:
            st.metric('EV total', f'{evTotal} / 508')

        notes = st.text_area('Notes', value=slot.get('notes', ''), key=f'notes_{rev}_{i}', height=68)

    newSlots.append({
        'slot': i, 'role': role, 'pokemon': pokemon, 'item': item, 'ability': ability,
        'moves': moves, 'evs': evs, 'nature': nature or '', 'notes': notes,
    })

# --- assemble + persist working team ------------------------------------------
assembled = dict(team)
assembled.update({
    'name': teamName, 'format': teamFormat, 'winCondition': winCondition,
    'metaSnapshot': metaSnapshot, 'seedReference': seedRef, 'slots': newSlots,
    'slug': teamStore.slugifyTeam(teamName),
})
st.session_state['team'] = assembled

# --- validation panel ---------------------------------------------------------
st.divider()
st.subheader('Team validity')
findings = legality.validateTeam(assembled, legalPool)
errors = [f for f in findings if f['level'] == 'error']
warnings = [f for f in findings if f['level'] == 'warning']
if not findings:
    st.success('No issues found. Item Clause, Species Clause, legality, and EV caps all pass.')
for f in errors:
    st.error(f['message'])
for f in warnings:
    st.warning(f['message'])

# --- save ---------------------------------------------------------------------
st.divider()
save = st.columns([1, 1, 3])
with save[0]:
    exportMd = st.checkbox('Export markdown', value=True)
with save[1]:
    if st.button('Save team', width='stretch', type='primary'):
        from datetime import date
        assembled['updated'] = str(date.today())
        if not assembled.get('created'):
            assembled['created'] = str(date.today())
        result = teamStore.saveTeam(assembled, exportMarkdownDoc=exportMd)
        dataAccess.bumpCacheBust()
        msg = f'Saved {Path(result["jsonPath"]).name}'
        if result.get('markdownPath'):
            msg += f' and {Path(result["markdownPath"]).name}'
        st.success(msg)
with save[2]:
    st.caption('Saves to docs/teams/data/ (JSON) and, if enabled, docs/teams/builds/ (markdown).')
