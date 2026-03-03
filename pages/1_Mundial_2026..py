"""
pages/1_⚽_Mundial_2026.py
Sección principal: Partidos, Grupos, Clasificaciones, Premios,
Plantillas y Comparación de jugadores.
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from datetime import datetime

from components.styles import CSS
from components.charts import (
    radar_chart, radar_comparison,
    bar_horizontal, bar_stat_comparison,
)
from data.mock_data import (
    GROUPS, MATCHES, FLAG_MAP, NAME_MAP,
    get_group_standings, STANDINGS,
    TOP_SCORERS, TOP_ASSISTS, CLEAN_SHEETS,
    AWARDS,
    get_squad, get_player_world_cup_stats, get_team_world_cup_stats,
    ALL_TEAMS,
)

st.set_page_config(page_title="Mundial 2026 · Partidos", page_icon="⚽", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────
def pos_emoji(pos):
    return {"POR": "🧤", "DEF": "🛡️", "MED": "⚙️", "DEL": "⚡"}.get(pos, "👤")

def section_header(title, sub=""):
    st.markdown(f"""
    <div class="sec-header">
        <div class="sec-title">{title}</div>
        {"<div class='sec-sub'>"+sub+"</div>" if sub else ""}
    </div>""", unsafe_allow_html=True)

def gold_divider():
    st.markdown('<div class="gold-div"></div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
# TABS PRINCIPALES
# ─────────────────────────────────────────────────────────
tabs = st.tabs([
    "🏟️  PARTIDOS",
    "📊  GRUPOS",
    "🥇  CLASIFICACIONES",
    "🏅  PREMIOS",
    "👕  SELECCIONES",
    "⚖️  COMPARACIÓN",
])

# ══════════════════════════════════════════════════════════
# TAB 1 — PARTIDOS
# ══════════════════════════════════════════════════════════
with tabs[0]:
    section_header("PARTIDOS", "Mundial 2026 · USA · Canadá · México")

    # Filtros
    col_f1, col_f2, col_f3 = st.columns([1, 1, 2])
    with col_f1:
        status_filter = st.selectbox("Estado", ["TODOS", "LIVE", "FT", "NS"])
    with col_f2:
        group_filter  = st.selectbox("Grupo", ["TODOS"] + list(GROUPS.keys()))

    filtered = MATCHES
    if status_filter != "TODOS":
        filtered = [m for m in filtered if m["status"] == status_filter]
    if group_filter != "TODOS":
        filtered = [m for m in filtered if m["group"] == group_filter]

    gold_divider()

    # Agrupar por jornada (grupo)
    by_group = {}
    for m in filtered:
        by_group.setdefault(m["group"], []).append(m)

    if not filtered:
        st.info("No hay partidos con los filtros seleccionados.")

    for grp, matches in sorted(by_group.items()):
        st.markdown(f'<span class="badge badge-group">GRUPO {grp}</span>', unsafe_allow_html=True)
        for m in matches:
            hf  = FLAG_MAP.get(m["home"], "🏳️")
            af  = FLAG_MAP.get(m["away"], "🏳️")
            hn  = NAME_MAP.get(m["home"], m["home"])
            an  = NAME_MAP.get(m["away"], m["away"])
            st_class = m["status"].lower()

            if m["status"] == "FT":
                score_html = f'<div class="match-score">{m["home_score"]} – {m["away_score"]}</div>'
                badge_html = '<span class="badge badge-ft">FT</span>'
            elif m["status"] == "LIVE":
                score_html = f'<div class="match-score live">{m["home_score"]} – {m["away_score"]}</div>'
                badge_html = '<span class="badge badge-live"><span class="live-dot"></span>EN VIVO</span>'
            else:
                score_html = f'<div class="match-score upcoming">{m["date"].strftime("%d %b · %H:%M")}</div>'
                badge_html = '<span class="badge badge-ns">PRÓXIMO</span>'

            st.markdown(f"""
            <div class="match-card {st_class}">
                <div class="match-row">
                    <div class="match-team">
                        <span class="team-flag">{hf}</span>
                        <span class="team-name">{hn}</span>
                    </div>
                    <div class="match-score-box">{score_html}</div>
                    <div class="match-team away">
                        <span class="team-flag">{af}</span>
                        <span class="team-name">{an}</span>
                    </div>
                </div>
                <div class="match-meta">
                    <span>📍 {m['venue']}</span>
                    {badge_html}
                    <span>📅 {m['date'].strftime('%d %b %Y')}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# TAB 2 — GRUPOS Y CLASIFICACIÓN
