"""
pages/2_📜_Estadísticas_Históricas.py
Historia mundialista, rankings históricos, selecciones con
estadísticas avanzadas y comparación de juego entre equipos.
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd

from components.styles import CSS
from components.charts import (
    radar_chart, radar_comparison,
    bar_horizontal, pie_donut,
    scatter_xg, line_history,
)
from data.mock_data import (
    GROUPS, FLAG_MAP, NAME_MAP,
    WORLD_CUP_HISTORY, TITLES_RANKING, HISTORIC_SCORERS,
    get_squad, get_team_last10_stats, get_player_season_stats,
    ALL_TEAMS,
)

st.set_page_config(page_title="Estadísticas Históricas", page_icon="📜", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────
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
    "🏆  HISTORIA MUNDIALISTA",
    "🌍  SELECCIONES",
    "⚖️  COMPARAR SELECCIONES",
])

# ══════════════════════════════════════════════════════════
# TAB 1 — HISTORIA MUNDIALISTA
# ══════════════════════════════════════════════════════════
with tabs[0]:
    section_header("HISTORIA MUNDIALISTA", "Todos los mundiales FIFA · 1930 – 2022")

    hist_tabs = st.tabs([
        "🥇  CAMPEONES",
        "📊  RANKING TÍTULOS",
        "⚽  GOLEADORES HISTÓRICOS",
        "📈  EVOLUCIÓN",
    ])

    # ── Campeones ──
    with hist_tabs[0]:
        col_l, col_r = st.columns([2, 1])
        with col_l:
            st.markdown('<div style="font-family:\'Bebas Neue\',sans-serif;font-size:1.2rem;letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">TODOS LOS MUNDIALES</div>', unsafe_allow_html=True)
            for wc in WORLD_CUP_HISTORY:
                # Buscar bandera del campeón
                champ_flag = next(
                    (t["flag"] for grp in GROUPS.values()
                     for t in grp if t["name"] == wc["champion"]), "🏆"
                )
                runner_flag = next(
                    (t["flag"] for grp in GROUPS.values()
                     for t in grp if t["name"] == wc["runner_up"]), "🥈"
                )
                st.markdown(f"""
                <div class="hist-card">
                    <div class="hist-year">{wc['year']}</div>
                    <div style="flex:1">
                        <div class="hist-champ">{champ_flag} {wc['champion']} 🏆</div>
                        <div class="hist-det">
                            🥈 {runner_flag} {wc['runner_up']} &nbsp;·&nbsp;
                            📍 {wc['host']} &nbsp;·&nbsp;
                            ⚽ {wc['goals']} goles &nbsp;·&nbsp;
                            🏟️ {wc['matches']} partidos &nbsp;·&nbsp;
                            🌍 {wc['teams']} selecciones
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)

        with col_r:
            # Campeones más frecuentes
            champion_counts = {}
            for wc in WORLD_CUP_HISTORY:
                champion_counts[wc["champion"]] = champion_counts.get(wc["champion"], 0) + 1
            sorted_champs = sorted(champion_counts.items(), key=lambda x: -x[1])
            labels  = [c[0] for c in sorted_champs]
            values  = [c[1] for c in sorted_champs]
            st.plotly_chart(pie_donut(labels, values, "Mundiales ganados"), use_container_width=True)

    # ── Ranking títulos ──
    with hist_tabs[1]:
        max_t = TITLES_RANKING[0]["titles"]
        col_main, col_side = st.columns([2, 1])
        with col_main:
            for tr in TITLES_RANKING:
                pct = tr["titles"] / max_t * 100
                st.markdown(f"""
                <div style="margin-bottom:1rem">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
                        <span style="font-family:'Oswald',sans-serif;font-size:1rem;letter-spacing:1px">
                            {tr['flag']} {tr['team']}
                        </span>
                        <span style="font-family:'Bebas Neue',sans-serif;font-size:1.2rem;color:var(--gold2)">
                            {tr['titles']} {'🏆' * tr['titles']}
                        </span>
                    </div>
                    <div class="title-bar-bg">
                        <div class="title-bar-fill" style="width:{pct}%"></div>
                    </div>
                    <div style="font-size:0.68rem;color:var(--muted);margin-top:2px;letter-spacing:1px">{tr['years']}</div>
                </div>""", unsafe_allow_html=True)

        with col_side:
            st.plotly_chart(
                bar_horizontal(
                    [r["flag"]+" "+r["team"] for r in TITLES_RANKING],
                    [r["titles"] for r in TITLES_RANKING],
                    title="🏆 Títulos mundiales",
                ),
                use_container_width=True,
            )

    # ── Goleadores históricos ──
    with hist_tabs[2]:
        col_a, col_b = st.columns([3, 2])
        with col_a:
            st.markdown('<div style="font-family:\'Bebas Neue\',sans-serif;font-size:1.2rem;letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">TOP GOLEADORES HISTÓRICOS</div>', unsafe_allow_html=True)
            for p in HISTORIC_SCORERS:
                rank_cls = "top1" if p["rank"] == 1 else ""
                st.markdown(f"""
                <div class="lb-card">
                    <div class="lb-rank {rank_cls}">#{p['rank']}</div>
                    <div class="lb-flag">{p['flag']}</div>
                    <div class="lb-info">
                        <div class="lb-name">{p['player']}</div>
                        <div class="lb-team">{p['years']} · {p['editions']} ed.</div>
                    </div>
                    <div style="text-align:right">
                        <div class="lb-val">{p['goals']}</div>
                        <div class="lb-val-l">goles</div>
                    </div>
                </div>""", unsafe_allow_html=True)

        with col_b:
            st.plotly_chart(
                bar_horizontal(
                    [p["player"].split()[-1] for p in HISTORIC_SCORERS],
                    [p["goals"] for p in HISTORIC_SCORERS],
                    title="⚽ Goles históricos",
                ),
                use_container_width=True,
            )

    # ── Evolución ──
    with hist_tabs[3]:
        years   = [wc["year"] for wc in reversed(WORLD_CUP_HISTORY)]
        goals   = [wc["goals"] for wc in reversed(WORLD_CUP_HISTORY)]
        matches = [wc["matches"] for wc in reversed(WORLD_CUP_HISTORY)]

        st.markdown("**⚽ Goles totales por Mundial**")
        st.plotly_chart(line_history(years, goals, "Goles"), use_container_width=True)

        col_e1, col_e2 = st.columns(2)
        with col_e1:
            st.markdown("**🏟️ Partidos por edición**")
            st.plotly_chart(line_history(years, matches, "Partidos", color="#3498DB"), use_container_width=True)
        with col_e2:
            goals_per_match = [round(g/m, 2) for g, m in zip(goals, matches)]
            st.markdown("**📊 Goles por partido**")
            st.plotly_chart(line_history(years, goals_per_match, "G/partido", color="#E74C3C"), use_container_width=True)

        # Tabla completa
        gold_divider()
        df_hist = pd.DataFrame(WORLD_CUP_HISTORY)
        df_hist["goles_partido"] = (df_hist["goals"] / df_hist["matches"]).round(2)
        st.dataframe(
            df_hist.rename(columns={
                "year":"Año","champion":"Campeón","runner_up":"Subcampeón",
                "host":"Sede","goals":"Goles","teams":"Equipos",
                "matches":"Partidos","goles_partido":"G/Partido"
            }),
            use_container_width=True, hide_index=True,
        )

