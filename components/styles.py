"""styles.py — CSS global de la app Mundial 2026"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&family=Oswald:wght@400;500;600;700&display=swap');

/* ─── VARIABLES ─── */
:root {
    --gold:     #C9A84C;
    --gold2:    #F0C040;
    --red:      #C0392B;
    --navy:     #060e1f;
    --navy2:    #0D1F3C;
    --navy3:    #122244;
    --blue:     #1A3A6B;
    --blue2:    #1E4A8A;
    --accent:   #E63946;
    --light:    #EEF2FF;
    --muted:    #7A8DAA;
    --white:    #FFFFFF;
    --card:     rgba(13,31,60,0.80);
    --border:   rgba(201,168,76,0.22);
    --border-h: rgba(201,168,76,0.55);
}

/* ─── GLOBAL ─── */
html, body, [class*="css"], .stApp {
    font-family: 'Inter', sans-serif !important;
    color: var(--light);
}

.stApp {
    background: radial-gradient(ellipse at 20% 10%, #0a1832 0%, #060e1f 50%, #07121e 100%);
    min-height: 100vh;
}

/* Ruido sutil */
.stApp::after {
    content: '';
    position: fixed; inset: 0;
    background-image:
        radial-gradient(circle at 80% 80%, rgba(201,168,76,0.03) 0%, transparent 50%),
        radial-gradient(circle at 20% 20%, rgba(30,74,138,0.05) 0%, transparent 50%);
    pointer-events: none; z-index: 0;
}

/* ─── SIDEBAR ─── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #040b17 0%, #060e1f 60%, #040b17 100%) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] * { color: var(--light) !important; }

.sidebar-logo {
    text-align: center;
    padding: 1.5rem 0 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.2rem;
}

.sidebar-logo-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.2rem;
    letter-spacing: 5px;
    background: linear-gradient(135deg, var(--gold), var(--gold2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1.1;
}

.sidebar-logo-sub {
    font-size: 0.68rem; letter-spacing: 4px;
    text-transform: uppercase; color: var(--muted) !important;
    margin-top: 0.2rem;
}

.nav-section {
    font-family: 'Oswald', sans-serif;
    font-size: 0.65rem; letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--gold) !important;
    padding: 0.8rem 1rem 0.3rem;
    opacity: 0.7;
}

/* ─── HEADINGS ─── */
h1, h2, h3 { font-family: 'Bebas Neue', sans-serif !important; letter-spacing: 2px !important; }
h1 { font-size: 2.8rem !important; }
h2 { font-size: 2rem !important; }
h3 { font-size: 1.4rem !important; }

/* ─── SECTION HEADER ─── */
.sec-header { margin-bottom: 1.5rem; }
.sec-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.4rem; letter-spacing: 5px; line-height: 1;
    background: linear-gradient(90deg, var(--gold) 0%, #fff 55%, var(--gold2) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; text-transform: uppercase; margin: 0;
}
.sec-sub {
    font-size: 0.72rem; letter-spacing: 4px; text-transform: uppercase;
    color: var(--muted); margin-top: 0.25rem;
    border-left: 3px solid var(--gold); padding-left: 10px;
}

/* ─── HERO ─── */
.hero {
    background: linear-gradient(135deg,
        rgba(6,14,31,0.95) 0%,
        rgba(18,34,68,0.85) 50%,
        rgba(6,14,31,0.95) 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 3rem 2rem 2.5rem;
    text-align: center;
    position: relative; overflow: hidden;
    margin-bottom: 2rem;
}
.hero::before {
    content: '🏆';
    position: absolute; font-size: 14rem; opacity: 0.035;
    left: -2rem; top: -2rem; transform: rotate(-15deg);
    filter: grayscale(1);
}
.hero::after {
    content: '⚽';
    position: absolute; font-size: 10rem; opacity: 0.035;
    right: -1rem; bottom: -2rem; transform: rotate(20deg);
}
.hero-ball { font-size: 3rem; margin-bottom: 0.5rem; }
.hero-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 5rem; letter-spacing: 10px; line-height: 1;
    background: linear-gradient(90deg, var(--gold) 0%, #fff 40%, var(--gold2) 70%, var(--gold) 100%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text; margin: 0;
}
.hero-sub {
    font-size: 0.85rem; letter-spacing: 7px; text-transform: uppercase;
    color: var(--muted); margin: 0.3rem 0 0.8rem;
}
.hero-dates {
    font-family: 'Oswald', sans-serif; font-size: 1.1rem;
    letter-spacing: 3px; font-weight: 600;
    background: linear-gradient(90deg, var(--gold), var(--gold2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-hosts {
    color: var(--muted); font-size: 0.8rem;
    letter-spacing: 3px; text-transform: uppercase; margin-top: 0.5rem;
}
.hero-stats {
    display: flex; gap: 2rem; justify-content: center;
    margin-top: 1.5rem; flex-wrap: wrap;
}
.hero-stat {
    text-align: center;
    padding: 0.8rem 1.5rem;
    background: rgba(255,255,255,0.04);
    border: 1px solid var(--border); border-radius: 10px;
}
.hero-stat-n {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem; letter-spacing: 2px; color: var(--gold2);
}
.hero-stat-l { font-size: 0.65rem; letter-spacing: 2px; color: var(--muted); text-transform: uppercase; }

/* ─── MATCH CARD ─── */
.match-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.2rem 1.5rem 1rem;
    margin-bottom: 0.8rem;
    backdrop-filter: blur(12px);
    position: relative; overflow: hidden;
    transition: transform 0.25s, border-color 0.25s, box-shadow 0.25s;
}
.match-card:hover {
    border-color: var(--border-h);
    transform: translateY(-2px);
    box-shadow: 0 10px 36px rgba(0,0,0,0.35);
}
.match-card::before {
    content: ''; position: absolute;
    left: 0; top: 0; bottom: 0; width: 4px;
    background: linear-gradient(180deg, var(--gold), var(--gold2));
    border-radius: 4px 0 0 4px;
}
.match-card.live::before { background: linear-gradient(180deg, var(--red), #ff6b6b); }
.match-card.upcoming::before { background: linear-gradient(180deg, var(--blue), var(--blue2)); }

.match-row {
    display: flex; align-items: center;
    justify-content: space-between; gap: 1rem;
}
.match-team {
    display: flex; align-items: center;
    gap: 0.75rem; flex: 1;
}
.match-team.away { flex-direction: row-reverse; }
.team-flag { font-size: 2.2rem; line-height: 1; }
.team-name {
    font-family: 'Oswald', sans-serif;
    font-size: 1.05rem; letter-spacing: 1px; color: var(--white);
}
.match-score-box {
    min-width: 110px; text-align: center;
    background: linear-gradient(135deg, rgba(26,58,107,0.9), rgba(30,74,138,0.7));
    border: 1px solid var(--border); border-radius: 12px;
    padding: 0.5rem 1rem;
}
.match-score {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.2rem; letter-spacing: 4px; color: var(--white);
    line-height: 1;
}
.match-score.live { color: #ff6b6b; }
.match-score.upcoming { font-size: 0.85rem; letter-spacing: 2px; color: var(--muted); }

.live-dot {
    display: inline-block; width: 8px; height: 8px;
    background: var(--red); border-radius: 50%;
    animation: blink 1.4s infinite;
    margin-right: 4px; vertical-align: middle;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.2} }

.match-meta {
    display: flex; justify-content: space-between; align-items: center;
    margin-top: 0.6rem; font-size: 0.72rem;
    color: var(--muted); letter-spacing: 1px;
}
.badge {
    font-size: 0.62rem; font-weight: 700; letter-spacing: 2px;
    padding: 2px 10px; border-radius: 20px; text-transform: uppercase;
}
.badge-live    { background: var(--red); color: #fff; animation: blink 1.4s infinite; }
.badge-ft      { background: rgba(255,255,255,0.1); color: var(--muted); }
.badge-ns      { background: rgba(30,74,138,0.5); color: #7fb3ff; border: 1px solid rgba(30,74,138,0.8); }
.badge-group   { background: rgba(201,168,76,0.15); color: var(--gold); border: 1px solid rgba(201,168,76,0.3); }

/* ─── STANDINGS ─── */
.standings-wrap {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px; overflow: hidden;
    backdrop-filter: blur(10px);
}
.standings-table { width: 100%; border-collapse: collapse; }
.standings-table th {
    background: rgba(201,168,76,0.08);
    color: var(--gold);
    font-family: 'Oswald', sans-serif;
    font-size: 0.72rem; letter-spacing: 2px;
    text-transform: uppercase; padding: 0.7rem 0.8rem;
    text-align: center; border-bottom: 1px solid var(--border);
}
.standings-table th:first-child { text-align: left; padding-left: 1rem; }
.standings-table td {
    padding: 0.65rem 0.8rem; text-align: center;
    font-size: 0.88rem; border-bottom: 1px solid rgba(255,255,255,0.04);
    transition: background 0.2s;
}
.standings-table td:first-child { text-align: left; padding-left: 1rem; }
.standings-table tr:last-child td { border-bottom: none; }
.standings-table tr:hover td { background: rgba(201,168,76,0.05); }
.standings-table tr.q-direct td { border-left: 3px solid #27ae60; }
.standings-table tr.q-playoff td { border-left: 3px solid var(--gold); }
.standings-table tr.q-out td { border-left: 3px solid rgba(255,255,255,0.1); }

.pos {
    display: inline-flex; align-items: center; justify-content: center;
    width: 26px; height: 26px; border-radius: 7px;
    font-family: 'Oswald', sans-serif; font-weight: 700; font-size: 0.85rem;
}
.pos-1 { background: linear-gradient(135deg,#C9A84C,#F0C040); color:#000; }
.pos-2 { background: linear-gradient(135deg,#95A5A6,#BDC3C7); color:#000; }
.pos-3 { background: linear-gradient(135deg,#CD7F32,#E59866); color:#000; }
.pos-4 { background: rgba(255,255,255,0.08); color: var(--muted); }

.group-pill {
    display: inline-block;
    background: linear-gradient(90deg, var(--gold), var(--gold2));
    color: #000; font-family: 'Bebas Neue', sans-serif;
    font-size: 1.1rem; letter-spacing: 4px;
    padding: 0.3rem 1rem; border-radius: 8px;
    margin-bottom: 0.8rem;
}

/* ─── STAT CARD ─── */
.stat-card {
    background: var(--card);
    border: 1px solid var(--border); border-radius: 14px;
    padding: 1.5rem 1rem; text-align: center;
    backdrop-filter: blur(10px);
    transition: all 0.25s;
}
.stat-card:hover {
    border-color: var(--border-h); transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.3);
}
.stat-icon { font-size: 2rem; margin-bottom: 0.4rem; }
.stat-n {
    font-family: 'Bebas Neue', sans-serif; font-size: 3rem; line-height: 1;
    background: linear-gradient(135deg, var(--gold), var(--gold2));
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    background-clip: text;
}
.stat-l { font-size: 0.7rem; letter-spacing: 2px; color: var(--muted); text-transform: uppercase; margin-top: 0.3rem; }

/* ─── LEADERBOARD CARD ─── */
.lb-card {
    background: var(--card);
    border: 1px solid var(--border); border-radius: 12px;
    padding: 0.85rem 1.2rem;
    display: flex; align-items: center; gap: 1rem;
    margin-bottom: 0.5rem; transition: all 0.25s;
    backdrop-filter: blur(10px);
}
.lb-card:hover { border-color: var(--border-h); transform: translateX(4px); }
.lb-rank {
    font-family: 'Bebas Neue', sans-serif; font-size: 1.8rem;
    color: var(--gold); min-width: 35px; line-height: 1;
}
.lb-rank.top1 { font-size: 2.2rem; color: var(--gold2); }
.lb-flag { font-size: 2rem; }
.lb-info { flex: 1; }
.lb-name { font-family: 'Oswald', sans-serif; font-size: 1rem; letter-spacing: 1px; color: var(--white); }
.lb-team { font-size: 0.72rem; letter-spacing: 2px; color: var(--muted); text-transform: uppercase; }
.lb-val {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2rem; color: var(--gold2); line-height: 1; min-width: 40px; text-align: right;
}
.lb-val-l { font-size: 0.65rem; color: var(--muted); letter-spacing: 1px; text-align: right; text-transform: uppercase; }

/* ─── AWARD CARD ─── */
.award-card {
    background: linear-gradient(135deg,
        rgba(13,31,60,0.92) 0%,
        rgba(20,45,90,0.8) 100%);
    border: 1px solid rgba(201,168,76,0.35);
    border-radius: 18px; padding: 2rem 1.5rem;
    text-align: center; position: relative; overflow: hidden;
    transition: all 0.3s;
}
.award-card::before {
    content: ''; position: absolute; inset: 0;
    background: radial-gradient(circle at 50% 0%,rgba(201,168,76,0.07) 0%,transparent 65%);
}
.award-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 60px rgba(201,168,76,0.15);
    border-color: rgba(201,168,76,0.65);
}
.award-icon { font-size: 3.5rem; margin-bottom: 0.6rem; }
.award-tit {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.15rem; letter-spacing: 3px;
    color: var(--gold); text-transform: uppercase;
}
.award-flag { font-size: 2rem; margin: 0.6rem 0; }
.award-name {
    font-family: 'Oswald', sans-serif;
    font-size: 1.3rem; color: var(--white); letter-spacing: 1px;
}
.award-team { color: var(--muted); font-size: 0.75rem; letter-spacing: 3px; text-transform: uppercase; }
.award-stat {
    display: inline-block; margin-top: 0.8rem;
    background: rgba(201,168,76,0.12);
    border: 1px solid rgba(201,168,76,0.3);
    color: var(--gold2); font-size: 0.82rem; letter-spacing: 1px;
    padding: 4px 14px; border-radius: 20px;
}

/* ─── PLAYER CARD ─── */
.player-card {
    background: var(--card);
    border: 1px solid var(--border); border-radius: 14px;
    padding: 1.5rem 1.2rem; text-align: center;
    backdrop-filter: blur(10px); transition: all 0.3s;
    position: relative; overflow: hidden; height: 100%;
}
.player-card:hover {
    border-color: var(--border-h); transform: translateY(-4px);
    box-shadow: 0 16px 48px rgba(0,0,0,0.35);
}
.player-card::after {
    content: ''; position: absolute;
    bottom: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}
.player-avatar {
    width: 76px; height: 76px; border-radius: 50%;
    background: linear-gradient(135deg, var(--blue), var(--blue2));
    display: flex; align-items: center; justify-content: center;
    font-size: 2.4rem; margin: 0 auto 0.9rem;
    border: 2px solid var(--border);
}
.player-num {
    position: absolute; top: 10px; right: 14px;
    font-family: 'Bebas Neue', sans-serif;
    font-size: 1.8rem; color: rgba(201,168,76,0.25); line-height: 1;
}
.player-name { font-family: 'Oswald', sans-serif; font-size: 1rem; letter-spacing: 1px; color: var(--white); }
.player-pos {
    display: inline-block; margin: 0.3rem 0;
    font-size: 0.65rem; letter-spacing: 2px;
    padding: 2px 10px; border-radius: 20px; text-transform: uppercase;
}
.pos-POR { background: rgba(52,152,219,0.2); color: #5dade2; border: 1px solid rgba(52,152,219,0.4); }
.pos-DEF { background: rgba(39,174,96,0.2);  color: #58d68d; border: 1px solid rgba(39,174,96,0.4); }
.pos-MED { background: rgba(201,168,76,0.15);color: var(--gold); border: 1px solid rgba(201,168,76,0.4); }
.pos-DEL { background: rgba(192,57,43,0.2);  color: #ec7063; border: 1px solid rgba(192,57,43,0.4); }

.player-club { color: var(--muted); font-size: 0.75rem; letter-spacing: 1px; }
.p-stats { display: flex; justify-content: space-around; margin-top: 1rem; padding-top: 0.8rem; border-top: 1px solid var(--border); }
.p-s-v { font-family: 'Bebas Neue', sans-serif; font-size: 1.6rem; color: var(--gold2); line-height: 1; }
.p-s-l { font-size: 0.6rem; color: var(--muted); letter-spacing: 1px; text-transform: uppercase; }

/* ─── HISTORY CARD ─── */
.hist-card {
    background: var(--card);
    border: 1px solid var(--border); border-radius: 12px;
    padding: 1.2rem 1.5rem;
    display: flex; align-items: center; gap: 1.5rem;
    margin-bottom: 0.6rem; transition: all 0.25s;
}
.hist-card:hover { border-color: var(--border-h); transform: translateX(5px); }
.hist-year {
    font-family: 'Bebas Neue', sans-serif; font-size: 2rem;
    color: var(--gold); min-width: 75px; letter-spacing: 2px; line-height: 1;
}
.hist-champ { font-family: 'Oswald', sans-serif; font-size: 1.05rem; color: var(--white); }
.hist-det { color: var(--muted); font-size: 0.78rem; margin-top: 0.25rem; }

/* ─── TITLES RANK ─── */
.title-bar-wrap { margin-bottom: 0.6rem; }
.title-bar-header {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 4px;
}
.title-bar-label { font-family: 'Oswald', sans-serif; font-size: 0.95rem; letter-spacing: 1px; }
.title-bar-val { font-family: 'Bebas Neue', sans-serif; font-size: 1.1rem; color: var(--gold2); }
.title-bar-bg { background: rgba(255,255,255,0.06); border-radius: 6px; height: 8px; overflow: hidden; }
.title-bar-fill { height: 100%; border-radius: 6px; background: linear-gradient(90deg, var(--gold), var(--gold2)); }

/* ─── TABS ─── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(13,31,60,0.6) !important;
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
    padding: 5px !important; gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--muted) !important;
    font-family: 'Oswald', sans-serif !important;
    letter-spacing: 2px !important; font-size: 0.82rem !important;
    border-radius: 8px !important; padding: 0.5rem 1.2rem !important;
    transition: all 0.2s !important; border: none !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--gold), var(--gold2)) !important;
    color: #000 !important; font-weight: 700 !important;
}

/* ─── SELECT / INPUT ─── */
.stSelectbox > div > div, .stTextInput > div > div > input {
    background: rgba(13,31,60,0.8) !important;
    border: 1px solid var(--border) !important;
    color: var(--light) !important; border-radius: 10px !important;
}
.stSelectbox label, .stTextInput label, .stMultiSelect label {
    color: var(--muted) !important;
    font-family: 'Oswald', sans-serif !important;
    letter-spacing: 2px !important; font-size: 0.78rem !important;
    text-transform: uppercase !important;
}

/* ─── RADIO / CHECKBOX ─── */
.stRadio > div { gap: 1rem; }
.stRadio label { color: var(--light) !important; font-size: 0.9rem !important; }

/* ─── EXPANDER ─── */
.streamlit-expanderHeader {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--light) !important;
    font-family: 'Oswald', sans-serif !important;
    letter-spacing: 1px !important;
}

/* ─── METRIC OVERRIDE ─── */
[data-testid="stMetricValue"] {
    font-family: 'Bebas Neue', sans-serif !important;
    font-size: 2.2rem !important;
    color: var(--gold2) !important;
}
[data-testid="stMetricLabel"] {
    font-family: 'Oswald', sans-serif !important;
    letter-spacing: 2px !important; color: var(--muted) !important;
    font-size: 0.72rem !important;
}

/* ─── SCROLLBAR ─── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--navy); }
::-webkit-scrollbar-thumb { background: var(--blue2); border-radius: 10px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }

/* ─── DIVIDER ─── */
.gold-div {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
    margin: 1.5rem 0; border: none;
}

/* ─── RADAR CONTAINER ─── */
.radar-wrap {
    background: var(--card);
    border: 1px solid var(--border); border-radius: 14px;
    padding: 1rem; backdrop-filter: blur(10px);
}

/* ─── COMPARISON HEADER ─── */
.cmp-header {
    display: grid; grid-template-columns: 1fr auto 1fr;
    align-items: center; gap: 1rem;
    padding: 1.5rem;
    background: var(--card);
    border: 1px solid var(--border); border-radius: 14px;
    margin-bottom: 1.5rem;
}
.cmp-vs {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.5rem; color: var(--gold);
    letter-spacing: 3px; text-align: center;
}
.cmp-player { text-align: center; }
.cmp-player-flag { font-size: 2.5rem; }
.cmp-player-name { font-family: 'Oswald', sans-serif; font-size: 1.1rem; color: var(--white); margin-top: 0.3rem; }
.cmp-player-team { font-size: 0.72rem; letter-spacing: 2px; color: var(--muted); }

/* ─── FOOTER ─── */
.footer {
    text-align: center; padding: 2rem;
    color: var(--muted); font-size: 0.75rem; letter-spacing: 2px;
    border-top: 1px solid var(--border); margin-top: 3rem;
    text-transform: uppercase;
}

/* ─── HIDE STREAMLIT BRANDING ─── */
#MainMenu, footer, header { visibility: hidden; }
</style>
"""
