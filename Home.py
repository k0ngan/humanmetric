import streamlit as st
from utils_ui import inject_css
from dummy_data import FEATURED_JOBS, CATEGORIES, TESTIMONIALS

st.set_page_config(page_title="HumanMetrics — Empleos y Talento", layout="wide")

# Inyecta CSS base + ajustes mobile
inject_css(css_file="styles.css")
inject_css("""
/* Botones cómodos en móvil */
.stButton > button { width:100%; padding:14px 18px; font-weight:700; border-radius:12px; }

/* Hero y buscador apilados en pantallas pequeñas */
@media (max-width: 820px){
  .hero{ grid-template-columns: 1fr !important; padding:18px; border-radius:16px; }
  .searchbar{ grid-template-columns: 1fr !important; gap:10px; }
}

/* KPIs y grids colapsan */
@media (max-width: 1024px){ .kpis{ grid-template-columns: repeat(2,1fr) !important; } }
@media (max-width: 680px){ .kpis{ grid-template-columns: 1fr !important; } }

/* Cards */
@media (max-width: 820px){
  .card{ padding:14px; border-radius:14px; }
  .card .title{ font-size:17px; }
}

/* Sidebar en móvil */
section[data-testid="stSidebar"] { min-width: 260px; }
""")

# ===== HERO (HTML plano, sin f-string) =====
st.markdown(
    '''
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
''',
    unsafe_allow_html=True,
)

# ===== KPIs (HTML plano) =====
st.markdown(
    '''
<div class="kpis">
  <div class="kpi"><span>Ofertas activas</span><h3>342</h3></div>
  <div class="kpi"><span>Empresas</span><h3>84</h3></div>
  <div class="kpi"><span>Postulaciones hoy</span><h3>1,209</h3></div>
  <div class="kpi"><span>Tasa de respuesta</span><h3>92%</h3></div>
</div>
''',
    unsafe_allow_html=True,
)

# ===== Categorías =====
st.markdown('<div class="section"><h3>Explora por categorías</h3><div class="grid">', unsafe_allow_html=True)
for c in CATEGORIES:
    name = c.get("name", "")
    openings = c.get("openings", 0)
    # cada tarjeta sin f-string de bloque
    st.markdown(
        '<div class="card">'
        '<div class="title">' + str(name) + '</div>'
        '<div class="meta">' + str(openings) + ' vacantes</div>'
        '<div><span class="tag">Remoto</span><span class="tag">Híbrido</span><span class="tag">Presencial</span></div>'
        '</div>',
        unsafe_allow_html=True,
    )
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Ofertas destacadas =====
st.markdown('<div class="section"><h3>Ofertas destacadas</h3><div class="grid">', unsafe_allow_html=True)
for job in FEATURED_JOBS:
    t = job.get("t", "")
    e = job.get("e", "")
    u = job.get("u", "")
    skills_html = ''.join(['<span class="tag">' + str(s) + '</span>' for s in job.get("skills", [])])
    st.markdown(
        '<div class="card">'
        '<p class="title">' + str(t) + '</p>'
        '<p class="meta">' + str(e) + ' — ' + str(u) + '</p>'
        '<div>' + skills_html + '</div>'
        '<div style="margin-top:.6rem; display:flex; gap:.5rem; flex-wrap:wrap;">'
        '<a class="btn" href="#" style="text-decoration:none; padding:.6rem .9rem; border-radius:10px;">Ver</a>'
        '<a class="btn" href="#" style="text-decoration:none; background:#0b5d73; padding:.6rem .9rem; border-radius:10px;">Postular</a>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Logos =====
st.markdown('<div class="section"><h3>Empresas que confían</h3><div class="logos">', unsafe_allow_html=True)
for name in ["Nómade", "MFN", "UTEM", "Betel", "CloudOps", "Acme"]:
    st.markdown('<div class="logo">' + name + '</div>', unsafe_allow_html=True)
st.markdown('</div></div>', unsafe_allow_html=True)

# ===== Testimonios =====
st.markdown('<div class="section"><h3>Testimonios</h3></div>', unsafe_allow_html=True)
cols = st.columns(3)
for i, t in enumerate(TESTIMONIALS):
    quote = t.get("q", "")
    author = t.get("a", "")
    with cols[i % 3]:
        st.markdown(
            '<div class="card">'
            '<p style="margin:0; font-size:16px;">“' + str(quote) + '”</p>'
            '<p class="meta" style="margin:.25rem 0 0;">' + str(author) + '</p>'
            '</div>',
            unsafe_allow_html=True,
        )

# ===== CTA (navegación Cloud segura) =====
c1, c2 = st.columns(2)
with c1:
    st.page_link("pages/2_Crear_Postulacion.py", label="📝 Crear Postulación")
with c2:
    st.page_link("pages/4_Postular_Con_Video.py", label="🎥 Postular con Video")

# ===== Footer =====
from datetime import datetime
st.markdown(
    '<div class="footer">© ' + str(datetime.now().year) + ' HumanMetrics — Todos los derechos reservados.</div>',
    unsafe_allow_html=True,
)
