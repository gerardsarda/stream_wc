"""
mock_data.py
Todos los datos de ejemplo para Mundial 2026.
Reemplaza estas estructuras con tu API/DB real.
"""
import pandas as pd
from datetime import datetime, timedelta

# ─────────────────────────────────────────────────────────
# GRUPOS Y SELECCIONES
# ─────────────────────────────────────────────────────────
GROUPS = {
    "A": [
        {"name": "Estados Unidos", "flag": "🇺🇸", "code": "USA"},
        {"name": "México",         "flag": "🇲🇽", "code": "MEX"},
        {"name": "Canadá",         "flag": "🇨🇦", "code": "CAN"},
        {"name": "Bolivia",        "flag": "🇧🇴", "code": "BOL"},
    ],
    "B": [
        {"name": "España",         "flag": "🇪🇸", "code": "ESP"},
        {"name": "Croacia",        "flag": "🇭🇷", "code": "CRO"},
        {"name": "Marruecos",      "flag": "🇲🇦", "code": "MAR"},
        {"name": "Bélgica",        "flag": "🇧🇪", "code": "BEL"},
    ],
    "C": [
        {"name": "Argentina",      "flag": "🇦🇷", "code": "ARG"},
        {"name": "Brasil",         "flag": "🇧🇷", "code": "BRA"},
        {"name": "Ecuador",        "flag": "🇪🇨", "code": "ECU"},
        {"name": "Nigeria",        "flag": "🇳🇬", "code": "NGA"},
    ],
    "D": [
        {"name": "Francia",        "flag": "🇫🇷", "code": "FRA"},
        {"name": "Alemania",       "flag": "🇩🇪", "code": "GER"},
        {"name": "Portugal",       "flag": "🇵🇹", "code": "POR"},
        {"name": "Argelia",        "flag": "🇩🇿", "code": "ALG"},
    ],
    "E": [
        {"name": "Inglaterra",     "flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "code": "ENG"},
        {"name": "Países Bajos",   "flag": "🇳🇱", "code": "NED"},
        {"name": "Uruguay",        "flag": "🇺🇾", "code": "URU"},
        {"name": "Irán",           "flag": "🇮🇷", "code": "IRN"},
    ],
    "F": [
        {"name": "Italia",         "flag": "🇮🇹", "code": "ITA"},
        {"name": "Turquía",        "flag": "🇹🇷", "code": "TUR"},
        {"name": "Senegal",        "flag": "🇸🇳", "code": "SEN"},
        {"name": "Australia",      "flag": "🇦🇺", "code": "AUS"},
    ],
}

FLAG_MAP = {t["code"]: t["flag"] for grp in GROUPS.values() for t in grp}
NAME_MAP = {t["code"]: t["name"] for grp in GROUPS.values() for t in grp}

# ─────────────────────────────────────────────────────────
# PARTIDOS
# ─────────────────────────────────────────────────────────
base = datetime(2026, 6, 11)

MATCHES = [
    # Grupo A
    {"id": 1,  "group": "A", "home": "USA", "away": "MEX", "home_score": 2, "away_score": 0, "status": "FT",   "date": base + timedelta(days=0),  "venue": "SoFi Stadium, LA"},
    {"id": 2,  "group": "A", "home": "CAN", "away": "BOL", "home_score": 3, "away_score": 1, "status": "FT",   "date": base + timedelta(days=0),  "venue": "Estadio Azteca, CDMX"},
    {"id": 3,  "group": "A", "home": "USA", "away": "CAN", "home_score": 1, "away_score": 1, "status": "FT",   "date": base + timedelta(days=4),  "venue": "MetLife Stadium, NJ"},
    {"id": 4,  "group": "A", "home": "MEX", "away": "BOL", "home_score": 2, "away_score": 2, "status": "FT",   "date": base + timedelta(days=4),  "venue": "AT&T Stadium, Dallas"},
    {"id": 5,  "group": "A", "home": "USA", "away": "BOL", "home_score": 1, "away_score": 0, "status": "LIVE", "date": base + timedelta(days=8),  "venue": "Rose Bowl, Pasadena"},
    {"id": 6,  "group": "A", "home": "MEX", "away": "CAN", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=8),  "venue": "Estadio Azteca, CDMX"},
    # Grupo B
    {"id": 7,  "group": "B", "home": "ESP", "away": "MAR", "home_score": 3, "away_score": 1, "status": "FT",   "date": base + timedelta(days=1),  "venue": "MetLife Stadium, NJ"},
    {"id": 8,  "group": "B", "home": "CRO", "away": "BEL", "home_score": 1, "away_score": 2, "status": "FT",   "date": base + timedelta(days=1),  "venue": "AT&T Stadium, Dallas"},
    {"id": 9,  "group": "B", "home": "ESP", "away": "CRO", "home_score": 2, "away_score": 1, "status": "FT",   "date": base + timedelta(days=5),  "venue": "Hard Rock Stadium, Miami"},
    {"id": 10, "group": "B", "home": "MAR", "away": "BEL", "home_score": 1, "away_score": 1, "status": "FT",   "date": base + timedelta(days=5),  "venue": "Gillette Stadium, Boston"},
    {"id": 11, "group": "B", "home": "ESP", "away": "BEL", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=9),  "venue": "SoFi Stadium, LA"},
    {"id": 12, "group": "B", "home": "CRO", "away": "MAR", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=9),  "venue": "Lincoln Financial, Philadelphia"},
    # Grupo C
    {"id": 13, "group": "C", "home": "ARG", "away": "ECU", "home_score": 3, "away_score": 0, "status": "FT",   "date": base + timedelta(days=2),  "venue": "Hard Rock Stadium, Miami"},
    {"id": 14, "group": "C", "home": "BRA", "away": "NGA", "home_score": 2, "away_score": 1, "status": "FT",   "date": base + timedelta(days=2),  "venue": "Rose Bowl, Pasadena"},
    {"id": 15, "group": "C", "home": "ARG", "away": "BRA", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=10), "venue": "MetLife Stadium, NJ"},
    {"id": 16, "group": "C", "home": "ECU", "away": "NGA", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=10), "venue": "AT&T Stadium, Dallas"},
    # Grupo D
    {"id": 17, "group": "D", "home": "FRA", "away": "ALG", "home_score": 4, "away_score": 0, "status": "FT",   "date": base + timedelta(days=3),  "venue": "Gillette Stadium, Boston"},
    {"id": 18, "group": "D", "home": "GER", "away": "POR", "home_score": 1, "away_score": 2, "status": "FT",   "date": base + timedelta(days=3),  "venue": "Lincoln Financial, Philadelphia"},
    {"id": 19, "group": "D", "home": "FRA", "away": "GER", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=11), "venue": "SoFi Stadium, LA"},
    {"id": 20, "group": "D", "home": "POR", "away": "ALG", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=11), "venue": "Rose Bowl, Pasadena"},
    # Grupo E
    {"id": 21, "group": "E", "home": "ENG", "away": "URU", "home_score": 2, "away_score": 1, "status": "FT",   "date": base + timedelta(days=3),  "venue": "AT&T Stadium, Dallas"},
    {"id": 22, "group": "E", "home": "NED", "away": "IRN", "home_score": 3, "away_score": 0, "status": "FT",   "date": base + timedelta(days=3),  "venue": "Hard Rock Stadium, Miami"},
    {"id": 23, "group": "E", "home": "ENG", "away": "NED", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=12), "venue": "MetLife Stadium, NJ"},
    {"id": 24, "group": "E", "home": "URU", "away": "IRN", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=12), "venue": "Gillette Stadium, Boston"},
    # Grupo F
    {"id": 25, "group": "F", "home": "ITA", "away": "AUS", "home_score": 2, "away_score": 0, "status": "FT",   "date": base + timedelta(days=4),  "venue": "Lincoln Financial, Philadelphia"},
    {"id": 26, "group": "F", "home": "TUR", "away": "SEN", "home_score": 1, "away_score": 1, "status": "FT",   "date": base + timedelta(days=4),  "venue": "Gillette Stadium, Boston"},
    {"id": 27, "group": "F", "home": "ITA", "away": "TUR", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=13), "venue": "SoFi Stadium, LA"},
    {"id": 28, "group": "F", "home": "SEN", "away": "AUS", "home_score": None, "away_score": None, "status": "NS", "date": base + timedelta(days=13), "venue": "AT&T Stadium, Dallas"},
]

