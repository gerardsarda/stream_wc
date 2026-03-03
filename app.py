"""
app.py — Página principal (Home) de la app Mundial 2026.
Ejecutar con:  streamlit run app.py
"""
import streamlit as st
from components.styles import CSS
from data.mock_data import (
    MATCHES, GROUPS, FLAG_MAP, NAME_MAP,
    TOP_SCORERS, STANDINGS, get_group_standings,
)

st.set_page_config(
    page_title="Mundial 2026 · Home",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo">
        <div style="font-size:3rem">🏆</div>
        <div class="sidebar-logo-title">MUNDIAL<br>2026</div>
        <div class="sidebar-logo-sub">USA · Canadá · México</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="nav-section">NAVEGACIÓN</div>', unsafe_allow_html=True)
    st.page_link("app.py",                                label="🏠  Inicio")
    st.page_link("pages/1_Mundial_2026.py",               label="⚽  Mundial 2026")
    st.page_link("pages/2_Estadisticas_Historicas.py",    label="📜  Historia")

    st.markdown('<div class="nav-section" style="margin-top:1rem">EN VIVO</div>', unsafe_allow_html=True)
    live = [m for m in MATCHES if m["status"] == "LIVE"]
    if live:
        for m in live:
            hf = FLAG_MAP.get(m["home"], "🏳️")
            af = FLAG_MAP.get(m["away"], "🏳️")
            st.markdown(f"""
            <div style="background:rgba(192,57,43,0.15);border:1px solid rgba(192,57,43,0.3);
                        border-radius:10px;padding:0.6rem 0.8rem;margin-bottom:0.4rem">
                <div style="font-size:0.65rem;letter-spacing:2px;color:#E74C3C;
                            text-transform:uppercase;margin-bottom:3px">
                    <span class="live-dot"></span> EN VIVO
                </div>
                <div style="font-family:'Oswald',sans-serif;font-size:0.9rem">
                    {hf} {m['home_score']} – {m['away_score']} {af}
                </div>
            </div>""", unsafe_allow_html=True)
    else:
        st.markdown('<div style="color:var(--muted);font-size:0.8rem;padding:0.5rem 1rem">No hay partidos en vivo</div>', unsafe_allow_html=True)

    st.markdown('<div class="nav-section" style="margin-top:1rem">INFO</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="color:var(--muted);font-size:0.72rem;padding:0 1rem;line-height:1.8">
        📅 11 Jun – 19 Jul 2026<br>
        🏟️ 16 estadios<br>
        🌍 48 selecciones<br>
        ⚽ 104 partidos<br>
        <span style="opacity:0.5;font-size:0.65rem">Datos de ejemplo</span>
    </div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-ball">🏆</div>
    <div class="hero-title">FIFA WORLD CUP</div>
    <div class="hero-sub">The Greatest Show on Earth</div>
    <div class="hero-dates">11 JUNIO — 19 JULIO 2026</div>
    <div class="hero-hosts">🇺🇸 Estados Unidos &nbsp;·&nbsp; 🇨🇦 Canadá &nbsp;·&nbsp; 🇲🇽 México</div>
    <div class="hero-stats">
        <div class="hero-stat">
            <div class="hero-stat-n">48</div>
            <div class="hero-stat-l">Selecciones</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-n">104</div>
            <div class="hero-stat-l">Partidos</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-n">16</div>
            <div class="hero-stat-l">Estadios</div>
        </div>
        <div class="hero-stat">
            <div class="hero-stat-n">39</div>
            <div class="hero-stat-l">Días</div>
        </div>
    </div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# STATS RÁPIDAS
# ─────────────────────────────────────────────────────────
played = sum(1 for m in MATCHES if m["status"] == "FT")
live_c = sum(1 for m in MATCHES if m["status"] == "LIVE")
goals  = sum(
    (m["home_score"] or 0) + (m["away_score"] or 0)
    for m in MATCHES if m["home_score"] is not None
)
ns = sum(1 for m in MATCHES if m["status"] == "NS")

c1, c2, c3, c4 = st.columns(4)
for col, icon, val, lbl in zip(
    [c1, c2, c3, c4],
    ["🏟️", "🔴", "⚽", "📅"],
    [played, live_c, goals, ns],
    ["PARTIDOS JUGADOS", "EN VIVO", "GOLES MARCADOS", "PRÓXIMOS"],
):
    col.markdown(f"""
    <div class="stat-card">
        <div class="stat-icon">{icon}</div>
        <div class="stat-n">{val}</div>
        <div class="stat-l">{lbl}</div>
    </div>""", unsafe_allow_html=True)

st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# ÚLTIMOS RESULTADOS + PRÓXIMOS PARTIDOS
# ─────────────────────────────────────────────────────────
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("""
    <div style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;
                letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">
        ÚLTIMOS RESULTADOS
    </div>""", unsafe_allow_html=True)

    recent = [m for m in MATCHES if m["status"] in ("FT", "LIVE")][-6:]
    for m in reversed(recent):
        hf = FLAG_MAP.get(m["home"], "🏳️")
        af = FLAG_MAP.get(m["away"], "🏳️")
        hn = NAME_MAP.get(m["home"], m["home"])
        an = NAME_MAP.get(m["away"], m["away"])
        if m["status"] == "LIVE":
            badge = '<span class="badge badge-live"><span class="live-dot"></span> LIVE</span>'
            score_cls = "live"
        else:
            badge = '<span class="badge badge-ft">FT</span>'
            score_cls = ""

        st.markdown(f"""
        <div class="match-card" style="padding:0.9rem 1.2rem">
            <div class="match-row">
                <div class="match-team">
                    <span class="team-flag">{hf}</span>
                    <span class="team-name" style="font-size:0.95rem">{hn}</span>
                </div>
                <div class="match-score-box" style="min-width:80px;padding:0.3rem 0.8rem">
                    <div class="match-score {score_cls}" style="font-size:1.6rem">
                        {m['home_score']} – {m['away_score']}
                    </div>
                </div>
                <div class="match-team away">
                    <span class="team-flag">{af}</span>
                    <span class="team-name" style="font-size:0.95rem">{an}</span>
                </div>
            </div>
            <div class="match-meta">
                <span style="font-size:0.68rem">Grupo {m['group']}</span>
                {badge}
                <span style="font-size:0.68rem">{m['date'].strftime('%d %b')}</span>
            </div>
        </div>""", unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;
                letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">
        PRÓXIMOS PARTIDOS
    </div>""", unsafe_allow_html=True)

    upcoming = [m for m in MATCHES if m["status"] == "NS"][:6]
    for m in upcoming:
        hf = FLAG_MAP.get(m["home"], "🏳️")
        af = FLAG_MAP.get(m["away"], "🏳️")
        hn = NAME_MAP.get(m["home"], m["home"])
        an = NAME_MAP.get(m["away"], m["away"])
        st.markdown(f"""
        <div class="match-card upcoming" style="padding:0.9rem 1.2rem">
            <div class="match-row">
                <div class="match-team">
                    <span class="team-flag">{hf}</span>
                    <span class="team-name" style="font-size:0.95rem">{hn}</span>
                </div>
                <div class="match-score-box" style="min-width:90px;padding:0.4rem 0.8rem;
                     background:rgba(26,58,107,0.4)">
                    <div class="match-score upcoming">
                        {m['date'].strftime('%d %b')}<br>{m['date'].strftime('%H:%M')}
                    </div>
                </div>
                <div class="match-team away">
                    <span class="team-flag">{af}</span>
                    <span class="team-name" style="font-size:0.95rem">{an}</span>
                </div>
            </div>
            <div class="match-meta">
                <span style="font-size:0.68rem">Grupo {m['group']}</span>
                <span class="badge badge-ns">PRÓXIMO</span>
                <span style="font-size:0.68rem">📍 {m['venue'].split(',')[0]}</span>
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# TOP GOLEADORES + LÍDERES DE GRUPO
# ─────────────────────────────────────────────────────────
col_g1, col_g2 = st.columns([1, 2])

with col_g1:
    st.markdown("""
    <div style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;
                letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">
        ⚽ TOP GOLEADORES
    </div>""", unsafe_allow_html=True)
    for p in TOP_SCORERS[:5]:
        rank_cls = "top1" if p["rank"] == 1 else ""
        st.markdown(f"""
        <div class="lb-card" style="padding:0.7rem 1rem">
            <div class="lb-rank {rank_cls}" style="font-size:1.4rem;min-width:28px">
                #{p['rank']}
            </div>
            <div class="lb-flag" style="font-size:1.6rem">{p['flag']}</div>
            <div class="lb-info">
                <div class="lb-name" style="font-size:0.9rem">{p['player']}</div>
                <div class="lb-team">{NAME_MAP.get(p['team'], p['team'])}</div>
            </div>
            <div style="text-align:right">
                <div class="lb-val" style="font-size:1.6rem">{p['goals']}</div>
                <div class="lb-val-l">⚽</div>
            </div>
        </div>""", unsafe_allow_html=True)

with col_g2:
    st.markdown("""
    <div style="font-family:'Bebas Neue',sans-serif;font-size:1.4rem;
                letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">
        🏆 LÍDERES DE GRUPO
    </div>""", unsafe_allow_html=True)
    grp_list = list(GROUPS.keys())
    leader_cols = st.columns(3)
    for i, grp in enumerate(grp_list):
        with leader_cols[i % 3]:
            leader = get_group_standings(grp)[0]
            st.markdown(f"""
            <div style="background:var(--card);border:1px solid var(--border);
                        border-radius:12px;padding:0.9rem;text-align:center;margin-bottom:0.5rem">
                <div style="font-size:0.65rem;letter-spacing:3px;color:var(--gold);
                            text-transform:uppercase;margin-bottom:0.3rem">GRUPO {grp}</div>
                <div style="font-size:2rem">{leader['flag']}</div>
                <div style="font-family:'Oswald',sans-serif;font-size:0.88rem;
                            letter-spacing:1px;color:var(--white)">{leader['name']}</div>
                <div style="font-family:'Bebas Neue',sans-serif;font-size:1.2rem;
                            color:var(--gold2)">{leader['pts']} PTS</div>
            </div>""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
    ⚽ FIFA World Cup 2026 · USA · Canadá · México · 11 Jun – 19 Jul 2026<br>
    <span style="font-size:0.65rem;opacity:0.5">
        App de demostración · Datos ficticios · Desarrollado con Streamlit + Plotly
    </span>
</div>""", unsafe_allow_html=True)
