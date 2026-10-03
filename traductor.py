import streamlit as st
from openai import OpenAI

API_BASE = "http://localhost:1234/v1"
API_KEY = "lm-studio"

MODELO_ACTUAL = "google/gemma-3n-e4b"  
IDIOMAS_DISPONIBLES = ["Español", "Inglés", "Francés", "Alemán"]
DEFAULT_ORIGEN = IDIOMAS_DISPONIBLES[0] 
DEFAULT_DESTINO = IDIOMAS_DISPONIBLES[1] 
@st.cache_resource
def get_openai_client():
    try:
        client = OpenAI(base_url=API_BASE, api_key=API_KEY)
        return client
    except Exception as e:
        return None

client = get_openai_client()

if 'origen' not in st.session_state:
    st.session_state.origen = DEFAULT_ORIGEN
if 'destino' not in st.session_state:
    st.session_state.destino = DEFAULT_DESTINO

def swap_languages():
    """Función que se llama al presionar el botón de intercambio, invierte Origen y Destino."""
    temp = st.session_state.origen
    st.session_state.origen = st.session_state.destino
    st.session_state.destino = temp

def traducir_texto(client, texto_a_traducir, idioma_origen, idioma_destino, modelo):
    """
    Envía la solicitud de traducción al modelo a través de la API local.
    """
    if not client:
        return "ERROR: Cliente de LM Studio no inicializado o conectado."

    system_prompt = (
        "Eres un traductor profesional, preciso y conciso. Tu única tarea es proporcionar la traducción solicitada. "
        "La respuesta DEBE ser SOLO la traducción, sin comillas, encabezados, o texto explicativo."
    )
    
    user_prompt = (
        f"Traduce el siguiente texto de **{idioma_origen}** a **{idioma_destino}**.\n\n"
        f"TEXTO A TRADUCIR: '{texto_a_traducir}'"
    )

    try:
        response = client.chat.completions.create(
            model=modelo,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1 
        )
        
        traduccion_bruta = response.choices[0].message.content
        traduccion_final = traduccion_bruta.strip().strip('"')
        return traduccion_bruta

    except Exception as e:
        return f"Error en la generación de la traducción. Asegúrate que el modelo '{modelo}' está cargado en LM Studio. Detalle: {e}"

def main():
    st.set_page_config(page_title="LM Studio Translator", layout="wide")
    st.title("🌐 Traductor de Texto con LLM Local (LM Studio)")
    st.subheader("Traducción impulsada por el modelo que ejecutas en tu propia máquina.")
    
    if client:
        st.sidebar.success(f"✅ Conectado a LM Studio en {API_BASE}")
    else:
        st.sidebar.error("❌ No se pudo conectar a LM Studio. Por favor, revísalo.")
        
    st.sidebar.markdown(f"**Modelo Utilizado:** `{MODELO_ACTUAL}`")

    col1, col_swap, col2 = st.columns([0.45, 0.1, 0.45])

    with col1:
        st.selectbox(
            "Idioma de Origen", 
            IDIOMAS_DISPONIBLES, 
            key='origen', 
            index=IDIOMAS_DISPONIBLES.index(st.session_state.origen)
        )
    
    with col_swap:
        st.markdown("<div style='margin-top: 28px; text-align: center;'>", unsafe_allow_html=True)
        st.button("🔄", on_click=swap_languages, help="Intercambiar Idiomas")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.selectbox(
            "Idioma de Destino", 
            IDIOMAS_DISPONIBLES, 
            key='destino', 
            index=IDIOMAS_DISPONIBLES.index(st.session_state.destino)
        )
    
    texto_entrada = st.text_area(
        "📝 Ingresa el texto a traducir aquí:",
        height=200,
        placeholder=f"Escribe tu texto en {st.session_state.origen}..."
    )

    if st.button("🚀 Traducir Texto", type="primary"):
        if texto_entrada and client:
            with st.spinner(f"⏳ Traduciendo de {st.session_state.origen} a {st.session_state.destino}..."):
                resultado = traducir_texto(
                    client, 
                    texto_entrada, 
                    st.session_state.origen, 
                    st.session_state.destino, 
                    MODELO_ACTUAL
                )
                
            st.success("Traducción completada.")
            
            st.markdown(f"**Resultado en {st.session_state.destino}:**")
            st.code(resultado, language='text')

        elif not texto_entrada:
            st.warning("Por favor, ingresa algún texto para traducir.")
            
if __name__ == "__main__":
    main()