# ─────────────────────────────────────────────────────────
# CLASIFICACIÓN DE GRUPOS  (calculada desde MATCHES)
# ─────────────────────────────────────────────────────────
def compute_standings():
    table = {}
    for grp, teams in GROUPS.items():
        for t in teams:
            table[t["code"]] = {
                "group": grp, "code": t["code"],
                "name": t["name"], "flag": t["flag"],
                "pj": 0, "v": 0, "e": 0, "d": 0,
                "gf": 0, "gc": 0, "dif": 0, "pts": 0,
                "ta": 0, "tr": 0,
            }
    for m in MATCHES:
        if m["status"] in ("FT",) and m["home_score"] is not None:
            h, a = m["home"], m["away"]
            hs, as_ = m["home_score"], m["away_score"]
            # partidos jugados
            table[h]["pj"] += 1; table[a]["pj"] += 1
            table[h]["gf"] += hs; table[h]["gc"] += as_
            table[a]["gf"] += as_; table[a]["gc"] += hs
            if hs > as_:
                table[h]["v"] += 1; table[h]["pts"] += 3
                table[a]["d"] += 1
            elif hs < as_:
                table[a]["v"] += 1; table[a]["pts"] += 3
                table[h]["d"] += 1
            else:
                table[h]["e"] += 1; table[h]["pts"] += 1
                table[a]["e"] += 1; table[a]["pts"] += 1
    # tarjetas mock
    import random; random.seed(42)
    for code in table:
        table[code]["ta"] = random.randint(0, 5)
        table[code]["tr"] = random.randint(0, 1)
        table[code]["dif"] = table[code]["gf"] - table[code]["gc"]
    return table

