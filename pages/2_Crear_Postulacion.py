import streamlit as st

st.set_page_config(page_title="Crear Postulación — HumanMetrics", layout="wide")
st.title("Crear Postulación (Demo)")
st.caption("Apartado visual para crear una nueva postulación/oferta. No realiza envíos reales.")

with st.form("crear_postulacion"):
    st.subheader("Información del cargo")
    rol = st.text_input("Rol / Título del cargo", placeholder="Ej: Data Scientist Senior")
    descripcion = st.text_area("Descripción del puesto", height=180, placeholder="Responsabilidades, requisitos, beneficios, etc.")
    empresa = st.text_input("Empresa", placeholder="Ej: Nómade Chile")
    extras = st.text_area("Notas adicionales (opcional)", placeholder="Stack tecnológico, bandas salariales, modalidad, etc.")
    analizar = st.checkbox("Permitir análisis automático (IA)", value=True)
    ocultar_empresa = st.checkbox("Ocultar nombre de empresa al público", value=False)

    st.subheader("Preguntas en video para postulantes")
    p1 = st.text_input("Pregunta 1", value="Cuéntanos un proyecto reciente del que te sientas orgulloso.")
    p2 = st.text_input("Pregunta 2", value="¿Qué te motiva del rol y cómo aportarías al equipo?")
    p3 = st.text_input("Pregunta 3", value="Describe un desafío técnico y cómo lo resolviste.")

    if st.form_submit_button("Publicar (simulado)"):
        st.success("Oferta publicada (simulada)")
