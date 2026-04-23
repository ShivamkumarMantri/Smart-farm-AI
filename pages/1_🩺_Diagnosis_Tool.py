import os
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
from services.hybrid_predictor import hybrid_predict
from core.ui_setup import initialize_ui, render_footer
initialize_ui()

# ── Sidebar ───────────────────────────────────────────────────
st.sidebar.markdown("### ⚙️ Diagnosis Settings")
st.sidebar.markdown("<span style='color:#475569;font-size:0.82rem'>Configure AI analysis options</span>", unsafe_allow_html=True)
st.sidebar.divider()

force_ai = st.sidebar.toggle("🔍 Force Advanced Vision", value=False,
    help="Skip CNN and use Gemini Vision AI for deep analysis")

if st.sidebar.button("🧹 Clear System Cache", use_container_width=True):
    from services.memory_service import MemoryService
    try:
        MemoryService.get_instance().reset_memory()
        st.sidebar.success("✅ Cache cleared!")
        st.toast("🗑️ Cache cleared. Next analysis will be fresh.", icon="✅")
        st.rerun()
    except Exception as e:
        st.sidebar.error(f"⚠️ {e}")

st.sidebar.divider()
st.sidebar.markdown("<span style='color:#334155;font-size:0.75rem'>SmartFarm AI v3.0 · Stable</span>", unsafe_allow_html=True)

# ── Page Header ───────────────────────────────────────────────
st.markdown("""
<div style="padding:20px 0 8px">
    <div class="sf-section-label">Diagnosis Tool</div>
    <div class="sf-section-heading">Plant Health Analysis</div>
    <div class="sf-section-sub">Upload a clear leaf photo. Our 3-stage AI pipeline returns results in seconds.</div>
</div>
""", unsafe_allow_html=True)

# ── Input Section ─────────────────────────────────────────────
in1, in2 = st.columns([3, 2])
with in1:
    uploaded_image = st.file_uploader("📤 Drop your leaf image here", type=["jpg","jpeg","png"], key="leaf_upload",
        help="Works best with clear, well-lit photos of a single leaf")
with in2:
    CROPS = [
        "🔍 Auto-Detect (Recommended)",
        "🍅 Tomato","🥔 Potato","🌽 Corn / Maize","🌾 Wheat",
        "🍇 Grape","🍎 Apple","🌶️ Pepper","🍓 Strawberry",
        "🫐 Blueberry","🍊 Orange","🌻 Sunflower","🍑 Peach",
        "🍒 Cherry","🫘 Soybean","🌿 Other"
    ]
    crop_sel = st.selectbox("🌱 Crop Type", CROPS)
    user_crop = None if crop_sel.startswith("🔍") else crop_sel.split(" ",1)[1].strip()

analyze = st.button("⚡ Run AI Diagnosis", type="primary", use_container_width=True)

# ── Processing ────────────────────────────────────────────────
if uploaded_image and analyze:
    with st.spinner("🌿 Analyzing your crop with AI..."):
        upload_dir = "data/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        image_path = os.path.join(upload_dir, uploaded_image.name)
        image = Image.open(uploaded_image).convert("RGB")
        image.save(image_path)
        result = hybrid_predict(image_path, user_crop=user_crop, force_gemini=force_ai)

    if result["stage"] == "error":
        st.error(f"⚠️ {result['message']}")
    else:
        st.toast("✅ Diagnosis complete!", icon="🌿")

        img_col, res_col = st.columns([1, 2])
        meta = result.get("metadata", {})
        conf = meta.get("cnn_conf", 0.0)
        label = meta.get("cnn_label", "Unknown").replace("_", " ")

        with img_col:
            st.image(image, caption="Uploaded Leaf", use_column_width=True)

            # Confidence Gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=round(conf * 100, 1),
                number={"suffix":"%","font":{"size":26,"color":"#34D399"}},
                title={"text":"AI Confidence","font":{"size":12,"color":"#475569"}},
                gauge={
                    "axis":{"range":[0,100],"tickcolor":"#334155"},
                    "bar":{"color":"#10B981"},
                    "bgcolor":"rgba(0,0,0,0)",
                    "steps":[
                        {"range":[0,50],"color":"rgba(239,68,68,0.08)"},
                        {"range":[50,75],"color":"rgba(234,179,8,0.08)"},
                        {"range":[75,100],"color":"rgba(16,185,129,0.08)"},
                    ],
                    "threshold":{"line":{"color":"#34D399","width":2},"thickness":0.75,"value":conf*100},
                },
            ))
            fig.update_layout(height=190, margin=dict(t=30,b=5,l=15,r=15),
                paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                font={"color":"#94A3B8"})
            st.plotly_chart(fig, use_container_width=True)

        with res_col:
            # Result Card
            mode_badge = {"gemini_vision_grok":"🧬 Advanced Vision","cnn_grok":"🧠 CNN Diagnosis","cached_result":"⚡ Cached Result"}.get(result["stage"],"🔬 Analysis")
            st.markdown(f"""
            <div class="sf-result">
                <div class="sf-result-badge">{mode_badge}</div>
                <div class="sf-disease-name">{label}</div>
                <div class="sf-confidence">Confidence: <span>{conf:.1%}</span></div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
            st.markdown("**📋 AI Analysis**")
            st.markdown(result["message"], unsafe_allow_html=True)

            st.divider()
            st.markdown("**✅ Action Checklist**")
            actions = [
                "Monitor plant over the next 48–72 hours",
                "Avoid overhead watering to reduce humidity",
                "Improve air circulation between plants",
                "Apply appropriate fungicide/pesticide as advised",
                "Isolate severely affected plants immediately",
                "Consult a local agronomist if symptoms worsen",
            ]
            for a in actions:
                st.checkbox(a, key=f"a_{a[:15]}")

            st.divider()
            report = f"""SmartFarm AI — Diagnosis Report
=================================
Crop       : {user_crop or 'Auto-Detected'}
Disease    : {label}
Confidence : {conf:.1%}
Mode       : {result['stage']}
Timestamp  : {result.get('timestamp','N/A')}

── Analysis ──────────────────────────
{result['message']}

── Recommended Actions ───────────────
1. Monitor plant over next 48-72 hours.
2. Avoid overhead watering.
3. Improve air circulation.
4. Apply appropriate fungicide/pesticide.
5. Isolate severely affected plants.
6. Consult a local agronomist if needed.

Generated by SmartFarm AI v3.0"""
            st.download_button("📥 Download Report", data=report,
                file_name="smartfarm_diagnosis.txt", mime="text/plain", use_container_width=True)

render_footer()
