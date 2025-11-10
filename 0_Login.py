# pages/0_Login.py
import streamlit as st
from auth_google import start_oauth, handle_callback

st.set_page_config(page_title="Login", layout="centered", initial_sidebar_state="collapsed")
st.title("Acceso a HumanMetrics")

# Botones por rol
col1, col2 = st.columns(2)
with col1:
    if st.button("Continuar con Google (Postulante)"):
        url, _ = start_oauth("POSTULANTE")
        # Redirige inmediatamente
        st.markdown(f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True)

with col2:
    if st.button("Continuar con Google (Reclutador)"):
        url, _ = start_oauth("RECLUTADOR")
        st.markdown(f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True)

# Manejo de callback
claims = handle_callback()
if claims:
    role = st.session_state.oauth_state["role"]

    # ⬇️ AQUÍ GUARDAS LA INFO DEL USUARIO EN SESIÓN
    st.session_state.user = {
        "id": claims.get("sub"),
        "email": claims.get("email"),
        "email_verified": claims.get("email_verified", False),
        "name": claims.get("name"),
        "given_name": claims.get("given_name"),
        "family_name": claims.get("family_name"),
        "picture": claims.get("picture"),
        "role": role,  # POSTULANTE o RECLUTADOR según el botón usado
        # Puedes guardar también el id_token si piensas verificar del lado backend:
        "id_token": claims,  # o almacena solo el string si lo necesitas
    }
    # ⬆️ FIN: zona explícita para datos del usuario

    st.success(f"Autenticado como {st.session_state.user['name']} · Rol: {role}")
    # Redirige a la sección según rol
    if role == "POSTULANTE":
        st.switch_page("pages/1_👨‍💻_Mi_Perfil.py")
    else:
        st.switch_page("pages/1_🧑‍💼_Empresa_Dashboard.py")

# Si ya hay usuario en sesión, muestra resumen
if "user" in st.session_state:
    u = st.session_state.user
    st.caption("Sesión activa:")
    st.write(
        {
            "name": u.get("name"),
            "email": u.get("email"),
            "role": u.get("role"),
        }
    )
