import streamlit as st
from utils_ui import inject_css
from dummy_data import FEATURED_JOBS, CATEGORIES, TESTIMONIALS

st.set_page_config(page_title="HumanMetrics — Empleos y Talento", layout="wide")

# CSS base + ajustes mobile
MOBILE_TWEAKS = """
/* Botones anchos y cómodos en mobile */
.stButton > button { width:100%; padding:14px 18px; font-weight:700; border-radius:12px; }

/* Hero y buscador: stack en pantallas pequeñas */
@media (max-width: 820px){
  .hero{ grid-template-columns: 1fr !important; padding:18px; border-radius:16px; }
  .searchbar{ grid-template-columns: 1fr !important; gap:10px; }
}

/* KPIs y grids colapsan a 1-2 columnas */
@media (max-width: 1024px){ .kpis{ grid-template-columns: repeat(2,1fr) !important; } }
@media (max-width: 680px){ .kpis{ grid-template-columns: 1fr !important; } }

/* Cards: márgenes y toque más grande en móvil */
@media (max-width: 820px){
  .card{ padding:14px; border-radius:14px; }
  .card .title{ font-size:17px; }
}

/* Sidebar link visible y usable en móvil */
section[data-testid="stSidebar"] { min-width: 260px; }
"""

# Inyecta estilos (tu styles.css + tweaks mobile)
inject_css(css_file="styles.css")
inject_css(MOBILE_TWEAKS)

# ===== HERO =====
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
      <li>Optimiza tu CV con logros medibles.</li>
      <li>Resalta habilidades clave (Python, SQL, Power BI...).</li>
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
      <div style="margin-top:.6rem; display:flex; gap:.5rem; flex-wrap:wrap;">
        <a class="btn" href="#" style="text-decoration:none; padding:.6rem .9rem; border-radius:10px;">Ver</a>
        <a class="btn" href="#" style="text-decoration:none; background:#0b5d73; padding:.6rem .9rem; border-radius:10px;">Postular</a>
      </div>
    </div>
    ''', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Logos =====
st.markdown('<div class="section"><h3>Empresas que confían</h3>', unsafe_allow_html=True)
st.markdown('<div class="logos">', unsafe_allow_html=True)
for name in ["Nómade", "MFN", "UTEM", "Betel", "CloudOps", "Acme"]:
    st.markdown(f'<div class="logo">{name}</div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Testimonios =====
st.markdown('<div class="section"><h3>Testimonios</h3>', unsafe_allow_html=True)
cols = st.columns(3)
for i, t in enumerate(TESTIMONIALS):
    with cols[i % 3]:
        st.markdown(f'''
        <div class="card">
          <p style="margin:0; font-size:16px;">“{t["q"]}”</p>
          <p class="meta" style="margin:.25rem 0 0;">{t["a"]}</p>
        </div>
        ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
# CTA principal (stack en móvil)
c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/2_Crear_Postulacion.py", label="📝 Crear Postulación")
with c2:
    st.page_link("pages/4_Postular_Con_Video.py", label="🎥 Postular con Video")

# ===== Footer =====
st.markdown(
    '<div class="footer">© {year} HumanMetrics — Todos los derechos reservados.</div>'.format(
        year=__import__("datetime").datetime.now().year
    ),
    unsafe_allow_html=True
)
