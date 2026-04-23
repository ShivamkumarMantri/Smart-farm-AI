import os
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
from collections import Counter
from services.hybrid_predictor import hybrid_predict
from core.ui_setup import initialize_ui, render_footer
initialize_ui()

# ── Sidebar ───────────────────────────────────────────────────
st.sidebar.markdown("### ⚙️ Diagnosis Settings")
st.sidebar.markdown("<span style='color:#475569;font-size:0.82rem'>Configure AI analysis options</span>", unsafe_allow_html=True)
st.sidebar.divider()

force_ai = st.sidebar.toggle("🔍 Force Advanced Vision", value=False,
    help="Skip CNN and use Gemini Vision for deep analysis")

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
    <div class="sf-section-sub">Upload up to 3 leaf photos for AI-powered disease detection. Multi-image analysis improves accuracy.</div>
</div>
""", unsafe_allow_html=True)

# ── Input Section ─────────────────────────────────────────────
in1, in2 = st.columns([3, 2])
with in1:
    uploaded_files = st.file_uploader(
        "📤 Drop leaf images here (up to 3 for best accuracy)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
        key="leaf_upload",
        help="Upload 1-3 clear, well-lit photos of the same plant from different angles"
    )
    # Limit to 3
    if uploaded_files and len(uploaded_files) > 3:
        st.warning("⚠️ Maximum 3 images allowed. Using the first 3.")
        uploaded_files = uploaded_files[:3]

with in2:
    CROPS = [
        "🔍 Auto-Detect (Recommended)",
        "🍅 Tomato","🥔 Potato","🌽 Corn / Maize","🌾 Wheat",
        "🍇 Grape","🍎 Apple","🌶️ Pepper","🍓 Strawberry",
        "🫐 Blueberry","🍊 Orange","🌻 Sunflower","🍑 Peach",
        "🍒 Cherry","🫘 Soybean","🌿 Other"
    ]
    crop_sel = st.selectbox("🌱 Crop Type", CROPS)
    user_crop = None if crop_sel.startswith("🔍") else crop_sel.split(" ", 1)[1].strip()

    city_input = st.text_input(
        "📍 Your Location (Optional)",
        placeholder="e.g. Mumbai, Delhi, Pune",
        help="Enter your city to get weather-aware treatment advice"
    )

analyze = st.button("⚡ Run AI Diagnosis", type="primary", use_container_width=True)

# ── Processing ────────────────────────────────────────────────
if uploaded_files and analyze:
    # ── Fetch weather silently ────────────────────────────────
    weather_data = None
    weather_context = None
    if city_input.strip():
        with st.spinner("🌦️ Fetching weather data..."):
            try:
                from services.weather_service import get_weather, weather_farming_advice
                weather_data = get_weather(city_input.strip())
                if weather_data:
                    weather_context = f"{weather_data['summary']} | Farming advice: {weather_farming_advice(weather_data)}"
            except Exception:
                pass  # Weather is optional — never block diagnosis

    # ── Run predictions ───────────────────────────────────────
    with st.spinner(f"🌿 Analyzing {'your images' if len(uploaded_files) > 1 else 'your image'} with AI..."):
        upload_dir = "data/uploads"
        os.makedirs(upload_dir, exist_ok=True)

        all_results = []
        saved_images = []

        for uf in uploaded_files:
            image_path = os.path.join(upload_dir, uf.name)
            img = Image.open(uf).convert("RGB")
            img.save(image_path)
            saved_images.append(img)

            res = hybrid_predict(image_path, user_crop=user_crop,
                                 force_gemini=force_ai, weather_context=weather_context)
            all_results.append(res)

    # ── Majority vote (multi-image) ───────────────────────────
    valid = [r for r in all_results if r["stage"] != "error"]
    if not valid:
        st.error("⚠️ All predictions failed. " + all_results[0].get("message", "Please try again."))
        st.stop()

    # Use majority vote on CNN label for the best result
    labels = [r["metadata"].get("cnn_label", "Unknown") for r in valid]
    winner_label = Counter(labels).most_common(1)[0][0]
    # Use the result whose label matches the majority vote (pick highest conf among them)
    matching = [r for r in valid if r["metadata"].get("cnn_label") == winner_label]
    result = max(matching, key=lambda r: r["metadata"].get("cnn_conf", 0))
    meta = result.get("metadata", {})
    conf = meta.get("cnn_conf", 0.0)
    label = meta.get("cnn_label", "Unknown").replace("_", " ")

    st.toast("✅ Diagnosis complete!", icon="🌿")

    # ── Weather Info Card ─────────────────────────────────────
    if weather_data:
        wc = weather_data
        st.markdown(f"""
        <div class="sf-card" style="margin-bottom:20px;padding:18px 24px;
             background:rgba(6,182,212,0.04);border-color:rgba(6,182,212,0.15)">
            <span style="font-size:0.7rem;font-weight:700;letter-spacing:1px;
                  text-transform:uppercase;color:#06B6D4">🌦️ Weather Context · {wc['location']}</span>
            <div style="margin-top:8px;display:flex;gap:24px;flex-wrap:wrap">
                <span style="color:#94A3B8;font-size:0.84rem">🌡️ <strong style="color:#E2E8F0">{wc['temp']}°C</strong></span>
                <span style="color:#94A3B8;font-size:0.84rem">💧 <strong style="color:#E2E8F0">{wc['humidity']}% humidity</strong></span>
                <span style="color:#94A3B8;font-size:0.84rem">🌧️ <strong style="color:#E2E8F0">{wc['rain']} mm rain</strong></span>
                <span style="color:#94A3B8;font-size:0.84rem">💨 <strong style="color:#E2E8F0">{wc['wind']} km/h wind</strong></span>
                <span style="color:#94A3B8;font-size:0.84rem">📅 <strong style="color:#E2E8F0">Tomorrow: {wc['tomorrow_rain']} mm forecast</strong></span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Multi-image preview ───────────────────────────────────
    if len(saved_images) > 1:
        st.markdown(f"<div style='color:#475569;font-size:0.8rem;margin-bottom:8px'>📸 Analyzed {len(saved_images)} images · Majority vote applied</div>", unsafe_allow_html=True)
        img_cols = st.columns(len(saved_images))
        for col, img, res in zip(img_cols, saved_images, all_results):
            with col:
                lbl = res["metadata"].get("cnn_label","?").replace("_"," ")
                c = res["metadata"].get("cnn_conf", 0)
                tick = "✅" if lbl == winner_label.replace("_"," ") else "⬜"
                st.image(img, caption=f"{tick} {lbl} ({c:.0%})", use_column_width=True)

    # ── Main Result ───────────────────────────────────────────
    img_col, res_col = st.columns([1, 2])

    with img_col:
        if len(saved_images) == 1:
            st.image(saved_images[0], caption="Uploaded Leaf", use_column_width=True)

        # Confidence Gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=round(conf * 100, 1),
            number={"suffix": "%", "font": {"size": 26, "color": "#34D399"}},
            title={"text": "AI Confidence", "font": {"size": 12, "color": "#475569"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#334155"},
                "bar": {"color": "#10B981"},
                "bgcolor": "rgba(0,0,0,0)",
                "steps": [
                    {"range": [0, 50],  "color": "rgba(239,68,68,0.08)"},
                    {"range": [50, 75], "color": "rgba(234,179,8,0.08)"},
                    {"range": [75, 100],"color": "rgba(16,185,129,0.08)"},
                ],
                "threshold": {"line": {"color": "#34D399", "width": 2}, "thickness": 0.75, "value": conf * 100},
            },
        ))
        fig.update_layout(height=190, margin=dict(t=30, b=5, l=15, r=15),
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "#94A3B8"})
        st.plotly_chart(fig, use_container_width=True)

    with res_col:
        mode_badge = {
            "gemini_vision_grok": "🧬 Advanced Vision",
            "cnn_grok": "🧠 CNN Diagnosis",
            "cached_result": "⚡ Cached Result"
        }.get(result["stage"], "🔬 Analysis")

        st.markdown(f"""
        <div class="sf-result">
            <div class="sf-result-badge">{mode_badge}</div>
            <div class="sf-disease-name">{label}</div>
            <div class="sf-confidence">Confidence: <span>{conf:.1%}</span>
            {"&nbsp;·&nbsp; <span style='color:#06B6D4'>🌦️ Weather-aware advice included</span>" if weather_data else ""}
            </div>
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
Images     : {len(saved_images)} analyzed
Timestamp  : {result.get('timestamp', 'N/A')}
{f"Location   : {weather_data['location']}" if weather_data else ""}
{f"Weather    : {weather_data['condition']}, {weather_data['temp']}°C, {weather_data['humidity']}% humidity" if weather_data else ""}

── AI Analysis ───────────────────────
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
