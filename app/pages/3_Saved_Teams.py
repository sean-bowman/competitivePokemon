'''
Saved Teams page.

Lists every team in docs/teams/data/, shows its summary table, and offers a
markdown export download. 'Edit in builder' loads the team into the Team Builder.
'''

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pandas as pd
import streamlit as st

from app import dataAccess, teamStore, theme

theme.applyTheme()

st.title('Saved Teams')

teams = teamStore.listTeams()
if not teams:
    st.info('No saved teams yet. Build one in the Team Builder, or run `python tools/migrate_builds.py`.')
    st.stop()

names = {t['name']: t['slug'] for t in teams}
pick = st.selectbox('Team', list(names.keys()))
team = teamStore.loadTeam(names[pick])

if team is None:
    st.error('Could not load that team.')
    st.stop()

meta = st.columns(3)
meta[0].metric('Format', team.get('format', '—').split('—')[-1].strip() or '—')
meta[1].metric('Created', team.get('created', '—'))
meta[2].metric('Meta snapshot', team.get('metaSnapshot', '—'))
if team.get('winCondition'):
    st.markdown(f'**Win condition:** {team["winCondition"]}')

rows = []
for slot in team.get('slots', []):
    if not slot.get('pokemon'):
        continue
    moves = (slot.get('moves', []) + ['', '', '', ''])[:4]
    rows.append({
        '#': slot.get('slot'),
        'Role': slot.get('role'),
        'Pokemon': slot.get('pokemon'),
        'Item': slot.get('item'),
        'Ability': slot.get('ability'),
        'Nature': slot.get('nature'),
        'Moves': ' / '.join(m for m in moves if m),
    })
st.dataframe(pd.DataFrame(rows), width='stretch', hide_index=True)

actions = st.columns([1, 1, 3])
with actions[0]:
    if st.button('Edit in builder', width='stretch'):
        base = teamStore.emptyTeam()
        base.update(team)
        st.session_state['team'] = base
        st.session_state['builderRev'] = st.session_state.get('builderRev', 0) + 1
        st.switch_page('pages/2_Team_Builder.py')
with actions[1]:
    st.download_button(
        'Download markdown', data=teamStore.exportMarkdown(team),
        file_name=f'{team.get("slug", "team")}.md', mime='text/markdown',
        width='stretch',
    )

with st.expander('Markdown preview'):
    st.code(teamStore.exportMarkdown(team), language='markdown')
