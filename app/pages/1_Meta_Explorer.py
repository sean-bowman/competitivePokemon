'''
Meta Explorer page.

Browse the current Pikalytics Champions usage snapshot, then drill into any
Pokemon for its move / item / ability / teammate breakdown and base stats.
A teammate-correlation heatmap summarises pairings across the dataset.
'''

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

import pandas as pd
import streamlit as st

from app import charts, dataAccess, theme

theme.applyTheme()

st.title('Meta Explorer')

bust = dataAccess.cacheBust()
snapshot = dataAccess.loadSnapshot(cacheBust=bust)
allDetail = dataAccess.loadAllChampionsDetail(cacheBust=bust)

if snapshot is None:
    st.warning('No meta snapshot found. Refresh from the Home page or run the fetch script.')
    st.stop()

st.caption(
    f'{snapshot.get("format", "—")} · snapshot {snapshot.get("fetched", "—")} · '
    f'{len(allDetail)} Pokemon with detailed data'
)

usageTab, detailTab, pairTab = st.tabs(['Usage table', 'Pokemon detail', 'Teammate correlation'])

with usageTab:
    pokemon = snapshot.get('pokemon', [])
    table = pd.DataFrame([
        {
            'Rank': p.get('rank'),
            'Pokemon': p.get('name'),
            'Usage %': p.get('usage_pct'),
            'Win %': p.get('win_rate'),
            'Record': p.get('record'),
        }
        for p in pokemon
    ])
    st.dataframe(table, width='stretch', hide_index=True)
    st.plotly_chart(charts.usageBar(pokemon, topN=20), width='stretch')

with detailTab:
    names = dataAccess.availableChampionsPokemon(cacheBust=bust)
    if not names:
        st.info('No per-Pokemon detail data committed yet. Fetch with --detail.')
    else:
        selected = st.selectbox('Pokemon', names)
        detail = dataAccess.loadChampionsDetail(selected, cacheBust=bust)
        profile = dataAccess.loadPokemonProfile(selected, cacheBust=bust)

        header = st.columns([2, 3])
        with header[0]:
            if profile:
                types = ' / '.join(t.title() for t in profile.get('types', []))
                st.markdown(f'**Type:** {types or "—"}')
                abilities = profile.get('abilities', {})
                normal = ', '.join(a.replace('-', ' ').title() for a in abilities.get('normal', []))
                hidden = (abilities.get('hidden') or '').replace('-', ' ').title()
                st.markdown(f'**Abilities:** {normal or "—"}' + (f' · _Hidden:_ {hidden}' if hidden else ''))
            else:
                st.caption('No PokeAPI profile committed for this Pokemon (e.g. a Mega form).')
        with header[1]:
            if profile and profile.get('base_stats'):
                st.plotly_chart(charts.statsBar(profile['base_stats']), width='stretch')

        if detail:
            row1 = st.columns(2)
            with row1[0]:
                st.markdown('**Common moves**')
                st.plotly_chart(charts.detailBar(detail.get('moves', []), theme.ACCENT),
                                width='stretch')
            with row1[1]:
                st.markdown('**Common items**')
                st.plotly_chart(charts.detailBar(detail.get('items', []), theme.GREEN),
                                width='stretch')
            row2 = st.columns(2)
            with row2[0]:
                st.markdown('**Abilities**')
                st.plotly_chart(charts.detailBar(detail.get('abilities', []), theme.BLUE),
                                width='stretch')
            with row2[1]:
                st.markdown('**Common teammates**')
                st.plotly_chart(charts.detailBar(detail.get('teammates', []), theme.ACCENT_SOFT),
                                width='stretch')
        else:
            st.info('No detail data for this Pokemon.')

with pairTab:
    st.caption('Teammate-usage %: each row shows how often the column Pokemon appears alongside it.')
    st.plotly_chart(charts.teammateHeatmap(allDetail), width='stretch')