STANDINGS = compute_standings()

def get_group_standings(group_code):
    rows = [v for v in STANDINGS.values() if v["group"] == group_code]
    rows.sort(key=lambda x: (-x["pts"], -x["dif"], -x["gf"]))
    return rows

# ─────────────────────────────────────────────────────────
# GOLEADORES / ASISTENTES / PORTERÍAS
# ─────────────────────────────────────────────────────────
TOP_SCORERS = [
    {"rank":1, "player":"Kylian Mbappé",    "flag":"🇫🇷", "team":"FRA", "goals":5, "assists":2, "matches":3},
    {"rank":2, "player":"Lionel Messi",     "flag":"🇦🇷", "team":"ARG", "goals":4, "assists":3, "matches":2},
    {"rank":3, "player":"Vinicius Jr.",      "flag":"🇧🇷", "team":"BRA", "goals":3, "assists":1, "matches":2},
    {"rank":4, "player":"Álvaro Morata",    "flag":"🇪🇸", "team":"ESP", "goals":3, "assists":0, "matches":3},
    {"rank":5, "player":"Harry Kane",       "flag":"🏴󠁧󠁢󠁥󠁮󠁧󠁿", "team":"ENG", "goals":2, "assists":1, "matches":2},
    {"rank":6, "player":"Lamine Yamal",     "flag":"🇪🇸", "team":"ESP", "goals":2, "assists":2, "matches":3},
    {"rank":7, "player":"Pedri",            "flag":"🇪🇸", "team":"ESP", "goals":1, "assists":3, "matches":3},
    {"rank":8, "player":"Romelu Lukaku",    "flag":"🇧🇪", "team":"BEL", "goals":2, "assists":0, "matches":2},
]

