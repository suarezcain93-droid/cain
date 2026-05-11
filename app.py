import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA IA (Pon tu API Key aquí) ---
# Consíguela en: https://aistudio.google.com/
API_KEY = "AIzaSyBRzef8Q6mQYOqt0-eT89b22wwcKQzPLO0"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- CONFIGURACIÓN DE TEMAS ---
TEMAS = {
    "Clásico": {"bg": "#ffffff", "txt": "#222222", "card": "#f0f2f6", "btn": "#4CAF50"},
    "Messi 10 🇦🇷": {"bg": "#74ACDF", "txt": "#ffffff", "card": "#003566", "btn": "#f0b429"},
    "Ronaldo CR7 🇵🇹": {"bg": "#E5252D", "txt": "#ffffff", "card": "#004B23", "btn": "#cfa10d"},
    "Boca Juniors 💙💛": {"bg": "#003566", "txt": "#ffc300", "card": "#001d3d", "btn": "#ffc300"},
    "River Plate ⚪🔴": {"bg": "#ffffff", "txt": "#d90429", "card": "#f5f5f5", "btn": "#000000"},
    "Brasil 🇧🇷": {"bg": "#FFDF00", "txt": "#009B3A", "card": "#002776", "btn": "#ffffff"},
    "Argentina 🇦🇷": {"bg": "#74ACDF", "txt": "#ffffff", "card": "#ffffff", "btn": "#f0b429"},
    "Flamengo ❤️🖤": {"bg": "#000000", "txt": "#ffffff", "card": "#c1121f", "btn": "#ffffff"},
    "Corinthians ⚪⚫": {"bg": "#ffffff", "txt": "#000000", "card": "#333333", "btn": "#000000"},
    "Vasco da Gama 💢": {"bg": "#000000", "txt": "#ffffff", "card": "#333333", "btn": "#ff0000"},
    "Sao Paulo 🔴⚪⚫": {"bg": "#ffffff", "txt": "#000000", "card": "#c1121f", "btn": "#000000"},
    "Anime ⛩️": {"bg": "#ff85a1", "txt": "#ffffff", "card": "#f72585", "btn": "#4cc9f0"},
    "F1 🏎️": {"bg": "#FF1801", "txt": "#ffffff", "card": "#000000", "btn": "#ffffff"},
    "Princesas Disney 👑": {"bg": "#f8c8dc", "txt": "#5d3fd3", "card": "#ffffff", "btn": "#ff69b4"},
    "Autos 🏎️": {"bg": "#2b2d42", "txt": "#edf2f4", "card": "#8d99ae", "btn": "#ef233c"},
    "The Simpsons 🍩": {"bg": "#FFD90F", "txt": "#4773AA", "card": "#ffffff", "btn": "#70ad47"},
    "Breaking Bad 🧪": {"bg": "#074701", "txt": "#ffffff", "card": "#000000", "btn": "#f2e307"},
    "Star Wars 🌌": {"bg": "#000000", "txt": "#FFE81F", "card": "#1a1a1a", "btn": "#ffffff"},
    "The Truman Show 📺": {"bg": "#87ceeb", "txt": "#000000", "card": "#ffffff", "btn": "#ff4500"},
    "Futbol ⚽": {"bg": "#2e7d32", "txt": "#ffffff", "card": "#1b5e20", "btn": "#c6ff00"},
}

# --- INTERFAZ ---
st.set_page_config(page_title="Buscador Humano IA", layout="wide")

# Selector de tema
st.sidebar.title("🎨 Personalizar")
opcion = st.sidebar.selectbox("Elige un tema:", list(TEMAS.keys()))
t = TEMAS[opcion]

# Inyección de Estilos CSS
st.markdown(f"""
    <style>
    .stApp {{ background-color: {t['bg']}; color: {t['txt']}; }}
    h1, h2, h3, p, label {{ color: {t['txt']} !important; }}
    .result-card {{
        background-color: {t['card']};
        padding: 20px;
        border-radius: 15px;
        border: 2px solid {t['btn']};
        margin-bottom: 20px;
        color: {t['txt']};
    }}
    .stButton>button {{
        background-color: {t['btn']};
        color: {t['bg']};
        border-radius: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

st.title(f"🔍 Buscador de Experiencias: {opcion}")
st.write("Encontramos personas reales en foros y comunidades que ya resolvieron tu duda.")

query = st.text_input("Escribe tu pregunta (Personal, Trabajo, Escuela...)", placeholder="¿Cómo puedo...?")

if query:
    with st.spinner('IA buscando personas reales y resumiendo...'):
        try:
            # PROMPT PARA LA IA
            # Aquí le pedimos a la IA que simule la búsqueda y cree las tarjetas estructuradas
            prompt_ia = f"""
            Actúa como un buscador avanzado. El usuario pregunta: "{query}".
            Busca en tu base de datos información real de foros como Reddit, Quora y StackOverflow.
            Devuelve 3 resultados distintos. 
            Para cada resultado pon: 
            1. Un título llamativo.
            2. Un resumen de la solución que dio una persona real.
            3. Una fuente inventada pero realista (ej: reddit.com/r/tecnologia).
            Separa los resultados con la palabra '---'.
            """
            
            response = model.generate_content(prompt_ia)
            resultados = response.text.split('---')

            # Mostrar resultados en columnas tipo "Google"
            for res in resultados:
                if len(res) > 10:
                    st.markdown(f"""
                    <div class="result-card">
                        {res}
                    </div>
                    """, unsafe_allow_html=True)
                    
        except Exception as e:
            st.error(f"Hubo un error con la API: {e}. Asegúrate de poner tu API KEY correctamente.")

st.sidebar.markdown("---")
st.sidebar.write("⚡ Desarrollado con IA Gratuita")