# ══════════════════════════════════════════════════════════
with tabs[1]:
    section_header("GRUPOS & CLASIFICACIÓN", "Fase de grupos · Mundial 2026")

    # Métricas rápidas
    c1, c2, c3, c4 = st.columns(4)
    played = sum(1 for m in MATCHES if m["status"] == "FT")
    live   = sum(1 for m in MATCHES if m["status"] == "LIVE")
    total  = len(MATCHES)
    goals  = sum((m["home_score"] or 0) + (m["away_score"] or 0) for m in MATCHES if m["home_score"] is not None)
    for col, icon, val, lbl in zip(
        [c1, c2, c3, c4],
        ["🏟️", "🔴", "⚽", "📺"],
        [played, live, goals, total],
        ["PARTIDOS JUGADOS", "EN VIVO", "GOLES TOTALES", "TOTAL PARTIDOS"],
    ):
        col.markdown(f"""
        <div class="stat-card">
            <div class="stat-icon">{icon}</div>
            <div class="stat-n">{val}</div>
            <div class="stat-l">{lbl}</div>
        </div>""", unsafe_allow_html=True)

    gold_divider()

    # Tabla por grupos (2 columnas)
    grp_keys = list(GROUPS.keys())
    for row_start in range(0, len(grp_keys), 2):
        cols = st.columns(2)
        for ci, grp in enumerate(grp_keys[row_start:row_start+2]):
            with cols[ci]:
                st.markdown(f'<div class="group-pill">GRUPO {grp}</div>', unsafe_allow_html=True)
                rows = get_group_standings(grp)
                html = """
                <div class="standings-wrap">
                <table class="standings-table">
                <thead>
                <tr>
                  <th style="width:30px">#</th>
                  <th style="text-align:left">Selección</th>
                  <th>PJ</th><th>V</th><th>E</th><th>D</th>
                  <th>GF</th><th>GC</th><th>DIF</th>
                  <th>TA</th><th>TR</th><th>PTS</th>
                </tr></thead><tbody>
                """
                for i, r in enumerate(rows):
                    pos_n = i + 1
                    q_class = "q-direct" if pos_n <= 2 else ("q-playoff" if pos_n == 3 else "q-out")
                    pos_cls = f"pos-{min(pos_n,4)}"
                    dif_str = f"+{r['dif']}" if r['dif'] > 0 else str(r['dif'])
                    html += f"""
                    <tr class="{q_class}">
                        <td><span class="pos {pos_cls}">{pos_n}</span></td>
                        <td><span style="font-size:1.2rem">{r['flag']}</span>&nbsp; <b>{r['name']}</b></td>
                        <td>{r['pj']}</td><td>{r['v']}</td><td>{r['e']}</td><td>{r['d']}</td>
                        <td>{r['gf']}</td><td>{r['gc']}</td>
                        <td style="color:{'#27ae60' if r['dif']>0 else ('#e74c3c' if r['dif']<0 else '#7A8DAA')};font-weight:600">{dif_str}</td>
                        <td style="color:#F0C040">{r['ta']}</td>
                        <td style="color:#E74C3C">{r['tr']}</td>
                        <td style="font-weight:700;color:#F0C040">{r['pts']}</td>
                    </tr>"""
                html += "</tbody></table></div>"
                html += """
                <div style="font-size:0.68rem;color:#7A8DAA;margin-top:0.4rem;padding:0 0.5rem">
                  <span style="color:#27ae60">■</span> Clasificado directo &nbsp;
                  <span style="color:#C9A84C">■</span> Repesca &nbsp;
                  <span style="color:rgba(255,255,255,0.15)">■</span> Eliminado
                </div>"""
                st.markdown(html, unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════
# TAB 3 — CLASIFICACIONES INDIVIDUALES
# ══════════════════════════════════════════════════════════
with tabs[2]:
    section_header("CLASIFICACIONES", "Máximos goleadores · Asistentes · Porterías imbatidas")

    sub_tabs = st.tabs(["⚽  GOLEADORES", "🎯  ASISTENTES", "🧤  PORTERÍA IMBATIDA"])

    # ── Goleadores ──
    with sub_tabs[0]:
        col_a, col_b = st.columns([3, 2])
        with col_a:
            for p in TOP_SCORERS:
                rank_cls = "top1" if p["rank"] == 1 else ""
                st.markdown(f"""
                <div class="lb-card">
                    <div class="lb-rank {rank_cls}">#{p['rank']}</div>
                    <div class="lb-flag">{p['flag']}</div>
                    <div class="lb-info">
                        <div class="lb-name">{p['player']}</div>
                        <div class="lb-team">{NAME_MAP.get(p['team'], p['team'])}</div>
                    </div>
                    <div style="text-align:right">
                        <div class="lb-val">{p['goals']}</div>
                        <div class="lb-val-l">goles</div>
                        <div style="font-size:0.72rem;color:#7A8DAA">{p['assists']} ast</div>
                    </div>
                </div>""", unsafe_allow_html=True)
        with col_b:
            st.plotly_chart(
                bar_horizontal(
                    [p["player"].split()[-1] for p in TOP_SCORERS],
                    [p["goals"] for p in TOP_SCORERS],
                    title="⚽ Goles en el torneo",
                ),
                use_container_width=True,
            )

    # ── Asistentes ──
    with sub_tabs[1]:
        col_a, col_b = st.columns([3, 2])
        with col_a:
            for p in TOP_ASSISTS:
                rank_cls = "top1" if p["rank"] == 1 else ""
                st.markdown(f"""
                <div class="lb-card">
                    <div class="lb-rank {rank_cls}">#{p['rank']}</div>
                    <div class="lb-flag">{p['flag']}</div>
                    <div class="lb-info">
                        <div class="lb-name">{p['player']}</div>
                        <div class="lb-team">{NAME_MAP.get(p['team'], p['team'])}</div>
                    </div>
                    <div style="text-align:right">
                        <div class="lb-val">{p['assists']}</div>
                        <div class="lb-val-l">asist.</div>
                        <div style="font-size:0.72rem;color:#7A8DAA">{p['goals']} goles</div>
                    </div>
                </div>""", unsafe_allow_html=True)
        with col_b:
            st.plotly_chart(
                bar_horizontal(
                    [p["player"].split()[-1] for p in TOP_ASSISTS],
                    [p["assists"] for p in TOP_ASSISTS],
                    title="🎯 Asistencias en el torneo",
                ),
                use_container_width=True,
            )

    # ── Porterías ──
    with sub_tabs[2]:
        col_a, col_b = st.columns([3, 2])
        with col_a:
            for p in CLEAN_SHEETS:
                rank_cls = "top1" if p["rank"] == 1 else ""
                st.markdown(f"""
                <div class="lb-card">
                    <div class="lb-rank {rank_cls}">#{p['rank']}</div>
                    <div class="lb-flag">{p['flag']}</div>
                    <div class="lb-info">
                        <div class="lb-name">{p['player']}</div>
                        <div class="lb-team">{NAME_MAP.get(p['team'], p['team'])}</div>
                    </div>
                    <div style="text-align:right">
                        <div class="lb-val">{p['cs']}</div>
                        <div class="lb-val-l">portería</div>
                        <div style="font-size:0.72rem;color:#7A8DAA">{p['saves']} paradas</div>
                    </div>
                </div>""", unsafe_allow_html=True)
        with col_b:
            st.plotly_chart(
                bar_horizontal(
                    [p["player"].split()[-1] for p in CLEAN_SHEETS],
                    [p["cs"] for p in CLEAN_SHEETS],
                    title="🧤 Porterías imbatidas",
                ),
                use_container_width=True,
            )

# ══════════════════════════════════════════════════════════
# TAB 4 — PREMIOS
# ══════════════════════════════════════════════════════════
with tabs[3]:
    section_header("PREMIOS DEL MUNDIAL", "Reconocimientos individuales · FIFA World Cup 2026")

    award_defs = [
        ("bota_oro",     "👟 BOTA DE ORO",    "Máximo goleador del torneo"),
        ("mvp",          "⭐ MVP",             "Mejor jugador del mundial"),
        ("mejor_portero","🧤 MEJOR PORTERO",   "Guante de Oro FIFA"),
        ("mejor_joven",  "🌟 MEJOR JOVEN",     "Jugador sub-21 más destacado"),
    ]

    cols = st.columns(4)
    for col, (key, tit, desc) in zip(cols, award_defs):
        a = AWARDS[key]
        with col:
            st.markdown(f"""
            <div class="award-card">
                <div class="award-icon">{tit.split()[0]}</div>
                <div class="award-tit">{' '.join(tit.split()[1:])}</div>
                <div style="font-size:0.7rem;color:#7A8DAA;letter-spacing:2px;margin-bottom:0.5rem">{desc}</div>
                <div class="award-flag">{a['flag']}</div>
                <div class="award-name">{a['player']}</div>
                <div class="award-team">{a['team']}</div>
                <div class="award-stat">{a['stat']}</div>
                <div style="font-size:0.72rem;color:#7A8DAA;margin-top:0.4rem">{a['extra']}</div>
            </div>""", unsafe_allow_html=True)

    gold_divider()

    # Tabla resumen
    st.markdown('<div class="sec-title" style="font-size:1.4rem">TABLA RESUMEN</div>', unsafe_allow_html=True)
    df_awards = pd.DataFrame([
        {"Premio": "Bota de Oro", "Jugador": AWARDS["bota_oro"]["player"],
         "Selección": AWARDS["bota_oro"]["team"], "Estadística": AWARDS["bota_oro"]["stat"]},
        {"Premio": "MVP", "Jugador": AWARDS["mvp"]["player"],
         "Selección": AWARDS["mvp"]["team"], "Estadística": AWARDS["mvp"]["stat"]},
        {"Premio": "Mejor Portero", "Jugador": AWARDS["mejor_portero"]["player"],
         "Selección": AWARDS["mejor_portero"]["team"], "Estadística": AWARDS["mejor_portero"]["stat"]},
        {"Premio": "Mejor Joven", "Jugador": AWARDS["mejor_joven"]["player"],
         "Selección": AWARDS["mejor_joven"]["team"], "Estadística": AWARDS["mejor_joven"]["stat"]},
    ])
    st.dataframe(df_awards, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════
# TAB 5 — SELECCIONES CONVOCADAS
# ══════════════════════════════════════════════════════════
with tabs[4]:
    section_header("SELECCIONES CONVOCADAS", "Plantillas y estadísticas del mundial")

    all_team_opts = {
        f"{FLAG_MAP.get(c,'🏳️')} {NAME_MAP.get(c, c)}": c
        for grp in GROUPS.values() for t in grp
        for c in [t["code"]]
    }
    sel_label = st.selectbox("Seleccionar selección", list(all_team_opts.keys()))
    sel_code  = all_team_opts[sel_label]
    sel_flag  = FLAG_MAP.get(sel_code, "🏳️")
    sel_name  = NAME_MAP.get(sel_code, sel_code)

    gold_divider()

    # Cabecera de selección
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:1.5rem;margin-bottom:1.5rem;
                background:var(--card);border:1px solid var(--border);
                border-radius:16px;padding:1.5rem 2rem;">
        <div style="font-size:5rem;line-height:1">{sel_flag}</div>
        <div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:2.5rem;
                        letter-spacing:4px;background:linear-gradient(90deg,#C9A84C,#F0C040);
                        -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                        background-clip:text">{sel_name.upper()}</div>
            <div style="color:#7A8DAA;font-size:0.8rem;letter-spacing:3px;text-transform:uppercase">
                FIFA WORLD CUP 2026 · PLANTILLA OFICIAL</div>
        </div>
    </div>""", unsafe_allow_html=True)

    team_tabs = st.tabs(["👕  PLANTILLA", "📈  ESTADÍSTICAS DEL MUNDIAL"])

    # ── Plantilla ──
    with team_tabs[0]:
        squad = get_squad(sel_code)
        pos_order = ["POR", "DEF", "MED", "DEL"]
        pos_labels = {"POR": "🧤 PORTEROS", "DEF": "🛡️ DEFENSAS",
                      "MED": "⚙️ CENTROCAMPISTAS", "DEL": "⚡ DELANTEROS"}

        for pos in pos_order:
            players_pos = [p for p in squad if p["pos"] == pos]
            if not players_pos:
                continue
            st.markdown(f"""
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;
                        letter-spacing:3px;color:var(--gold);margin:1rem 0 0.6rem">
                {pos_labels[pos]}
            </div>""", unsafe_allow_html=True)

            cols_p = st.columns(min(len(players_pos), 4))
            for i, player in enumerate(players_pos):
                with cols_p[i % 4]:
                    wc_stats = get_player_world_cup_stats(player["name"], pos)
                    if pos == "DEL":
                        sv1, sl1 = wc_stats.get("goles", 0), "GOL"
                        sv2, sl2 = wc_stats.get("asistencias", 0), "AST"
                        sv3, sl3 = wc_stats.get("remates", 0), "REM"
                    elif pos == "MED":
                        sv1, sl1 = wc_stats.get("goles", 0), "GOL"
                        sv2, sl2 = wc_stats.get("asistencias", 0), "AST"
                        sv3, sl3 = wc_stats.get("pases_clave", 0), "PK"
                    elif pos == "DEF":
                        sv1, sl1 = wc_stats.get("duelos_ganados", 0), "DUE"
                        sv2, sl2 = wc_stats.get("intercepciones", 0), "INT"
                        sv3, sl3 = wc_stats.get("goles", 0), "GOL"
                    else:
                        sv1, sl1 = wc_stats.get("paradas", 0), "PAR"
                        sv2, sl2 = wc_stats.get("porterias_imbatidas", 0), "PI"
                        sv3, sl3 = round(wc_stats.get("porcentaje_paradas", 0), 0), "%"

                    st.markdown(f"""
                    <div class="player-card">
                        <div class="player-num">{player['number']}</div>
                        <div class="player-avatar">{pos_emoji(pos)}</div>
                        <div class="player-name">{player['name']}</div>
                        <span class="player-pos pos-{pos}">{pos}</span>
                        <div class="player-club">{player['club']}</div>
                        <div class="p-stats">
                            <div class="p-s-item">
                                <div class="p-s-v">{sv1}</div>
                                <div class="p-s-l">{sl1}</div>
                            </div>
                            <div class="p-s-item">
                                <div class="p-s-v">{sv2}</div>
                                <div class="p-s-l">{sl2}</div>
                            </div>
                            <div class="p-s-item">
                                <div class="p-s-v">{sv3}</div>
                                <div class="p-s-l">{sl3}</div>
                            </div>
                        </div>
                    </div>""", unsafe_allow_html=True)

                    # Detalle del jugador en expander
                    with st.expander(f"📊 Stats avanzadas · {player['name']}"):
                        st.markdown(f"**Partidos jugados:** {wc_stats.get('partidos', 0)}")
                        if pos == "DEL":
                            cats = ["Goles", "Asistencias", "xG", "Remates", "Al arco", "Regates", "Tq. área"]
                            vals = [
                                min(wc_stats.get("goles", 0)*10, 100),
                                min(wc_stats.get("asistencias", 0)*15, 100),
                                min(wc_stats.get("xG", 0)*20, 100),
                                min(wc_stats.get("remates", 0)*7, 100),
                                min(wc_stats.get("remates_puerta", 0)*12, 100),
                                min(wc_stats.get("regates_exitosos", 0)*9, 100),
                                min(wc_stats.get("toques_area", 0)*4, 100),
                            ]
                        elif pos == "MED":
                            cats = ["Goles", "Asistencias", "Pases clave", "Recup.", "xA", "Km/partido", "Presión"]
                            vals = [
                                min(wc_stats.get("goles", 0)*20, 100),
                                min(wc_stats.get("asistencias", 0)*15, 100),
                                min(wc_stats.get("pases_clave", 0)*10, 100),
                                min(wc_stats.get("recuperaciones", 0)*8, 100),
                                min(wc_stats.get("xA", 0)*30, 100),
                                min(wc_stats.get("km_recorridos", 0)*8, 100),
                                min(wc_stats.get("presiones", 0)*3, 100),
                            ]
                        elif pos == "DEF":
                            cats = ["Duelos", "Intercep.", "Despejes", "Pases %", "Aéreos", "Presión", "Goles"]
                            vals = [
                                min(wc_stats.get("duelos_ganados", 0)*5, 100),
                                min(wc_stats.get("intercepciones", 0)*10, 100),
                                min(wc_stats.get("despejes", 0)*7, 100),
                                wc_stats.get("pases_completados", 0),
                                min(wc_stats.get("duelos_aereos", 0)*9, 100),
                                wc_stats.get("presion_exitosa", 0),
                                min(wc_stats.get("goles", 0)*30, 100),
                            ]
                        else:
                            cats = ["Paradas", "% Paradas", "Goles encaj.", "xG-parado", "Salidas", "P. imbat.", "Dist. jueg."]
                            vals = [
                                min(wc_stats.get("paradas", 0)*7, 100),
                                wc_stats.get("porcentaje_paradas", 0),
                                max(0, 100 - wc_stats.get("goles_recibidos", 0)*20),
                                80,
                                min(wc_stats.get("salidas", 0)*12, 100),
                                min(wc_stats.get("porterias_imbatidas", 0)*40, 100),
                                65,
                            ]
                        st.plotly_chart(
                            radar_chart(cats, vals, player["name"]),
                            use_container_width=True,
                        )
                        st.json(wc_stats, expanded=False)

    # ── Stats del equipo en el Mundial ──
    with team_tabs[1]:
        ts = get_team_world_cup_stats(sel_code)

        # KPIs
        k1, k2, k3, k4, k5, k6 = st.columns(6)
        for col, icon, val, lbl in zip(
            [k1, k2, k3, k4, k5, k6],
            ["🏆", "✅", "⚽", "🛡️", "📐", "🎯"],
            [ts["victorias"], ts["victorias"], ts["goles_favor"], ts["goles_contra"],
             ts["posesion"], ts["xG"]],
            ["VICTORIAS", "JUGADOS", "GOLES", "EN CONTRA", "POSESIÓN %", "xG TOTAL"],
        ):
            col.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">{icon}</div>
                <div class="stat-n">{val}</div>
                <div class="stat-l">{lbl}</div>
            </div>""", unsafe_allow_html=True)

        gold_divider()

        col_r, col_b2 = st.columns([1, 1])
        with col_r:
            # Radar del equipo
            cats = ["xG", "Posesión", "Pases%", "Duelos%", "Remates", "Presión alta", "Km/partido"]
            vals = [
                min(ts["xG"]*10, 100),
                ts["posesion"],
                ts["pases_completados"],
                ts["duelos_ganados"],
                min(ts["remates_partido"]*5, 100),
                ts["presion_alta"],
                min(ts["km_partido"]-100, 100),
            ]
            st.markdown('<div class="radar-wrap">', unsafe_allow_html=True)
            st.plotly_chart(radar_chart(cats, vals, sel_name), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_b2:
            stats_df = pd.DataFrame({
                "Métrica": ["xG", "xGA", "Posesión %", "Pases comp. %",
                             "Presión alta %", "Duelos gan. %",
                             "Remates/partido", "km/partido"],
                "Valor": [ts["xG"], ts["xGA"], ts["posesion"], ts["pases_completados"],
                           ts["presion_alta"], ts["duelos_ganados"],
                           ts["remates_partido"], ts["km_partido"]],
            })
            st.dataframe(stats_df, use_container_width=True, hide_index=True)
            st.markdown("<br>", unsafe_allow_html=True)
            # Resultado del grupo
            g_rows = get_group_standings(
                next(g for g, teams in GROUPS.items()
                     if any(t["code"] == sel_code for t in teams))
            )
            g_df = pd.DataFrame([
                {"Pos": i+1, "Selección": r["flag"]+" "+r["name"],
                 "PJ": r["pj"], "V": r["v"], "E": r["e"], "D": r["d"],
                 "GF": r["gf"], "GC": r["gc"], "Dif": r["dif"], "Pts": r["pts"]}
                for i, r in enumerate(g_rows)
            ])
            st.caption("📊 Clasificación de grupo")
            st.dataframe(g_df, use_container_width=True, hide_index=True)

# ══════════════════════════════════════════════════════════
# TAB 6 — COMPARACIÓN DE JUGADORES
# ══════════════════════════════════════════════════════════
with tabs[5]:
    section_header("COMPARACIÓN DE JUGADORES", "Estadísticas cara a cara · Mundial 2026")

    # Filtros
    cf1, cf2, cf3 = st.columns(3)
    with cf1:
        pos_filter = st.selectbox("Filtrar por posición", ["TODAS", "POR", "DEF", "MED", "DEL"])
    with cf2:
        team_filter_label = st.selectbox("Filtrar por selección",
            ["TODAS"] + [f"{FLAG_MAP.get(c,'🏳️')} {NAME_MAP.get(c,c)}"
                         for grp in GROUPS.values() for t in grp for c in [t["code"]]])
    with cf3:
        search_q = st.text_input("Buscar jugador", placeholder="Ej: Messi, Mbappé...")

    # Construir lista de todos los jugadores
    all_players = []
    for grp in GROUPS.values():
        for t in grp:
            for p in get_squad(t["code"]):
                all_players.append({**p, "team_code": t["code"],
                                     "team_name": t["name"], "team_flag": t["flag"]})

    # Aplicar filtros
    fp = all_players
    if pos_filter != "TODAS":
        fp = [p for p in fp if p["pos"] == pos_filter]
    if team_filter_label != "TODAS":
        t_code = next((t["code"] for grp in GROUPS.values()
                       for t in grp
                       if f"{FLAG_MAP.get(t['code'],'🏳️')} {NAME_MAP.get(t['code'],t['code'])}" == team_filter_label), None)
        if t_code:
            fp = [p for p in fp if p["team_code"] == t_code]
    if search_q:
        fp = [p for p in fp if search_q.lower() in p["name"].lower()]

    player_names = [f"{p['team_flag']} {p['name']} ({p['team_name']})" for p in fp]

    if len(player_names) < 2:
        st.warning("Necesitas al menos 2 jugadores disponibles para comparar. Ajusta los filtros.")
    else:
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            sel_p1 = st.selectbox("Jugador 1", player_names, key="cmp_p1")
        with col_s2:
            default_idx = min(1, len(player_names)-1)
            sel_p2 = st.selectbox("Jugador 2", player_names, index=default_idx, key="cmp_p2")

        p1 = fp[player_names.index(sel_p1)]
        p2 = fp[player_names.index(sel_p2)]
        s1 = get_player_world_cup_stats(p1["name"], p1["pos"])
        s2 = get_player_world_cup_stats(p2["name"], p2["pos"])

        gold_divider()

        # Header visual
        st.markdown(f"""
        <div class="cmp-header">
            <div class="cmp-player">
                <div class="cmp-player-flag">{p1['team_flag']}</div>
                <div class="cmp-player-name">{p1['name']}</div>
                <div class="cmp-player-team">{p1['team_name']}</div>
                <span class="player-pos pos-{p1['pos']}">{p1['pos']}</span>
            </div>
            <div class="cmp-vs">VS</div>
            <div class="cmp-player">
                <div class="cmp-player-flag">{p2['team_flag']}</div>
                <div class="cmp-player-name">{p2['name']}</div>
                <div class="cmp-player-team">{p2['team_name']}</div>
                <span class="player-pos pos-{p2['pos']}">{p2['pos']}</span>
            </div>
        </div>""", unsafe_allow_html=True)

        # Radar comparativo
        shared_cats = ["Goles", "Asistencias", "Participación", "Duelos", "Técnica", "Físico", "Impacto"]

        def norm_stats(s, pos):
            if pos == "DEL":
                return [
                    min(s.get("goles", 0)*12, 100),
                    min(s.get("asistencias", 0)*15, 100),
                    min((s.get("goles", 0)+s.get("asistencias", 0))*8, 100),
                    min(s.get("remates", 0)*6, 100),
                    min(s.get("regates_exitosos", 0)*8, 100),
                    min(s.get("toques_area", 0)*4, 100),
                    min(s.get("xG", 0)*15, 100),
                ]
            elif pos == "MED":
                return [
                    min(s.get("goles", 0)*20, 100),
                    min(s.get("asistencias", 0)*15, 100),
                    min(s.get("pases_clave", 0)*10, 100),
                    min(s.get("recuperaciones", 0)*7, 100),
                    min(s.get("xA", 0)*35, 100),
                    min(s.get("km_recorridos", 0)*8, 100),
                    min(s.get("presiones", 0)*3, 100),
                ]
            elif pos == "DEF":
                return [
                    min(s.get("goles", 0)*30, 100),
                    min(s.get("asistencias", 0)*20, 100),
                    min(s.get("duelos_ganados", 0)*5, 100),
                    min(s.get("intercepciones", 0)*10, 100),
                    s.get("presion_exitosa", 0),
                    min(s.get("despejes", 0)*7, 100),
                    min(s.get("duelos_aereos", 0)*9, 100),
                ]
            else:
                return [
                    max(0, 100 - s.get("goles_recibidos", 0)*25),
                    min(s.get("porterias_imbatidas", 0)*45, 100),
                    s.get("porcentaje_paradas", 0),
                    min(s.get("paradas", 0)*7, 100),
                    min(s.get("salidas", 0)*12, 100),
                    80, 70,
                ]

        v1 = norm_stats(s1, p1["pos"])
        v2 = norm_stats(s2, p2["pos"])

        col_radar, col_bars = st.columns([1, 1])
        with col_radar:
            st.plotly_chart(
                radar_comparison(shared_cats, v1, v2, p1["name"], p2["name"]),
                use_container_width=True,
            )
        with col_bars:
            cats_short = [c[:8] for c in shared_cats]
            st.plotly_chart(
                bar_stat_comparison(cats_short, v1, v2, p1["name"], p2["name"]),
                use_container_width=True,
            )

        # Tabla numérica
        gold_divider()
        st.caption("📋 Estadísticas numéricas completas")
        all_keys = set(list(s1.keys()) + list(s2.keys()))
        cmp_data = []
        for k in sorted(all_keys):
            cmp_data.append({
                "Métrica": k.replace("_", " ").title(),
                p1["name"]: s1.get(k, "—"),
                p2["name"]: s2.get(k, "—"),
            })
        st.dataframe(pd.DataFrame(cmp_data), use_container_width=True, hide_index=True)

# Footer
st.markdown('<div class="footer">⚽ Mundial 2026 · USA · Canadá · México · 11 Jun – 19 Jul 2026</div>', unsafe_allow_html=True)
