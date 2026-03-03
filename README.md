# ⚽ Mundial 2026 — App Streamlit

App completa para seguir el Mundial 2026 con estadísticas avanzadas, diseño premium y CSS personalizado.

## 📁 Estructura del proyecto

```
mundial_2026/
├── app.py                              ← Página principal (Home)
├── requirements.txt
├── pages/
│   ├── 1_⚽_Mundial_2026.py            ← Partidos, Grupos, Clasificaciones, Premios, Selecciones, Comparación
│   └── 2_📜_Estadísticas_Históricas.py ← Historia, Selecciones históricas, Comparar equipos
├── components/
│   ├── styles.py                       ← CSS global (colores, tarjetas, tablas, etc.)
│   └── charts.py                       ← Gráficos Plotly (radar, barras, scatter, etc.)
└── data/
    └── mock_data.py                    ← Datos de ejemplo (reemplazar con API real)
```

## 🚀 Instalación y ejecución

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🎨 Diseño

- **Paleta**: Azul marino profundo + Dorado FIFA + Rojo acento
- **Tipografías**: Bebas Neue (títulos) + Oswald (subtítulos) + Inter (cuerpo)
- **Componentes**: Tarjetas de partido, tablas de clasificación, radar charts, leaderboards, award cards

## 📋 Secciones

### 1. MUNDIAL 2026
| Sección | Descripción |
|---------|-------------|
| 🏟️ Partidos | Resultados en vivo, finalizados y próximos con banderas |
| 📊 Grupos | Clasificación completa por grupo (PJ, V, E, D, GF, GC, DIF, TA, TR, PTS) |
| 🥇 Clasificaciones | Máximos goleadores, asistentes y porterías imbatidas |
| 🏅 Premios | Bota de Oro, MVP, Mejor Portero, Mejor Joven |
| 👕 Selecciones | Plantillas por posición + stats avanzadas de jugador (radar) + stats del equipo |
| ⚖️ Comparación | Cara a cara de jugadores con radar comparativo y barras |

### 2. ESTADÍSTICAS HISTÓRICAS
| Sección | Descripción |
|---------|-------------|
| 🏆 Historia | Todos los mundiales (1930–2022), campeones, estadísticas |
| 📊 Ranking | Títulos por selección con barras visuales |
| ⚽ Goleadores históricos | Top 10 goleadores de todos los tiempos |
| 📈 Evolución | Gráficos de goles, partidos y goles/partido por edición |
| 🌍 Selecciones | Estadísticas avanzadas (radar, métricas, jugadores) de los últimos 10 partidos |
| ⚖️ Comparar selecciones | Radar comparativo + scatter xG/xGA + tabla |

## 🔌 Conectar datos reales

Sustituye las funciones en `data/mock_data.py` con llamadas a tu API preferida:

- **API-Football** (api-football.com)
- **StatsBomb** (statsbomb.com)
- **Opta / Stats Perform**
- **FBref** (web scraping con BeautifulSoup)
- **FIFA API oficial**

Ejemplo de integración:
```python
import requests

def get_live_matches():
    r = requests.get("https://api-football.com/v3/fixtures?live=all&league=1",
                     headers={"X-RapidAPI-Key": "TU_API_KEY"})
    return r.json()["response"]
```

## 🎨 Personalización CSS

Todos los estilos están centralizados en `components/styles.py`. Variables CSS:

```css
:root {
    --gold:   #C9A84C;   /* Dorado principal */
    --gold2:  #F0C040;   /* Dorado brillante */
    --red:    #C0392B;   /* Rojo acento (LIVE) */
    --navy:   #060e1f;   /* Azul marino fondo */
    --blue2:  #1E4A8A;   /* Azul tarjetas */
}
```
