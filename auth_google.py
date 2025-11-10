# auth_google.py
import streamlit as st
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from google.auth.transport import requests as grequests

SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]

CLIENT_ID = st.secrets["GOOGLE_CLIENT_ID"]
REDIRECT_URI = st.secrets["GOOGLE_REDIRECT_URI"]

def _flow():
    # Usa el archivo oficial bajado de Google Cloud
    return Flow.from_client_secrets_file(
        "client_secret.json",
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,  # Debe coincidir con el de la consola
    )

def start_oauth(role: str):
    """Inicia el flujo y retorna (auth_url, state)."""
    flow = _flow()
    auth_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )
    # Guarda estado + rol solicitado (POSTULANTE o RECLUTADOR)
    st.session_state.oauth_state = {"state": state, "role": role}
    return auth_url, state

def handle_callback():
    """Completa el intercambio y retorna el payload del usuario (claims)."""
    params = st.experimental_get_query_params()
    if "code" not in params or "state" not in params:
        return None

    code = params["code"][0]
    state = params["state"][0]

    if "oauth_state" not in st.session_state or st.session_state.oauth_state["state"] != state:
        st.error("Estado OAuth inválido.")
        return None

    flow = _flow()
    flow.fetch_token(code=code)
    creds = flow.credentials

    # Verifica el ID Token y obtiene claims del usuario
    request = grequests.Request()
    claims = id_token.verify_oauth2_token(
        id_token=creds.id_token,
        request=request,
        audience=CLIENT_ID,
    )
    # claims típicos: sub (id), email, email_verified, name, picture, given_name, family_name
    return claims
