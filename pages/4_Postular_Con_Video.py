import streamlit as st

st.set_page_config(page_title="Postular con Video — HumanMetrics", layout="wide")
st.title("Postular al Cargo (Demo)")
st.caption("Formulario visual de postulación. Los videos se graban en la página y puedes descargarlos.")

st.subheader("Datos del postulante")
col1, col2 = st.columns(2)
with col1:
    rut = st.text_input("RUT", placeholder="12.345.678-9")
    nombre = st.text_input("Nombre completo", placeholder="Nombre Apellido Apellido")
with col2:
    email = st.text_input("Email", placeholder="tucorreo@dominio.cl")
    telefono = st.text_input("Teléfono (opcional)", placeholder="+56 9 1234 5678")

cv = st.file_uploader("Subir CV (PDF/DOC/DOCX)", type=["pdf","doc","docx"])

st.divider()
st.subheader("Responde en video")
st.caption("Graba desde el navegador. Al finalizar, descarga el .webm (simulado).")

QUESTIONS = [
    "Cuéntanos un proyecto reciente del que te sientas orgulloso.",
    "¿Qué te motiva del rol y cómo aportarías al equipo?",
    "Describe un desafío técnico y cómo lo resolviste."
]

def recorder(question_text: str, key_sfx: str):
    html = '''
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

      async function start(){{
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
      }}
      function stop(){{
        if(rec && rec.state !== "inactive") rec.stop();
        if(stream) {{ stream.getTracks().forEach(t => t.stop()); }}
        startBtn.disabled = false; stopBtn.disabled = true;
      }}
      startBtn.addEventListener("click", start);
      stopBtn.addEventListener("click", stop);
    </script>
    '''.format(question_text=question_text, key_sfx=key_sfx)
    st.components.v1.html(html, height=380)

for i, q in enumerate(QUESTIONS, start=1):
    recorder(q, str(i))

st.divider()
if st.button("Enviar Postulación (simulado)"):
    st.success("Postulación enviada (simulada).")
