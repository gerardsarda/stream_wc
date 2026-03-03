"""charts.py — Plotly helpers con estética del Mundial 2026"""
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Paleta base
NAVY   = "#060e1f"
NAVY2  = "#0D1F3C"
GOLD   = "#C9A84C"
GOLD2  = "#F0C040"
BLUE   = "#1A3A6B"
BLUE2  = "#1E4A8A"
MUTED  = "#7A8DAA"
WHITE  = "#EEF2FF"
RED    = "#C0392B"

LAYOUT_BASE = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor ="rgba(0,0,0,0)",
    font=dict(family="Inter, Oswald", color=WHITE, size=12),
    margin=dict(l=10, r=10, t=40, b=10),
    legend=dict(
        bgcolor="rgba(13,31,60,0.7)",
        bordercolor=GOLD,
        borderwidth=1,
        font=dict(color=WHITE, size=11),
    ),
)

def radar_chart(categories, values, player_name, color=GOLD, max_val=100):
    """Radar / Spider chart para estadísticas de jugador o equipo."""
    cats = categories + [categories[0]]
    vals = values + [values[0]]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=vals, theta=cats,
        fill='toself',
        fillcolor=f"rgba(201,168,76,0.12)",
        line=dict(color=color, width=2.5),
        name=player_name,
        hovertemplate="%{theta}: <b>%{r}</b><extra></extra>",
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        polar=dict(
            bgcolor="rgba(13,31,60,0.5)",
            radialaxis=dict(
                visible=True, range=[0, max_val],
                gridcolor="rgba(255,255,255,0.07)",
                linecolor="rgba(255,255,255,0.1)",
                tickfont=dict(color=MUTED, size=9),
                tickcolor=MUTED,
            ),
            angularaxis=dict(
                gridcolor="rgba(255,255,255,0.07)",
                linecolor="rgba(255,255,255,0.1)",
                tickfont=dict(color=WHITE, size=11),
            ),
        ),
        showlegend=False,
        height=380,
    )
    return fig

