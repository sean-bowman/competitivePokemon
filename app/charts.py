'''
Plotly chart helpers for the meta explorer.

All charts return a plotly Figure styled to match the dark copper-amber theme.
Inputs are the {name, pct} lists already present in the committed JSON data.
'''

import plotly.graph_objects as go

from app import theme


def _emptyFigure(message: str) -> go.Figure:
    '''Return a placeholder figure when there is nothing to plot.'''
    fig = go.Figure()
    fig.update_layout(**theme.plotlyLayout(height=160))
    fig.add_annotation(text=message, showarrow=False, font={'color': theme.MUTED})
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)
    return fig


def usageBar(pokemon: list[dict], topN: int = 15) -> go.Figure:
    '''Horizontal bar of usage_pct for the top-N Pokemon in a snapshot.'''
    rows = [p for p in pokemon if p.get('usage_pct') is not None][:topN]
    if not rows:
        return _emptyFigure('No usage data')
    rows = list(reversed(rows))  # highest at top
    names = [p.get('name', '?') for p in rows]
    pcts = [p.get('usage_pct', 0) for p in rows]
    fig = go.Figure(go.Bar(
        x=pcts, y=names, orientation='h',
        marker_color=theme.ACCENT,
        text=[f'{v:.1f}%' for v in pcts], textposition='auto',
    ))
    fig.update_layout(**theme.plotlyLayout(height=max(260, 26 * len(rows))))
    fig.update_xaxes(title='Usage %')
    return fig


def detailBar(entries: list[dict], color: str, height: int = 300) -> go.Figure:
    '''Horizontal bar of a {name, pct} detail list (moves/items/abilities/teammates).'''
    if not entries:
        return _emptyFigure('No data')
    rows = list(reversed(entries))
    names = [e.get('name', '?') for e in rows]
    pcts = [e.get('pct', 0) for e in rows]
    fig = go.Figure(go.Bar(
        x=pcts, y=names, orientation='h',
        marker_color=color,
        text=[f'{v:.1f}%' for v in pcts], textposition='auto',
    ))
    fig.update_layout(**theme.plotlyLayout(height=max(height, 24 * len(rows))))
    fig.update_xaxes(title='%')
    return fig


def statsBar(baseStats: dict) -> go.Figure:
    '''Vertical bar of the six base stats for a PokeAPI profile.'''
    if not baseStats:
        return _emptyFigure('No base stats')
    order = ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
    labels = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']
    values = [baseStats.get(k, 0) for k in order]
    fig = go.Figure(go.Bar(
        x=labels, y=values, marker_color=theme.SERIES[:6],
        text=values, textposition='auto',
    ))
    fig.update_layout(**theme.plotlyLayout(height=260))
    fig.update_yaxes(title='Base stat')
    return fig


def teammateHeatmap(allDetail: dict[str, dict]) -> go.Figure:
    '''
    Heatmap of teammate-usage % across all Pokemon with Champions detail.

    Rows = focal Pokemon, columns = teammate, cell = the teammate's pct in that
    Pokemon's `teammates` list (0 when not listed). Asymmetric by construction.
    '''
    names = sorted(allDetail.keys())
    if not names:
        return _emptyFigure('No teammate data')
    index = {n: i for i, n in enumerate(names)}
    z = [[0.0] * len(names) for _ in names]
    for focal, data in allDetail.items():
        row = index[focal]
        for mate in data.get('teammates', []):
            mateName = mate.get('name')
            if mateName in index:
                z[row][index[mateName]] = mate.get('pct', 0)
    fig = go.Figure(go.Heatmap(
        z=z, x=names, y=names,
        colorscale=[[0, theme.SURFACE], [0.5, theme.ACCENT], [1, theme.ACCENT_SOFT]],
        hovertemplate='%{y} pairs with %{x}: %{z:.1f}%<extra></extra>',
    ))
    layout = theme.plotlyLayout(height=max(420, 22 * len(names)))
    fig.update_layout(**layout)
    fig.update_xaxes(tickangle=-45)
    return fig