TOP_ASSISTS = [
    {"rank":1, "player":"Lionel Messi",     "flag":"🇦🇷", "team":"ARG", "assists":3, "goals":4, "matches":2},
    {"rank":2, "player":"Pedri",            "flag":"🇪🇸", "team":"ESP", "assists":3, "goals":1, "matches":3},
    {"rank":3, "player":"Kylian Mbappé",    "flag":"🇫🇷", "team":"FRA", "assists":2, "goals":5, "matches":3},
    {"rank":4, "player":"Lamine Yamal",     "flag":"🇪🇸", "team":"ESP", "assists":2, "goals":2, "matches":3},
    {"rank":5, "player":"Phil Foden",       "flag":"🏴󠁧󠁢󠁥󠁮󠁧󠁿", "team":"ENG", "assists":2, "goals":0, "matches":2},
    {"rank":6, "player":"Vinicius Jr.",      "flag":"🇧🇷", "team":"BRA", "assists":1, "goals":3, "matches":2},
    {"rank":7, "player":"Harry Kane",       "flag":"🏴󠁧󠁢󠁥󠁮󠁧󠁿", "team":"ENG", "assists":1, "goals":2, "matches":2},
    {"rank":8, "player":"Rafael Leão",      "flag":"🇵🇹", "team":"POR", "assists":2, "goals":1, "matches":2},
]

CLEAN_SHEETS = [
    {"rank":1, "player":"Yassine Bounou",   "flag":"🇲🇦", "team":"MAR", "cs":2, "matches":3, "saves":12},
    {"rank":2, "player":"Gianluigi Donnarumma","flag":"🇮🇹","team":"ITA","cs":2, "matches":2, "saves":6},
    {"rank":3, "player":"Alisson Becker",   "flag":"🇧🇷", "team":"BRA", "cs":1, "matches":2, "saves":4},
    {"rank":4, "player":"Jordan Pickford",  "flag":"🏴󠁧󠁢󠁥󠁮󠁧󠁿", "team":"ENG", "cs":1, "matches":2, "saves":5},
    {"rank":5, "player":"Unai Simón",       "flag":"🇪🇸", "team":"ESP", "cs":1, "matches":3, "saves":7},
]

# ─────────────────────────────────────────────────────────
# PREMIOS
# ─────────────────────────────────────────────────────────
AWARDS = {
    "bota_oro":   {"player":"Kylian Mbappé",     "flag":"🇫🇷", "team":"Francia",   "icon":"🥇", "stat":"5 goles", "extra":"2 asistencias"},
    "mvp":        {"player":"Lionel Messi",       "flag":"🇦🇷", "team":"Argentina", "icon":"⭐", "stat":"Rating: 9.2", "extra":"4G + 3A"},
    "mejor_portero":{"player":"Yassine Bounou",  "flag":"🇲🇦", "team":"Marruecos", "icon":"🧤", "stat":"2 p. imbatidas","extra":"12 paradas"},
    "mejor_joven": {"player":"Lamine Yamal",      "flag":"🇪🇸", "team":"España",    "icon":"🌟", "stat":"2G + 2A", "extra":"Rating: 8.7"},
}

