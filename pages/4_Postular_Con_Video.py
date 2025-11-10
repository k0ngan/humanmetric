import streamlit as st

st.set_page_config(page_title="Postular con Video — HumanMetrics", layout="wide")

# ==============================
# Descripción del cargo (visible al postulante)
# ==============================
st.title("Analista de Experiencia del Cliente")
st.caption("Área: Experiencia del Cliente y Mejora de Procesos · Ubicación: Lima, Perú")

st.subheader("🎯 Propósito del Cargo")
st.write("""
Diseñar, analizar y ejecutar iniciativas orientadas a optimizar la experiencia del cliente en canales presenciales y digitales,
garantizando una atención eficiente, empática y alineada con los estándares de servicio del banco. Contribuir a la mejora continua
de procesos mediante el seguimiento de indicadores y la implementación de proyectos de optimización.
""")

with st.expander("🧩 Responsabilidades", expanded=True):
    st.markdown("""
- Analizar y monitorear NPS, tiempos de atención, reclamos y resolución de casos.  
- Levantar oportunidades de mejora a partir de datos y retroalimentación de usuarios.  
- Diseñar flujos y propuestas que reduzcan tiempos de respuesta y mejoren la eficiencia operativa.  
- Coordinar proyectos con áreas internas; comunicación con equipos técnicos y gerenciales.  
- Elaborar reportes y presentaciones para jefaturas y comités.  
- Implementar herramientas en Excel y otras plataformas para automatizar reportes y análisis.  
- Documentar procesos, metodologías y resultados.  
- Promover una cultura de servicio basada en empatía, respeto y mejora continua.
""")

with st.expander("📋 Requisitos", expanded=True):
    st.markdown("""
- Estudiante avanzado o egresado de Ingeniería Industrial, Administración o afín.  
- ≥1 año en atención al cliente o análisis de procesos.  
- Excel intermedio/avanzado y herramientas de gestión (Google Workspace, Trello, **Power BI** deseable).  
- Habilidades analíticas, comunicación efectiva, trabajo en equipo.  
- Capacidad para entornos dinámicos y bajo presión.  
- Español nativo; Inglés intermedio (deseable).
""")

with st.expander("💡 Deseables", expanded=False):
    st.markdown("""
- Gestión de proyectos o mejora continua (Lean/Six Sigma básico).  
- Automatización de reportes (macros u otras herramientas).  
- Experiencia en atención digital o transformación del servicio al cliente.
""")

with st.expander("📈 Indicadores de Éxito (KPIs)", expanded=False):
    st.markdown("""
- Reducción de tiempos de atención ≥ 30%.  
- Incremento del NPS u otras métricas de satisfacción.  
- Cumplimiento de plazos y entregables de proyectos.  
- Implementación de reportes automatizados o dashboards funcionales.
""")

st.divider()

# ==============================
# Formulario de Postulación
# ==============================
st.subheader("📝 Datos del Postulante")
col1, col2 = st.columns(2)
with col1:
    rut = st.text_input("RUT", placeholder="12.345.678-9")
    nombre = st.text_input("Nombre completo", placeholder="Nombre Apellido Apellido")
with col2:
    email = st.text_input("Email", placeholder="tucorreo@dominio.cl")
    telefono = st.text_input("Teléfono (opcional)", placeholder="+51 9 1234 5678")

cv = st.file_uploader("Subir CV (PDF/DOC/DOCX)", type=["pdf", "doc", "docx"])

st.divider()
st.subheader("🎥 Responde en video")
st.caption("Graba desde el navegador. Al finalizar, podrás **descargar** el archivo .webm (cliente).")

QUESTIONS = [
    "Cuéntanos un proyecto reciente del que te sientas orgulloso.",
    "¿Qué te motiva del rol y cómo aportarías al equipo?",
    "Describe un desafío técnico y cómo lo resolviste."
]

def recorder(question_text: str, key_sfx: str):
    # Grabación en cliente con MediaRecorder (no sube archivos; entrega enlace de descarga local)
    html = f'''
    <div style="padding:12px; border:1px solid #1E293B; border-radius:12px;">
      <div style="font-weight:600; margin-bottom:6px;">{question_text}</div>
      <video id="v_{key_sfx}" autoplay playsinline muted style="width:100%; max-height:260px; background:#000; border-radius:8px;"></video>
      <div style="display:flex; gap:8px; margin-top:8px;">
        <button id="start_{key_sfx}" style="padding:8px 12px; border-radius:8px; background:#0E7490; color:#fff; border:0;">Iniciar</button>
        <button id="stop_{key_sfx}" style="padding:8px 12px; border-radius:8px; background:#334155; color:#fff; border:0;" disabled>Detener</button>
        <a id="dl_{key_sfx}" style="padding:8px 12px; border-radius:8px; background:#065f46; color:#fff; text-decoration:none; display:none;">Descargar video</a>
      </div>
      <div id="msg_{key_sfx}" style="color:#94A3B8; font-size:12px; margin-top:6px;">Permite acceso a tu cámara y micrófono para grabar.</div>
    </div>
    <script>
      const v = document.getElementById("v_{key_sfx}");
      const startBtn = document.getElementById("start_{key_sfx}");
      const stopBtn = document.getElementById("stop_{key_sfx}");
      const dl = document.getElementById("dl_{key_sfx}");
      const msg = document.getElementById("msg_{key_sfx}");
      let stream = null, rec = null, chunks = [];

      async function start(){
        try{{
          stream = await navigator.mediaDevices.getUserMedia({{video:true, audio:true}});
          v.srcObject = stream;
          chunks = [];
          rec = new MediaRecorder(stream, {{mimeType: "video/webm"}});
          rec.ondataavailable = e => {{ if(e.data.size>0) chunks.push(e.data); }};
          rec.onstop = () => {{
            const blob = new Blob(chunks, {{type:"video/webm"}});
            const url = URL.createObjectURL(blob);
            dl.href = url; dl.download = "respuesta_{key_sfx}.webm";
            dl.style.display = "inline-block";
            msg.textContent = "Grabación lista. Descarga el archivo .webm.";
          }};
          rec.start();
          startBtn.disabled = true; stopBtn.disabled = false;
          msg.textContent = "Grabando...";
        }}catch(err){{
          console.error(err);
          msg.textContent = "No se pudo acceder a la cámara/micrófono.";
        }}
      }
      function stop(){{
        if(rec && rec.state !== "inactive") rec.stop();
        if(stream) {{ stream.getTracks().forEach(t => t.stop()); }}
        startBtn.disabled = false; stopBtn.disabled = true;
      }}
      startBtn.addEventListener("click", start);
      stopBtn.addEventListener("click", stop);
    </script>
    '''
    st.components.v1.html(html, height=380)

for i, q in enumerate(QUESTIONS, start=1):
    recorder(q, str(i))

st.divider()
if st.button("Enviar Postulación (simulado)"):
    st.success("Postulación enviada (simulada).")
    st.write({
        "rut": rut,
        "nombre": nombre,
        "email": email,
        "telefono": telefono,
        "cv_subido": "Sí" if cv else "No",
        "videos": "Grabados en el navegador y descargados como .webm (cliente)"
    })
