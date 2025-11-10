
import streamlit as st
from pathlib import Path

def inject_css(css_text: str = "", css_file: str | None = None):
    """Inject CSS into Streamlit app."""
    if css_file:
        css_text = Path(css_file).read_text(encoding="utf-8")
    st.markdown(f"<style>{css_text}</style>", unsafe_allow_html=True)