# ─────────────────────────────────────────────────────────
# PLANTILLAS  (solo España y Argentina completas como ejemplo)
# ─────────────────────────────────────────────────────────
def get_squad(team_code):
    squads = {
        "ESP": [
            {"name":"Unai Simón",       "pos":"POR", "age":27, "club":"Athletic Club",    "flag":"🇪🇸", "number":1},
            {"name":"David Raya",       "pos":"POR", "age":28, "club":"Arsenal",           "flag":"🇪🇸", "number":13},
            {"name":"Robert Sánchez",   "pos":"POR", "age":26, "club":"Chelsea",           "flag":"🇪🇸", "number":23},
            {"name":"Dani Carvajal",    "pos":"DEF", "age":32, "club":"Real Madrid",       "flag":"🇪🇸", "number":2},
            {"name":"Pau Cubarsí",      "pos":"DEF", "age":17, "club":"FC Barcelona",      "flag":"🇪🇸", "number":4},
            {"name":"Aymeric Laporte",  "pos":"DEF", "age":32, "club":"Al-Nassr",          "flag":"🇪🇸", "number":14},
            {"name":"Alejandro Balde",  "pos":"DEF", "age":21, "club":"FC Barcelona",      "flag":"🇪🇸", "number":3},
            {"name":"Dani Olmo",        "pos":"MED", "age":26, "club":"FC Barcelona",      "flag":"🇪🇸", "number":8},
            {"name":"Pedri",            "pos":"MED", "age":23, "club":"FC Barcelona",      "flag":"🇪🇸", "number":26},
            {"name":"Fabián Ruiz",      "pos":"MED", "age":28, "club":"PSG",               "flag":"🇪🇸", "number":7},
            {"name":"Rodri",            "pos":"MED", "age":28, "club":"Manchester City",   "flag":"🇪🇸", "number":16},
            {"name":"Lamine Yamal",     "pos":"DEL", "age":18, "club":"FC Barcelona",      "flag":"🇪🇸", "number":19},
            {"name":"Álvaro Morata",    "pos":"DEL", "age":32, "club":"AC Milan",          "flag":"🇪🇸", "number":9},
            {"name":"Nico Williams",    "pos":"DEL", "age":22, "club":"Athletic Club",     "flag":"🇪🇸", "number":17},
            {"name":"Ferran Torres",    "pos":"DEL", "age":24, "club":"FC Barcelona",      "flag":"🇪🇸", "number":11},
        ],
        "ARG": [
            {"name":"Emiliano Martínez","pos":"POR", "age":32, "club":"Aston Villa",       "flag":"🇦🇷", "number":1},
            {"name":"Nahuel Molina",    "pos":"DEF", "age":26, "club":"Atlético Madrid",   "flag":"🇦🇷", "number":26},
            {"name":"Cristian Romero",  "pos":"DEF", "age":26, "club":"Tottenham",         "flag":"🇦🇷", "number":13},
            {"name":"Lisandro Martínez","pos":"DEF", "age":26, "club":"Manchester United", "flag":"🇦🇷", "number":25},
            {"name":"Nicolás Tagliafico","pos":"DEF","age":32, "club":"Olympique Lyon",    "flag":"🇦🇷", "number":3},
            {"name":"Rodrigo De Paul",  "pos":"MED", "age":30, "club":"Atlético Madrid",   "flag":"🇦🇷", "number":7},
            {"name":"Leandro Paredes",  "pos":"MED", "age":30, "club":"Roma",              "flag":"🇦🇷", "number":5},
            {"name":"Enzo Fernández",   "pos":"MED", "age":24, "club":"Chelsea",           "flag":"🇦🇷", "number":24},
            {"name":"Alexis Mac Allister","pos":"MED","age":25,"club":"Liverpool",          "flag":"🇦🇷", "number":20},
            {"name":"Lionel Messi",     "pos":"DEL", "age":38, "club":"Inter Miami",       "flag":"🇦🇷", "number":10},
            {"name":"Julián Álvarez",   "pos":"DEL", "age":24, "club":"Atlético Madrid",   "flag":"🇦🇷", "number":9},
            {"name":"Lautaro Martínez", "pos":"DEL", "age":26, "club":"Inter Milán",       "flag":"🇦🇷", "number":22},
            {"name":"Ángel Di María",   "pos":"DEL", "age":38, "club":"Benfica",           "flag":"🇦🇷", "number":11},
        ],
    }
    default = [{"name": f"Jugador {i}", "pos": ["POR","DEF","MED","DEL"][i%4],
                "age": 24+i, "club": "Club FC", "flag": FLAG_MAP.get(team_code, "🏳️"), "number": i+1}
               for i in range(23)]
    return squads.get(team_code, default)

# ─────────────────────────────────────────────────────────
# ESTADÍSTICAS AVANZADAS DE JUGADOR  (mundial actual)
# ─────────────────────────────────────────────────────────
import random as _rnd
_rnd.seed(7)