# ══════════════════════════════════════════════════════════
# TAB 2 — SELECCIONES
# ══════════════════════════════════════════════════════════
with tabs[1]:
    section_header("SELECCIONES", "Estadísticas avanzadas · Últimos 10 partidos oficiales")

    all_team_opts = {
        f"{FLAG_MAP.get(t['code'],'🏳️')} {t['name']}": t["code"]
        for grp in GROUPS.values() for t in grp
    }
    sel_label = st.selectbox("Seleccionar selección", list(all_team_opts.keys()), key="hist_team")
    sel_code  = all_team_opts[sel_label]
    sel_flag  = FLAG_MAP.get(sel_code, "🏳️")
    sel_name  = NAME_MAP.get(sel_code, sel_code)

    gold_divider()

    # Header
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
                Últimos 10 partidos oficiales · Estadísticas avanzadas</div>
        </div>
    </div>""", unsafe_allow_html=True)

    sel_sub = st.tabs(["📈  CÓMO JUEGA", "👤  JUGADORES"])

    # ── Cómo juega ──
    with sel_sub[0]:
        ts = get_team_last10_stats(sel_code)

        # KPIs
        kp_cols = st.columns(5)
        kpi_data = [
            ("✅", ts["victorias"], "VICTORIAS"),
            ("➖", ts["empates"], "EMPATES"),
            ("❌", ts["derrotas"], "DERROTAS"),
            ("⚽", ts["goles_favor"], "GOLES MARCADOS"),
            ("🛡️", ts["goles_contra"], "GOLES CONCEDIDOS"),
        ]
        for col, (icon, val, lbl) in zip(kp_cols, kpi_data):
            col.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">{icon}</div>
                <div class="stat-n">{val}</div>
                <div class="stat-l">{lbl}</div>
            </div>""", unsafe_allow_html=True)

        gold_divider()

        col_r, col_m = st.columns([1, 1])
        with col_r:
            cats = [
                "xG/partido", "Posesión", "Pases comp.%",
                "Presión alta", "Duelos gan.", "Remates/P",
                "km/partido", "xGA/P",
            ]
            vals = [
                min(ts["xG_promedio"]*25, 100),
                ts["posesion"],
                ts["pases_completados"],
                ts["presion_alta"],
                ts["duelos_ganados"],
                min(ts["remates_partido"]*5, 100),
                min((ts["km_partido"]-100)*10, 100),
                max(0, 100 - ts["xGA_promedio"]*30),
            ]
            st.markdown('<div class="radar-wrap">', unsafe_allow_html=True)
            st.plotly_chart(radar_chart(cats, vals, sel_name), use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with col_m:
            st.markdown('<div style="font-family:\'Bebas Neue\',sans-serif;font-size:1.1rem;letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">MÉTRICAS AVANZADAS</div>', unsafe_allow_html=True)
            metrics = [
                ("📐 xG promedio/partido", ts["xG_promedio"]),
                ("🛡️ xGA promedio/partido", ts["xGA_promedio"]),
                ("⚽ Posesión media %", ts["posesion"]),
                ("🎯 Pases completados %", ts["pases_completados"]),
                ("💪 Presión alta %", ts["presion_alta"]),
                ("🤼 Duelos ganados %", ts["duelos_ganados"]),
                ("🎯 Remates/partido", ts["remates_partido"]),
                ("🏹 Remates a puerta/P", ts["remates_puerta"]),
                ("🏃 km recorridos/P", ts["km_partido"]),
                ("⚠️ Faltas/partido", ts["faltas"]),
            ]
            for label, val in metrics:
                bar_pct = min(float(val) / 120 * 100, 100)
                st.markdown(f"""
                <div style="margin-bottom:0.7rem">
                    <div style="display:flex;justify-content:space-between;margin-bottom:3px">
                        <span style="font-size:0.85rem;color:var(--light)">{label}</span>
                        <span style="font-family:'Bebas Neue',sans-serif;font-size:1rem;color:var(--gold2)">{val}</span>
                    </div>
                    <div style="background:rgba(255,255,255,0.06);border-radius:4px;height:5px">
                        <div style="width:{bar_pct}%;height:100%;border-radius:4px;
                                    background:linear-gradient(90deg,#1E4A8A,#C9A84C)"></div>
                    </div>
                </div>""", unsafe_allow_html=True)

            # Zonas de ataque
            gold_divider()
            st.markdown('<div style="font-family:\'Bebas Neue\',sans-serif;font-size:1rem;letter-spacing:3px;color:var(--gold);margin-bottom:0.8rem">ZONAS DE ATAQUE</div>', unsafe_allow_html=True)
            zc1, zc2, zc3 = st.columns(3)
            for col, zone, val, color in zip(
                [zc1, zc2, zc3],
                ["◀ BANDA IZQ", "▲ CENTRO", "BANDA DER ▶"],
                [ts["ataques_izquierda"], ts["ataques_centro"], ts["ataques_derecha"]],
                ["#3498DB", "#F0C040", "#E74C3C"],
            ):
                col.markdown(f"""
                <div style="text-align:center;background:rgba(13,31,60,0.6);
                            border:1px solid rgba(255,255,255,0.08);border-radius:12px;padding:1rem">
                    <div style="font-family:'Bebas Neue',sans-serif;font-size:2rem;color:{color}">{val}%</div>
                    <div style="font-size:0.68rem;letter-spacing:2px;color:var(--muted);text-transform:uppercase">{zone}</div>
                </div>""", unsafe_allow_html=True)

    # ── Jugadores ──
    with sel_sub[1]:
        squad = get_squad(sel_code)
        pos_order  = ["POR", "DEF", "MED", "DEL"]
        pos_labels = {"POR": "🧤 PORTEROS", "DEF": "🛡️ DEFENSAS",
                      "MED": "⚙️ CENTROCAMPISTAS", "DEL": "⚡ DELANTEROS"}

        for pos in pos_order:
            players_pos = [p for p in squad if p["pos"] == pos]
            if not players_pos:
                continue
            st.markdown(f"""
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.1rem;
                        letter-spacing:3px;color:var(--gold);margin:1.2rem 0 0.6rem">
                {pos_labels[pos]}
            </div>""", unsafe_allow_html=True)

            for player in players_pos:
                season_stats = get_player_season_stats(player["name"], pos)
                with st.expander(f"{player['flag']} {player['name']}  ·  {player['club']}  ·  {pos}  ·  {player['age']} años"):
                    ep1, ep2 = st.columns([1, 2])
                    with ep1:
                        st.markdown(f"""
                        <div style="background:var(--card);border:1px solid var(--border);
                                    border-radius:12px;padding:1.5rem;text-align:center">
                            <div style="font-size:3.5rem">{'🧤' if pos=='POR' else '🛡️' if pos=='DEF' else '⚙️' if pos=='MED' else '⚡'}</div>
                            <div style="font-family:'Oswald',sans-serif;font-size:1.1rem;
                                        letter-spacing:1px;color:var(--white);margin-top:0.5rem">{player['name']}</div>
                            <span class="player-pos pos-{pos}">{pos}</span>
                            <div style="color:var(--muted);font-size:0.8rem;margin-top:0.4rem">{player['club']}</div>
                            <div style="margin-top:1rem;display:grid;grid-template-columns:1fr 1fr;gap:0.5rem">
                                <div style="background:rgba(255,255,255,0.05);border-radius:8px;padding:0.6rem;text-align:center">
                                    <div style="font-family:'Bebas Neue';font-size:1.4rem;color:var(--gold2)">{season_stats['partidos']}</div>
                                    <div style="font-size:0.6rem;color:var(--muted);letter-spacing:1px">PARTIDOS</div>
                                </div>
                                <div style="background:rgba(255,255,255,0.05);border-radius:8px;padding:0.6rem;text-align:center">
                                    <div style="font-family:'Bebas Neue';font-size:1.4rem;color:var(--gold2)">{season_stats['goles']}</div>
                                    <div style="font-size:0.6rem;color:var(--muted);letter-spacing:1px">GOLES</div>
                                </div>
                                <div style="background:rgba(255,255,255,0.05);border-radius:8px;padding:0.6rem;text-align:center">
                                    <div style="font-family:'Bebas Neue';font-size:1.4rem;color:var(--gold2)">{season_stats['asistencias']}</div>
                                    <div style="font-size:0.6rem;color:var(--muted);letter-spacing:1px">ASIST.</div>
                                </div>
                                <div style="background:rgba(255,255,255,0.05);border-radius:8px;padding:0.6rem;text-align:center">
                                    <div style="font-family:'Bebas Neue';font-size:1.4rem;color:var(--gold2)">{season_stats['xG']}</div>
                                    <div style="font-size:0.6rem;color:var(--muted);letter-spacing:1px">xG</div>
                                </div>
                            </div>
                        </div>""", unsafe_allow_html=True)

                    with ep2:
                        cats = ["Goles", "Asistencias", "xG", "xA",
                                "Pases clave", "Duelos", "Regates", "Recuper."]
                        vals = [
                            min(season_stats["goles"] * 3, 100),
                            min(season_stats["asistencias"] * 6, 100),
                            min(season_stats["xG"] * 4, 100),
                            min(season_stats["xA"] * 8, 100),
                            min(season_stats["pases_clave"] * 0.8, 100),
                            season_stats["duelos_ganados"],
                            min(season_stats["regates_exitosos"] * 0.8, 100),
                            min(season_stats["recuperaciones"] * 0.7, 100),
                        ]
                        st.plotly_chart(
                            radar_chart(cats, vals, player["name"]),
                            use_container_width=True,
                        )

                    # Métricas numéricas
                    mc = st.columns(4)
                    extra_metrics = [
                        ("xG", season_stats["xG"]),
                        ("xA", season_stats["xA"]),
                        ("Km/P", season_stats["km_partido"]),
                        ("Presión %", season_stats["presion_exitosa"]),
                    ]
                    for col, (k, v) in zip(mc, extra_metrics):
                        col.metric(k, v)

# ══════════════════════════════════════════════════════════
# TAB 3 — COMPARAR SELECCIONES
# ══════════════════════════════════════════════════════════
with tabs[2]:
    section_header("COMPARAR SELECCIONES", "Cara a cara · Estadísticas avanzadas · Últimos 10 partidos")

    cc1, cc2 = st.columns(2)
    all_team_list = [
        f"{FLAG_MAP.get(t['code'],'🏳️')} {t['name']}"
        for grp in GROUPS.values() for t in grp
    ]
    all_codes = [
        t["code"]
        for grp in GROUPS.values() for t in grp
    ]

    with cc1:
        t1_label = st.selectbox("Selección 1", all_team_list, key="cmp_t1", index=0)
    with cc2:
        t2_label = st.selectbox("Selección 2", all_team_list, key="cmp_t2", index=1)

    t1_code = all_codes[all_team_list.index(t1_label)]
    t2_code = all_codes[all_team_list.index(t2_label)]
    t1_flag = FLAG_MAP.get(t1_code, "🏳️")
    t2_flag = FLAG_MAP.get(t2_code, "🏳️")
    t1_name = NAME_MAP.get(t1_code, t1_code)
    t2_name = NAME_MAP.get(t2_code, t2_code)

    ts1 = get_team_last10_stats(t1_code)
    ts2 = get_team_last10_stats(t2_code)

    gold_divider()

    # Cabecera visual
    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr auto 1fr;
                align-items:center;gap:1rem;padding:1.5rem 2rem;
                background:var(--card);border:1px solid var(--border);
                border-radius:16px;margin-bottom:1.5rem">
        <div style="text-align:center">
            <div style="font-size:4rem">{t1_flag}</div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;
                        letter-spacing:3px;color:var(--gold2)">{t1_name.upper()}</div>
        </div>
        <div style="font-family:'Bebas Neue',sans-serif;font-size:3rem;
                    color:var(--gold);letter-spacing:3px;text-align:center">VS</div>
        <div style="text-align:center">
            <div style="font-size:4rem">{t2_flag}</div>
            <div style="font-family:'Bebas Neue',sans-serif;font-size:1.8rem;
                        letter-spacing:3px;color:#E74C3C">{t2_name.upper()}</div>
        </div>
    </div>""", unsafe_allow_html=True)

    # Radar comparativo
    cats_team = [
        "xG/P", "xGA/P", "Posesión",
        "Pases%", "Presión alta", "Duelos gan.",
        "Remates/P", "km/P",
    ]
    v_t1 = [
        min(ts1["xG_promedio"]*25, 100),
        max(0, 100 - ts1["xGA_promedio"]*30),
        ts1["posesion"],
        ts1["pases_completados"],
        ts1["presion_alta"],
        ts1["duelos_ganados"],
        min(ts1["remates_partido"]*5, 100),
        min((ts1["km_partido"]-100)*10, 100),
    ]
    v_t2 = [
        min(ts2["xG_promedio"]*25, 100),
        max(0, 100 - ts2["xGA_promedio"]*30),
        ts2["posesion"],
        ts2["pases_completados"],
        ts2["presion_alta"],
        ts2["duelos_ganados"],
        min(ts2["remates_partido"]*5, 100),
        min((ts2["km_partido"]-100)*10, 100),
    ]

    col_r2, col_xg = st.columns([1, 1])
    with col_r2:
        st.markdown('<div class="radar-wrap">', unsafe_allow_html=True)
        st.plotly_chart(
            radar_comparison(cats_team, v_t1, v_t2, t1_name, t2_name),
            use_container_width=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col_xg:
        # Scatter xG para todas las selecciones
        all_codes_list = [t["code"] for grp in GROUPS.values() for t in grp]
        xg_vals  = [get_team_last10_stats(c)["xG_promedio"] for c in all_codes_list]
        xga_vals = [get_team_last10_stats(c)["xGA_promedio"] for c in all_codes_list]
        names_xg = [FLAG_MAP.get(c,"🏳️")+" "+NAME_MAP.get(c,c) for c in all_codes_list]
        st.plotly_chart(scatter_xg(all_codes_list, xg_vals, xga_vals, names_xg), use_container_width=True)

    gold_divider()

    # Tabla comparativa
    cmp_rows = [
        {"Métrica": "Victorias (últ. 10)", t1_name: ts1["victorias"], t2_name: ts2["victorias"]},
        {"Métrica": "Empates",             t1_name: ts1["empates"],   t2_name: ts2["empates"]},
        {"Métrica": "Derrotas",            t1_name: ts1["derrotas"],  t2_name: ts2["derrotas"]},
        {"Métrica": "Goles marcados",      t1_name: ts1["goles_favor"],  t2_name: ts2["goles_favor"]},
        {"Métrica": "Goles encajados",     t1_name: ts1["goles_contra"], t2_name: ts2["goles_contra"]},
        {"Métrica": "xG promedio",         t1_name: ts1["xG_promedio"],  t2_name: ts2["xG_promedio"]},
        {"Métrica": "xGA promedio",        t1_name: ts1["xGA_promedio"], t2_name: ts2["xGA_promedio"]},
        {"Métrica": "Posesión %",          t1_name: ts1["posesion"],     t2_name: ts2["posesion"]},
        {"Métrica": "Pases completados %", t1_name: ts1["pases_completados"], t2_name: ts2["pases_completados"]},
        {"Métrica": "Presión alta %",      t1_name: ts1["presion_alta"],  t2_name: ts2["presion_alta"]},
        {"Métrica": "Duelos ganados %",    t1_name: ts1["duelos_ganados"],"**"+t2_name: ts2["duelos_ganados"]},
        {"Métrica": "Remates/partido",     t1_name: ts1["remates_partido"], t2_name: ts2["remates_partido"]},
        {"Métrica": "Remates a puerta/P",  t1_name: ts1["remates_puerta"],  t2_name: ts2["remates_puerta"]},
        {"Métrica": "km recorridos/P",     t1_name: ts1["km_partido"],   t2_name: ts2["km_partido"]},
        {"Métrica": "Faltas/partido",      t1_name: ts1["faltas"],       t2_name: ts2["faltas"]},
        {"Métrica": "Ataques banda izq.",  t1_name: ts1["ataques_izquierda"], t2_name: ts2["ataques_izquierda"]},
        {"Métrica": "Ataques centro",      t1_name: ts1["ataques_centro"],    t2_name: ts2["ataques_centro"]},
        {"Métrica": "Ataques banda der.",  t1_name: ts1["ataques_derecha"],   t2_name: ts2["ataques_derecha"]},
    ]
    # Fix column name typo
    cmp_rows = [{k.replace("**",""):v for k,v in r.items()} for r in cmp_rows]
    st.dataframe(pd.DataFrame(cmp_rows), use_container_width=True, hide_index=True)

# Footer
st.markdown('<div class="footer">📜 Estadísticas Históricas · Mundial 2026 · FIFA</div>', unsafe_allow_html=True)
