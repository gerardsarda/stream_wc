import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN DE PÁGINA Y CSS
st.set_page_config(page_title="Mundial 2026 Analytics", layout="wide", initial_sidebar_state="expanded")

# Inyectamos CSS para darle un diseño "Pro" (Tarjetas, avatares redondos, sombras)
st.markdown("""
    <style>
    /* Estilo para las tarjetas de partidos */
    .match-card {
        background-color: #1e1e1e;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid #333;
    }
    .team-info {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .score {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ff4b4b;
    }
    /* Estilo para fotos de jugadores */
    .player-avatar {
        border-radius: 50%;
        width: 60px;
        height: 60px;
        object-fit: cover;
        border: 2px solid #ff4b4b;
    }
    /* Limpiar apariencia de tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 5px 5px 0px 0px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. NAVEGACIÓN PRINCIPAL (Sidebar)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/23/FIFA_World_Cup_2026_Logo.png/800px-FIFA_World_Cup_2026_Logo.png", width=200)
st.sidebar.title("Navegación")
menu_principal = st.sidebar.radio("Secciones", ["1. Mundial 2026", "2. Estadísticas Históricas"])

# ==========================================
# SECCIÓN 1: MUNDIAL 2026
# ==========================================
if menu_principal == "1. Mundial 2026":
    st.title("🏆 Mundial 2026: Dashboard en Vivo")
    
    # Submenú usando pestañas (Tabs)
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📅 Partidos", "📊 Clasificación", "🥇 Líderes", "🏆 Premios", "🛡️ Selecciones", "⚖️ Comparador"
    ])
    
    with tab1:
        st.header("Partidos y Resultados")
        st.info("A la espera de resultados. Aquí se conectará la API en vivo.")
        # Ejemplo de tarjeta de partido con CSS
        st.markdown("""
        <div class="match-card">
            <div class="team-info"><img src="https://flagcdn.com/w40/es.png" width="30"> España</div>
            <div class="score">0 - 0</div>
            <div class="team-info">Brasil <img src="https://flagcdn.com/w40/br.png" width="30"></div>
        </div>
        """, unsafe_allow_html=True)
        
    with tab2:
        st.header("Clasificación Fase de Grupos")
        # DataFrame de ejemplo
        df_grupo = pd.DataFrame({
            "Pos": [1, 2, 3, 4],
            "Selección": ["España", "Brasil", "Japón", "Marruecos"],
            "Pts": [0, 0, 0, 0],
            "GF": [0, 0, 0, 0],
            "GC": [0, 0, 0, 0],
            "Dif": [0, 0, 0, 0],
            "TA": [0, 0, 0, 0],
            "TR": [0, 0, 0, 0]
        })
        st.dataframe(df_grupo, hide_index=True, use_container_width=True)

    with tab3:
        st.header("Líderes del Torneo")
        col1, col2, col3 = st.columns(3)
        col1.subheader("⚽ Goleadores")
        col1.write("1. [Foto] Jugador X - 0 Goles")
        col2.subheader("👟 Asistencias")
        col2.write("1. [Foto] Jugador Y - 0 Asistencias")
        col3.subheader("🧤 Portería a Cero")
        col3.write("1. [Foto] Portero Z - 0 Partidos")

    with tab4:
        st.header("Premios (Post-Torneo)")
        st.warning("Esta sección se actualizará al finalizar el torneo.")
        st.markdown("- **Bota de Oro:** Por definir\n- **MVP:** Por definir\n- **Mejor Portero:** Por definir\n- **Mejor Joven:** Por definir")

    with tab5:
        st.header("Selecciones Convocadas")
        seleccion = st.selectbox("Elige una selección:", ["España", "Brasil", "Argentina", "Francia"])
        
        subtab1, subtab2 = st.tabs(["👥 Jugadores", "📈 Estadísticas Avanzadas (Selección)"])
        with subtab1:
            st.write(f"### Convocatoria de {seleccion}")
            st.markdown("""
            <div style='display: flex; align-items: center; gap: 15px;'>
                <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' class='player-avatar'>
                <div>
                    <b>Lamine Yamal</b><br>
                    <small>Delantero | Estadísticas Avanzadas del Mundial: 0 xG, 0 xA</small>
                </div>
            </div>
            """, unsafe_allow_html=True)
        with subtab2:
            st.write(f"### Estilo de Juego: {seleccion} en el Mundial")
            st.info("Aquí insertaremos los gráficos de Posesión, Entradas al área y Radares colectivos.")

    with tab6:
        st.header("Comparador de Jugadores")
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("Jugador 1", ["Jugador A"])
        with col2:
            st.selectbox("Jugador 2", ["Jugador B"])
        st.info("Aquí irá el Radar Chart superpuesto comparando a ambos.")

# ==========================================
# SECCIÓN 2: ESTADÍSTICAS HISTÓRICAS
# ==========================================
elif menu_principal == "2. Estadísticas Históricas":
    st.title("📚 Archivo Histórico")
    
    tab1, tab2 = st.tabs(["📖 Historia Mundialista", "🛡️ Análisis Histórico de Selecciones"])
    
    with tab1:
        st.header("Palmarés y Récords")
        st.write("- **Clasificación de Mundiales Ganados** (Brasil 5, Alemania 4...)")
        st.write("- **Máximos Goleadores Históricos** (Klose 16, Ronaldo 15...)")
        
    with tab2:
        st.header("Análisis de Selecciones (Pre-Mundial)")
        seleccion_hist = st.selectbox("Selecciona un país a analizar:", ["España", "Argentina", "Inglaterra"])
        
        st.subheader("Cómo Juega (Últimos 10 Partidos Oficiales)")
        st.info(f"Radar chart de {seleccion_hist} basado en sus últimos 10 partidos (Clasificatorias/Nations League).")
        
        st.subheader("Estado de Forma de los Jugadores")
        st.info("Métricas avanzadas del último año natural en sus respectivos clubes para los jugadores convocados.")