def get_player_world_cup_stats(player_name, position):
    pos_stats = {
        "POR": {"paradas":_rnd.randint(4,14),"goles_recibidos":_rnd.randint(0,3),
                "porterias_imbatidas":_rnd.randint(0,2),"porcentaje_paradas":round(_rnd.uniform(70,95),1),
                "xg_contra":round(_rnd.uniform(1.5,5.0),2),"salidas":_rnd.randint(1,8),
                "partidos":_rnd.randint(1,3)},
        "DEF": {"duelos_ganados":_rnd.randint(5,20),"intercepciones":_rnd.randint(2,10),
                "despejes":_rnd.randint(4,15),"pases_completados":_rnd.randint(60,95),
                "presion_exitosa":round(_rnd.uniform(40,70),1),"duelos_aereos":_rnd.randint(3,12),
                "goles":_rnd.randint(0,2),"asistencias":_rnd.randint(0,2),"partidos":_rnd.randint(1,3)},
        "MED": {"pases_clave":_rnd.randint(2,10),"pases_completados":_rnd.randint(70,95),
                "recuperaciones":_rnd.randint(3,12),"km_recorridos":round(_rnd.uniform(8.5,12.5),1),
                "xA":round(_rnd.uniform(0.2,1.5),2),"presiones":_rnd.randint(10,30),
                "goles":_rnd.randint(0,3),"asistencias":_rnd.randint(0,4),"partidos":_rnd.randint(1,3)},
        "DEL": {"goles":_rnd.randint(0,5),"asistencias":_rnd.randint(0,3),
                "xG":round(_rnd.uniform(0.5,4.0),2),"remates":_rnd.randint(3,15),
                "remates_puerta":_rnd.randint(1,8),"regates_exitosos":_rnd.randint(2,12),
                "toques_area":_rnd.randint(5,25),"partidos":_rnd.randint(1,3)},
    }
    return pos_stats.get(position, pos_stats["MED"])

# ─────────────────────────────────────────────────────────
# ESTADÍSTICAS AVANZADAS DE SELECCIÓN (mundial actual)
# ─────────────────────────────────────────────────────────
def get_team_world_cup_stats(team_code):
    _rnd.seed(hash(team_code) % 100)
    st = STANDINGS.get(team_code, {})
    return {
        "partidos": st.get("pj", 2),
        "victorias": st.get("v", 1),
        "empates":   st.get("e", 0),
        "derrotas":  st.get("d", 1),
        "goles_favor": st.get("gf", 3),
        "goles_contra": st.get("gc", 2),
        "xG":       round(_rnd.uniform(1.5, 5.0), 2),
        "xGA":      round(_rnd.uniform(0.8, 3.5), 2),
        "posesion": round(_rnd.uniform(45, 68), 1),
        "pases_completados": round(_rnd.uniform(78, 92), 1),
        "presion_alta": round(_rnd.uniform(30, 60), 1),
        "duelos_ganados": round(_rnd.uniform(48, 62), 1),
        "remates_partido": round(_rnd.uniform(8, 18), 1),
        "remates_puerta": round(_rnd.uniform(3, 8), 1),
        "km_partido": round(_rnd.uniform(105, 115), 1),
        "faltas": round(_rnd.uniform(8, 18), 1),
    }

