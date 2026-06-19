'''
Pokemon Champions Meta Lab — Streamlit entrypoint.

Run from the repository root:
    streamlit run app/Home.py

Landing page: shows the current meta snapshot status, a top-usage chart, and the
on-demand meta refresh control. The Meta Explorer and Team Builder live under pages/.
'''

import sys
from pathlib import Path

# Put the repo root on the path so `from app import ...` / `from tools import ...`
# resolve when Streamlit launches this file directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st

from app import charts, dataAccess, refresh, theme

theme.applyTheme()

st.title('Pokemon Champions Meta Lab')
st.caption('Interactive meta explorer and team builder for Pokemon Champions VGC.')

snapshot = dataAccess.loadSnapshot(cacheBust=dataAccess.cacheBust())
roster = dataAccess.availableChampionsPokemon(cacheBust=dataAccess.cacheBust())

if snapshot is None:
    st.warning(
        'No meta snapshot found in docs/snapshots/. Use the refresh button below, '
        'or run `python tools/fetch_meta_stats.py --detail`.'
    )
else:
    col1, col2, col3 = st.columns(3)
    col1.metric('Snapshot date', snapshot.get('fetched', '—'))
    col2.metric('Pokemon ranked', len(snapshot.get('pokemon', [])))
    col3.metric('Detailed dataset', f'{len(roster)} Pokemon')
    st.caption(f'Format: {snapshot.get("format", "—")} · source: {snapshot.get("source", "—")}')

st.divider()

left, right = st.columns([3, 2])

with left:
    st.subheader('Top usage')
    if snapshot and snapshot.get('pokemon'):
        st.plotly_chart(charts.usageBar(snapshot['pokemon'], topN=15), width='stretch')
    else:
        st.info('Usage chart appears once a snapshot is available.')

with right:
    st.subheader('Refresh meta data')
    st.caption(
        'Scrapes Pikalytics Champions live and writes a new dated snapshot into '
        'docs/snapshots/ (and per-Pokemon files). Reads use committed data by default.'
    )
    topN = st.slider('Top N Pokemon', min_value=10, max_value=60, value=30, step=5)
    fetchDetail = st.checkbox('Also fetch per-Pokemon detail (slower)', value=True)
    if st.button('Refresh from Pikalytics', width='stretch'):
        with st.spinner('Fetching latest Champions meta…'):
            result = refresh.refreshMeta(topN=topN, fetchDetail=fetchDetail)
        if result['ok']:
            dataAccess.bumpCacheBust()
            st.success(result['message'])
            st.rerun()
        else:
            st.error(result['message'])

    st.markdown(
        '**Navigate:** use the sidebar for the Meta Explorer, Team Builder, and Saved Teams.'
    )

st.divider()
st.caption(
    'Data: Pikalytics (Champions usage), PokeAPI (base stats / learnsets), '
    'Game8 (Champions legality). See README for attribution.'
)