def radar_comparison(categories, values1, values2, name1, name2, max_val=100):
    """Radar doble para comparar dos jugadores o equipos."""
    cats = categories + [categories[0]]
    v1   = values1 + [values1[0]]
    v2   = values2 + [values2[0]]
    fig  = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=v1, theta=cats, fill='toself', name=name1,
        fillcolor="rgba(201,168,76,0.10)",
        line=dict(color=GOLD2, width=2.5),
        hovertemplate="%{theta}: <b>%{r}</b><extra></extra>",
    ))
    fig.add_trace(go.Scatterpolar(
        r=v2, theta=cats, fill='toself', name=name2,
        fillcolor="rgba(192,57,43,0.10)",
        line=dict(color="#E74C3C", width=2.5),
        hovertemplate="%{theta}: <b>%{r}</b><extra></extra>",
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        polar=dict(
            bgcolor="rgba(13,31,60,0.5)",
            radialaxis=dict(
                visible=True, range=[0, max_val],
                gridcolor="rgba(255,255,255,0.06)",
                linecolor="rgba(255,255,255,0.08)",
                tickfont=dict(color=MUTED, size=9),
            ),
            angularaxis=dict(
                gridcolor="rgba(255,255,255,0.06)",
                linecolor="rgba(255,255,255,0.08)",
                tickfont=dict(color=WHITE, size=11),
            ),
        ),
        showlegend=True,
        height=420,
    )
    return fig

def bar_horizontal(labels, values, title="", color=GOLD):
    fig = go.Figure(go.Bar(
        x=values, y=labels, orientation='h',
        marker=dict(
            color=values,
            colorscale=[[0, BLUE2], [1, GOLD2]],
            showscale=False,
            line=dict(width=0),
        ),
        hovertemplate="%{y}: <b>%{x}</b><extra></extra>",
        text=values, textposition='outside',
        textfont=dict(color=WHITE, size=11),
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text=title, font=dict(color=GOLD, size=14, family="Bebas Neue"), x=0),
        xaxis=dict(
            gridcolor="rgba(255,255,255,0.06)",
            linecolor="rgba(255,255,255,0.08)",
            tickfont=dict(color=MUTED),
            showgrid=True,
        ),
        yaxis=dict(
            gridcolor="rgba(0,0,0,0)",
            tickfont=dict(color=WHITE, size=12),
            autorange="reversed",
        ),
        height=max(280, len(labels) * 40),
    )
    return fig

def bar_grouped(df, x_col, y_cols, names, title=""):
    colors = [GOLD2, "#E74C3C", "#3498DB", "#2ECC71"]
    fig = go.Figure()
    for i, (col, name) in enumerate(zip(y_cols, names)):
        fig.add_trace(go.Bar(
            x=df[x_col], y=df[col], name=name,
            marker_color=colors[i % len(colors)],
            hovertemplate=f"{name}: <b>%{{y}}</b><extra></extra>",
        ))
    fig.update_layout(
        **LAYOUT_BASE,
        barmode='group',
        title=dict(text=title, font=dict(color=GOLD, size=14, family="Bebas Neue"), x=0),
        xaxis=dict(tickfont=dict(color=WHITE), gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(tickfont=dict(color=MUTED), gridcolor="rgba(255,255,255,0.05)"),
        height=320,
    )
    return fig

def pie_donut(labels, values, title=""):
    fig = go.Figure(go.Pie(
        labels=labels, values=values, hole=0.55,
        marker=dict(
            colors=[GOLD2, BLUE2, "#E74C3C", "#2ECC71", "#9B59B6", "#E67E22", "#1ABC9C", MUTED],
            line=dict(color=NAVY, width=2),
        ),
        textfont=dict(color=WHITE, size=12),
        hovertemplate="%{label}: <b>%{value}</b> (%{percent})<extra></extra>",
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text=title, font=dict(color=GOLD, size=14, family="Bebas Neue"), x=0.5),
        height=340,
        showlegend=True,
        legend=dict(
            bgcolor="rgba(13,31,60,0.7)",
            bordercolor=GOLD,
            borderwidth=1,
            font=dict(color=WHITE, size=10),
            orientation="v",
        ),
    )
    return fig

def scatter_xg(teams, xg, xga, names):
    fig = go.Figure()
    fig.add_shape(type="line",
        x0=min(xg)-0.3, y0=min(xg)-0.3,
        x1=max(xg)+0.3, y1=max(xg)+0.3,
        line=dict(color=MUTED, dash="dash", width=1))
    fig.add_trace(go.Scatter(
        x=xg, y=xga, mode='markers+text',
        text=names, textposition='top center',
        textfont=dict(color=WHITE, size=10),
        marker=dict(
            size=14, color=xg,
            colorscale=[[0, BLUE2], [0.5, GOLD], [1, GOLD2]],
            showscale=True,
            colorbar=dict(
                title="xG", titlefont=dict(color=MUTED),
                tickfont=dict(color=MUTED),
                thickness=12,
            ),
            line=dict(color=WHITE, width=1),
        ),
        hovertemplate="<b>%{text}</b><br>xG: %{x:.2f}<br>xGA: %{y:.2f}<extra></extra>",
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        title=dict(text="xG vs xGA por selección", font=dict(color=GOLD, size=14, family="Bebas Neue"), x=0),
        xaxis=dict(title="xG (creación)", titlefont=dict(color=MUTED), tickfont=dict(color=MUTED), gridcolor="rgba(255,255,255,0.06)"),
        yaxis=dict(title="xGA (concedido)", titlefont=dict(color=MUTED), tickfont=dict(color=MUTED), gridcolor="rgba(255,255,255,0.06)"),
        height=380,
    )
    return fig

def line_history(years, values, name="Goles", color=GOLD):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=years, y=values, mode='lines+markers', name=name,
        line=dict(color=color, width=2.5),
        marker=dict(size=7, color=NAVY2, line=dict(color=color, width=2)),
        fill='tozeroy', fillcolor=f"rgba(201,168,76,0.07)",
        hovertemplate=f"{name} %{{x}}: <b>%{{y}}</b><extra></extra>",
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        xaxis=dict(tickfont=dict(color=MUTED), gridcolor="rgba(255,255,255,0.05)"),
        yaxis=dict(tickfont=dict(color=MUTED), gridcolor="rgba(255,255,255,0.05)"),
        height=280,
        showlegend=False,
    )
    return fig

def bar_stat_comparison(categories, val1, val2, name1, name2):
    """Barras horizontales cara a cara para comparar dos jugadores."""
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=categories, x=[-v for v in val1], orientation='h',
        name=name1,
        marker=dict(color=GOLD2, line=dict(width=0)),
        hovertemplate="%{y}: <b>%{customdata}</b><extra></extra>",
        customdata=val1, text=val1,
        textposition='outside', textfont=dict(color=GOLD2),
    ))
    fig.add_trace(go.Bar(
        y=categories, x=val2, orientation='h',
        name=name2,
        marker=dict(color="#E74C3C", line=dict(width=0)),
        hovertemplate="%{y}: <b>%{x}</b><extra></extra>",
        text=val2, textposition='outside',
        textfont=dict(color="#E74C3C"),
    ))
    fig.update_layout(
        **LAYOUT_BASE,
        barmode='relative',
        xaxis=dict(
            tickfont=dict(color=MUTED), gridcolor="rgba(255,255,255,0.05)",
            zeroline=True, zerolinecolor=MUTED, zerolinewidth=1.5,
            showticklabels=False,
        ),
        yaxis=dict(tickfont=dict(color=WHITE, size=11), gridcolor="rgba(0,0,0,0)"),
        height=max(300, len(categories) * 38),
        showlegend=True,
    )
    return fig