# ─────────────────────────────────────────────────────────
# HISTORIA MUNDIALISTA
# ─────────────────────────────────────────────────────────
WORLD_CUP_HISTORY = [
    {"year":2022,"champion":"Argentina","runner_up":"Francia",       "host":"Qatar",           "goals":172,"teams":32,"matches":64},
    {"year":2018,"champion":"Francia",  "runner_up":"Croacia",       "host":"Rusia",           "goals":169,"teams":32,"matches":64},
    {"year":2014,"champion":"Alemania", "runner_up":"Argentina",     "host":"Brasil",          "goals":171,"teams":32,"matches":64},
    {"year":2010,"champion":"España",   "runner_up":"Países Bajos",  "host":"Sudáfrica",       "goals":145,"teams":32,"matches":64},
    {"year":2006,"champion":"Italia",   "runner_up":"Francia",       "host":"Alemania",        "goals":147,"teams":32,"matches":64},
    {"year":2002,"champion":"Brasil",   "runner_up":"Alemania",      "host":"Corea/Japón",     "goals":161,"teams":32,"matches":64},
    {"year":1998,"champion":"Francia",  "runner_up":"Brasil",        "host":"Francia",         "goals":171,"teams":32,"matches":64},
    {"year":1994,"champion":"Brasil",   "runner_up":"Italia",        "host":"EE.UU.",          "goals":141,"teams":24,"matches":52},
    {"year":1990,"champion":"Alemania", "runner_up":"Argentina",     "host":"Italia",          "goals":115,"teams":24,"matches":52},
    {"year":1986,"champion":"Argentina","runner_up":"Alemania Occ.", "host":"México",          "goals":132,"teams":24,"matches":52},
    {"year":1982,"champion":"Italia",   "runner_up":"Alemania Occ.", "host":"España",          "goals":146,"teams":24,"matches":52},
    {"year":1978,"champion":"Argentina","runner_up":"Países Bajos",  "host":"Argentina",       "goals":102,"teams":16,"matches":38},
    {"year":1974,"champion":"Alemania Occ.","runner_up":"Países Bajos","host":"Alemania Occ.", "goals":97, "teams":16,"matches":38},
    {"year":1970,"champion":"Brasil",   "runner_up":"Italia",        "host":"México",          "goals":95, "teams":16,"matches":32},
    {"year":1966,"champion":"Inglaterra","runner_up":"Alemania Occ.","host":"Inglaterra",      "goals":89, "teams":16,"matches":32},
    {"year":1962,"champion":"Brasil",   "runner_up":"Checoslovaquia","host":"Chile",           "goals":89, "teams":16,"matches":32},
    {"year":1958,"champion":"Brasil",   "runner_up":"Suecia",        "host":"Suecia",          "goals":126,"teams":16,"matches":35},
    {"year":1954,"champion":"Alemania Occ.","runner_up":"Hungría",   "host":"Suiza",           "goals":140,"teams":16,"matches":26},
    {"year":1950,"champion":"Uruguay",  "runner_up":"Brasil",        "host":"Brasil",          "goals":88, "teams":13,"matches":22},
    {"year":1938,"champion":"Italia",   "runner_up":"Hungría",       "host":"Francia",         "goals":84, "teams":15,"matches":18},
    {"year":1934,"champion":"Italia",   "runner_up":"Checoslovaquia","host":"Italia",          "goals":70, "teams":16,"matches":17},
    {"year":1930,"champion":"Uruguay",  "runner_up":"Argentina",     "host":"Uruguay",         "goals":70, "teams":13,"matches":18},
]

TITLES_RANKING = [
    {"team":"Brasil",        "flag":"🇧🇷", "titles":5,  "years":"1958,1962,1970,1994,2002"},
    {"team":"Alemania",      "flag":"🇩🇪", "titles":4,  "years":"1954,1974,1990,2014"},
    {"team":"Italia",        "flag":"🇮🇹", "titles":4,  "years":"1934,1938,1982,2006"},
    {"team":"Argentina",     "flag":"🇦🇷", "titles":3,  "years":"1978,1986,2022"},
    {"team":"Francia",       "flag":"🇫🇷", "titles":2,  "years":"1998,2018"},
    {"team":"Uruguay",       "flag":"🇺🇾", "titles":2,  "years":"1930,1950"},
    {"team":"Inglaterra",    "flag":"🏴󠁧󠁢󠁥󠁮󠁧󠁿", "titles":1,  "years":"1966"},
    {"team":"España",        "flag":"🇪🇸", "titles":1,  "years":"2010"},
]

