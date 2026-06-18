'''
Shared theming for the Streamlit app.

Applies a dark, technical copper-amber palette consistently across pages via a
small CSS injection and exposes the palette constants used by the plotly charts.
'''

import streamlit as st

# Copper-amber dark technical palette
BG = '#1a1e2a'
SURFACE = '#222735'
SURFACE_ALT = '#2b3142'
TEXT = '#e6e8ef'
MUTED = '#9aa0b0'
ACCENT = '#e0975a'        # copper
ACCENT_SOFT = '#f0b988'
GREEN = '#86c06c'         # positive / legal
RED = '#d9755f'           # warning / illegal
BLUE = '#6c9cc0'          # secondary series

# Ordered palette for multi-series plotly charts
SERIES = [ACCENT, GREEN, BLUE, ACCENT_SOFT, '#b08cc0', '#c0b06c']

# Type colours for typing chips / stat context
TYPE_COLORS = {
    'normal': '#9099a1', 'fire': '#e0975a', 'water': '#6c9cc0', 'electric': '#e0c75a',
    'grass': '#86c06c', 'ice': '#8cc0c0', 'fighting': '#c0604a', 'poison': '#a06ca0',
    'ground': '#c0a06c', 'flying': '#9cb0c0', 'psychic': '#d07a9c', 'bug': '#a0b04a',
    'rock': '#b0a070', 'ghost': '#7a6ca0', 'dragon': '#7060c0', 'dark': '#5a5466',
    'steel': '#90a0b0', 'fairy': '#d09cc0',
}

_CSS = f'''
<style>
    .stApp {{ background-color: {BG}; }}
    section[data-testid="stSidebar"] {{ background-color: {SURFACE}; }}
    h1, h2, h3, h4 {{ color: {TEXT}; letter-spacing: 0.2px; }}
    h1 {{ border-bottom: 2px solid {ACCENT}; padding-bottom: 0.3rem; }}
    .stApp, p, span, label, li {{ color: {TEXT}; }}
    a {{ color: {ACCENT_SOFT}; }}
    div[data-testid="stMetricValue"] {{ color: {ACCENT}; }}
    .stButton > button {{
        background-color: {ACCENT}; color: {BG}; border: none;
        border-radius: 6px; font-weight: 600;
    }}
    .stButton > button:hover {{ background-color: {ACCENT_SOFT}; color: {BG}; }}
    .stDownloadButton > button {{
        background-color: {SURFACE_ALT}; color: {TEXT};
        border: 1px solid {ACCENT}; border-radius: 6px;
    }}
</style>
'''


def applyTheme(pageTitle: str, icon: str = '🔴') -> None:
    '''Set page config and inject the shared CSS. Call once at the top of each page.'''
    st.set_page_config(page_title=pageTitle, page_icon=icon, layout='wide')
    st.markdown(_CSS, unsafe_allow_html=True)


def plotlyLayout(height: int = 320) -> dict:
    '''Return a plotly layout dict matching the dark theme.'''
    return {
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'font': {'color': TEXT, 'size': 12},
        'height': height,
        'margin': {'l': 10, 'r': 10, 't': 30, 'b': 10},
        'xaxis': {'gridcolor': SURFACE_ALT, 'zerolinecolor': SURFACE_ALT},
        'yaxis': {'gridcolor': SURFACE_ALT, 'zerolinecolor': SURFACE_ALT},
    }
