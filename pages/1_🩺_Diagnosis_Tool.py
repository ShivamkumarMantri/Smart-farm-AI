import os
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
from services.hybrid_predictor import hybrid_predict
from core.ui_setup import initialize_ui, render_footer

initialize_ui()

# ─── Sidebar ─────────────────────────────────────────────────
st.sidebar.title("🌿 SmartFarm AI")
st.sidebar.markdown("Advanced Crop Health Diagnosis")
st.sidebar.divider()

st.sidebar.subheader("⚙️ Settings")
force_ai = st.sidebar.checkbox(
    "🔍 Force Advanced Vision",
    help="Bypass CNN and use Gemini Vision for deeper analysis."
)

if st.sidebar.button("🧹 Reset System Cache"):
    from services.memory_service import MemoryService
    try:
        ms = MemoryService.get_instance()
        ms.reset_memory()
        st.sidebar.success("✅ Cache cleared!")
        st.toast("System reset. Next analysis will be fresh.")
        st.rerun()
    except Exception as e:
        st.sidebar.error(f"⚠️ Reset failed: {e}")

st.sidebar.divider()
st.sidebar.markdown("👨‍🌾 **Status:** Stable Release")
st.sidebar.markdown("📚 CNN + Vision + Expert AI")

# ─── Page Title ───────────────────────────────────────────────
st.title("🩺 Plant Health Diagnosis")
st.markdown("Upload a clear photo of your crop's leaf for **AI-powered disease detection and treatment advice.**")

# ─── Input Section ───────────────────────────────────────────
col_in1, col_in2 = st.columns(2)

with col_in1:
    uploaded_image = st.file_uploader(
        "📤 Upload a leaf photo",
        type=["jpg", "jpeg", "png"],
        key="leaf_upload",
    )

with col_in2:
    CROP_OPTIONS = [
        "🔍 Auto-Detect (Recommended)",
        "🍅 Tomato", "🥔 Potato", "🌽 Corn / Maize",
        "🌾 Wheat", "🍇 Grape", "🍎 Apple", "🌶️ Pepper",
        "🍓 Strawberry", "🫐 Blueberry", "🍊 Orange",
        "🌻 Sunflower", "🍑 Peach", "🍒 Cherry", "🫘 Soybean",
        "🌿 Other"
    ]
    crop_selection = st.selectbox("🌱 Select Your Crop", CROP_OPTIONS)
    user_crop = None if crop_selection.startswith("🔍") else crop_selection.split(" ", 1)[1].strip()

analyze_button = st.button("🔍 Run Diagnosis", type="primary", use_container_width=True)

# ─── Processing & Results ────────────────────────────────────
if uploaded_image and analyze_button:
    with st.spinner("🌿 Analyzing plant health... please wait ⏳"):
        upload_dir = "data/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        image_path = os.path.join(upload_dir, uploaded_image.name)
        image = Image.open(uploaded_image).convert("RGB")
        image.save(image_path)

        result = hybrid_predict(
            image_path,
            user_crop=user_crop,
            force_gemini=force_ai
        )

    if result["stage"] == "error":
        st.error(result["message"])
    else:
        st.success("✅ Analysis Complete!")

        res_col1, res_col2 = st.columns([1, 2])

        with res_col1:
            st.image(image, caption="Uploaded Leaf Image", use_column_width=True)
            
            # ── Confidence Gauge ──────────────────────────
            meta = result.get("metadata", {})
            conf = meta.get("cnn_conf", 0.0)
            
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=round(conf * 100, 1),
                number={"suffix": "%", "font": {"size": 28, "color": "#4ADE80"}},
                title={"text": "AI Confidence", "font": {"size": 14, "color": "#94A3B8"}},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "#475569"},
                    "bar": {"color": "#11B27B"},
                    "bgcolor": "rgba(0,0,0,0)",
                    "steps": [
                        {"range": [0, 50], "color": "rgba(239,68,68,0.15)"},
                        {"range": [50, 75], "color": "rgba(234,179,8,0.15)"},
                        {"range": [75, 100], "color": "rgba(17,178,123,0.15)"},
                    ],
                    "threshold": {
                        "line": {"color": "#4ADE80", "width": 3},
                        "thickness": 0.75,
                        "value": conf * 100,
                    },
                },
            ))
            fig.update_layout(
                height=220,
                margin=dict(t=30, b=10, l=20, r=20),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font={"color": "#E2E8F0"},
            )
            st.plotly_chart(fig, use_container_width=True)

        with res_col2:
            st.subheader("🌿 Diagnosis Result")

            if result["stage"] == "gemini_vision_grok":
                st.info("🧬 **Mode:** Advanced AI Vision (Deep Analysis)")
            elif result["stage"] == "cnn_grok":
                st.success("🧠 **Mode:** Standard CNN Diagnosis")
            elif result["stage"] == "cached_result":
                st.info("⚡ **Mode:** Result loaded from Cache")

            st.markdown("### 🧠 Analysis Summary")
            st.markdown(result["message"], unsafe_allow_html=True)

            # ── Quick Action Checklist ──────────────────────
            st.markdown("---")
            st.markdown("### ✅ Recommended Actions")
            actions = [
                "📸 Take more photos over the next 3 days to monitor progress.",
                "💧 Avoid over-watering — check soil moisture daily.",
                "🌬️ Improve air circulation around affected plants.",
                "🧴 Apply a suitable fungicide/pesticide as advised above.",
                "🌱 Isolate severely affected plants to prevent spread.",
                "📞 Consult a local agricultural expert if symptoms worsen.",
            ]
            for action in actions:
                st.checkbox(action, key=f"chk_{action[:20]}")

            # ── Download Report ─────────────────────────────
            st.markdown("---")
            report_text = f"""
SmartFarm AI — Diagnosis Report
================================
Crop       : {user_crop or 'Auto-Detected'}
Confidence : {conf:.1%}
Mode       : {result['stage']}
Timestamp  : {result.get('timestamp', 'N/A')}

--- Analysis Summary ---
{result['message']}

--- Recommended Actions ---
1. Monitor plant over next 3 days.
2. Avoid over-watering.
3. Improve air circulation.
4. Apply suitable fungicide as advised.
5. Isolate severely affected plants.
6. Consult local agricultural expert if needed.

Generated by SmartFarm AI 2025-26
            """.strip()

            st.download_button(
                label="📥 Download Report",
                data=report_text,
                file_name="smartfarm_diagnosis.txt",
                mime="text/plain",
                use_container_width=True,
            )

render_footer()