HISTORIC_SCORERS = [
    {"rank":1,  "player":"Miroslav Klose",   "flag":"🇩🇪", "goals":16, "editions":4, "years":"2002-2014"},
    {"rank":2,  "player":"Ronaldo Nazário",  "flag":"🇧🇷", "goals":15, "editions":4, "years":"1994-2006"},
    {"rank":3,  "player":"Gerd Müller",      "flag":"🇩🇪", "goals":14, "editions":2, "years":"1970-1974"},
    {"rank":4,  "player":"Just Fontaine",    "flag":"🇫🇷", "goals":13, "editions":1, "years":"1958"},
    {"rank":5,  "player":"Pelé",             "flag":"🇧🇷", "goals":12, "editions":4, "years":"1958-1970"},
    {"rank":6,  "player":"Sándor Kocsis",    "flag":"🇭🇺", "goals":11, "editions":1, "years":"1954"},
    {"rank":7,  "player":"Jürgen Klinsmann", "flag":"🇩🇪", "goals":11, "editions":3, "years":"1990-1998"},
    {"rank":8,  "player":"Gabriel Batistuta","flag":"🇦🇷", "goals":10, "editions":3, "years":"1994-2002"},
    {"rank":9,  "player":"Gary Lineker",     "flag":"🏴󠁧󠁢󠁥󠁮󠁧󠁿", "goals":10, "editions":2, "years":"1986-1990"},
    {"rank":10, "player":"Teófilo Cubillas", "flag":"🇵🇪", "goals":10, "editions":2, "years":"1970-1978"},
]

# ─────────────────────────────────────────────────────────
# ESTADÍSTICAS HISTÓRICAS DE SELECCIÓN (últimos 10 partidos)
# ─────────────────────────────────────────────────────────
def get_team_last10_stats(team_code):
    _rnd.seed(hash(team_code) % 999)
    return {
        "victorias": _rnd.randint(5, 9),
        "empates":   _rnd.randint(0, 3),
        "derrotas":  _rnd.randint(0, 2),
        "goles_favor": _rnd.randint(12, 25),
        "goles_contra": _rnd.randint(3, 12),
        "xG_promedio": round(_rnd.uniform(1.5, 2.8), 2),
        "xGA_promedio": round(_rnd.uniform(0.6, 1.5), 2),
        "posesion": round(_rnd.uniform(48, 68), 1),
        "pases_completados": round(_rnd.uniform(80, 92), 1),
        "presion_alta": round(_rnd.uniform(35, 60), 1),
        "duelos_ganados": round(_rnd.uniform(50, 65), 1),
        "remates_partido": round(_rnd.uniform(10, 20), 1),
        "remates_puerta": round(_rnd.uniform(4, 9), 1),
        "km_partido": round(_rnd.uniform(108, 118), 1),
        "faltas": round(_rnd.uniform(9, 17), 1),
        "ataques_derecha": round(_rnd.uniform(28, 38), 1),
        "ataques_centro": round(_rnd.uniform(22, 32), 1),
        "ataques_izquierda": round(_rnd.uniform(28, 38), 1),
    }

# ─────────────────────────────────────────────────────────
# JUGADORES HISTÓRICOS (estadísticas avanzadas último año)
# ─────────────────────────────────────────────────────────
def get_player_season_stats(player_name, position):
    _rnd.seed(hash(player_name) % 500)
    base = {
        "partidos": _rnd.randint(25, 38),
        "minutos": _rnd.randint(1800, 3400),
        "goles": _rnd.randint(0, 30),
        "asistencias": _rnd.randint(0, 15),
        "xG": round(_rnd.uniform(0.5, 20.0), 2),
        "xA": round(_rnd.uniform(0.3, 12.0), 2),
        "pases_clave": _rnd.randint(20, 120),
        "duelos_ganados": round(_rnd.uniform(45, 68), 1),
        "regates_exitosos": _rnd.randint(10, 120),
        "intercepciones": _rnd.randint(5, 60),
        "recuperaciones": _rnd.randint(20, 150),
        "km_partido": round(_rnd.uniform(8.5, 12.5), 1),
        "presion_exitosa": round(_rnd.uniform(28, 55), 1),
        "remates_puerta_pct": round(_rnd.uniform(30, 70), 1),
    }
    return base

ALL_TEAMS = list({t["code"] for grp in GROUPS.values() for t in grp})
