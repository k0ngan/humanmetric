
import streamlit as st
from utils_ui import inject_css
from dummy_data import FEATURED_JOBS, CATEGORIES, TESTIMONIALS

st.set_page_config(page_title="HumanMetrics — Empleos y Talento", layout="wide")
inject_css(css_file="styles.css")

# 🔹 NUEVOS BOTONES
st.title("Conectamos el talento con las oportunidades correctas.")
st.caption("Busca, postula y crea ofertas con análisis inteligente.")
# ===== Hero =====
st.markdown('''
<div class="hero">
  <div>
    <div class="badge">🚀 Nueva • Plataforma de Empleo</div>
    <h1>Conectamos el talento con las oportunidades correctas.</h1>
    <p>Busca empleos, filtra por ubicación y tecnología, y postula en minutos.</p>
    <div class="searchbar">
      <div class="input-like">🔎 &nbsp; Rol o tecnología</div>
      <div class="input-like">📍 &nbsp; Ubicación</div>
      <div class="input-like">🏷️ &nbsp; Modalidad</div>
      <button class="btn">Buscar Empleo</button>
    </div>
  </div>
  <div class="hero-card">
    <strong>Tips para destacar</strong>
    <ul>
      <li>Optimiza tu CV con 5 logros medibles.</li>
      <li>Agrega habilidades clave (Python, SQL, Docker, ...).</li>
      <li>Activa alertas por correo (próximamente).</li>
    </ul>
  </div>
</div>
''', unsafe_allow_html=True)

# ===== KPIs =====
st.markdown('''
<div class="kpis">
  <div class="kpi"><span>Ofertas activas</span><h3>342</h3></div>
  <div class="kpi"><span>Empresas</span><h3>84</h3></div>
  <div class="kpi"><span>Postulaciones hoy</span><h3>1,209</h3></div>
  <div class="kpi"><span>Tasa de respuesta</span><h3>92%</h3></div>
</div>
''', unsafe_allow_html=True)

# ===== Categorías =====
st.markdown('<div class="section"><h3>Explora por categorías</h3>', unsafe_allow_html=True)
st.markdown('<div class="grid">', unsafe_allow_html=True)
for c in CATEGORIES:
    st.markdown(f'''
    <div class="card">
      <div class="title">{c["name"]}</div>
      <div class="meta">{c["openings"]} vacantes</div>
      <div><span class="tag">Remoto</span><span class="tag">Híbrido</span><span class="tag">Presencial</span></div>
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Ofertas destacadas =====
st.markdown('<div class="section"><h3>Ofertas destacadas</h3>', unsafe_allow_html=True)
st.markdown('<div class="grid">', unsafe_allow_html=True)
for job in FEATURED_JOBS:
    skills = " ".join([f'<span class="tag">{s}</span>' for s in job["skills"]])
    st.markdown(f'''
    <div class="card">
      <p class="title">{job["t"]}</p>
      <p class="meta">{job["e"]} — {job["u"]}</p>
      <div>{skills}</div>
      <div style="margin-top:.6rem; display:flex; gap:.5rem;">
        <a class="btn" href="#" style="text-decoration:none; padding:.5rem .8rem; border-radius:10px;">Ver</a>
        <a class="btn" href="#" style="text-decoration:none; background:rgba(14,116,144,.08); padding:.5rem .8rem; border-radius:10px;">Postular</a>
      </div>
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Logos (placeholder) =====
st.markdown('<div class="section"><h3>Empresas que confían</h3>', unsafe_allow_html=True)
st.markdown('<div class="logos">', unsafe_allow_html=True)
companies = {
    "Nómade": "https://nomade.com",
    "MFN": "https://mfn.com",
    "UTEM": "https://utem.cl",
    "Betel": "https://betel.com",
    "CloudOps": "https://cloudops.com",
    "Acme": "https://acme.com"
}
for name, url in companies.items():
    st.markdown(f'<a href="{url}" target="_blank" style="text-decoration:none;"><div class="logo">{name}</div></a>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Testimonials =====
st.markdown('<div class="section"><h3>Testimonios</h3>', unsafe_allow_html=True)
st.markdown('<div class="testimonials-grid">', unsafe_allow_html=True)
for t in TESTIMONIALS:
    st.markdown(f'''
    <div class="testimonial-card">
      <p class="quote">{t["q"]}</p>
      <p class="author">— {t["a"]}</p>
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    if st.button("📝 Crear Postulación"):
        st.switch_page("pages/2_Crear_Postulacion.py")
with col2:
    if st.button("🎥 Postular con Video"):
        st.switch_page("pages/4_Postular_Con_Video.py")

# ===== CTA Footer =====
st.markdown('<div class="footer">© {year} HumanMetrics — Todos los derechos reservados.</div>'.format(year=__import__("datetime").datetime.now().year), unsafe_allow_html=True)