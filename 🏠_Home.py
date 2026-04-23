import streamlit as st
from core.ui_setup import initialize_ui, render_footer
initialize_ui()

# ── HERO ─────────────────────────────────────────────────────
st.markdown("""
<div class="sf-hero">
    <div class="sf-hero-tag"><div class="sf-hero-tag-dot"></div> Now with Gemini Vision + Grok LLM</div>
    <div class="sf-hero-heading">
        <span class="white">AI-Powered</span><br>
        <span class="grad">Crop Diagnosis</span>
    </div>
    <div class="sf-hero-sub">
        Upload a photo of your crop leaf. Our AI pipeline detects diseases, analyzes symptoms,
        and delivers a complete treatment plan — in under 10 seconds.
    </div>
    <div class="sf-hero-btns">
        <a class="sf-btn-primary" href="#">📤 Upload Image</a>
        <a class="sf-btn-secondary" href="#">Explore Features →</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ── TRUST STATS ───────────────────────────────────────────────
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
c1,c2,c3,c4 = st.columns(4)
for col, num, label in [
    (c1, "38+",   "Diseases Detected"),
    (c2, "94.2%", "CNN Accuracy"),
    (c3, "<3s",   "Avg Response Time"),
    (c4, "3",     "AI Pipeline Stages"),
]:
    with col:
        st.markdown(f"""
        <div class="sf-stat">
            <div class="sf-stat-num">{num}</div>
            <div class="sf-stat-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:56px'></div>", unsafe_allow_html=True)

# ── FEATURES ──────────────────────────────────────────────────
st.markdown("""
<div class="sf-section-label">Features</div>
<div class="sf-section-heading">Everything you need to protect your crops</div>
<div class="sf-section-sub">From detection to treatment, SmartFarm AI handles the entire diagnostic pipeline.</div>
""", unsafe_allow_html=True)

f1,f2 = st.columns(2)
features = [
    ("green",  "🧠", "Disease Detection",         "Custom-trained CNN analyzes leaf patterns to detect 38+ plant diseases with up to 94% accuracy."),
    ("teal",   "👁️", "AI Vision Analysis",         "Gemini Vision provides deep pathological analysis for complex cases, estimating severity and spread."),
    ("violet", "📊", "Farm History Tracking",      "ChromaDB vector memory stores every diagnosis, enabling long-term trend tracking across your farm."),
    ("amber",  "💡", "Smart Recommendations",      "Grok LLM synthesizes all data into plain-language, actionable treatment plans tailored for farmers."),
]
for i,(col,(color,icon,title,body)) in enumerate(zip([f1,f2,f1,f2], features)):
    with col:
        st.markdown(f"""
        <div class="sf-card">
            <div class="sf-card-icon {color}">{icon}</div>
            <div class="sf-card-title">{title}</div>
            <div class="sf-card-body">{body}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:56px'></div>", unsafe_allow_html=True)

# ── HOW IT WORKS ──────────────────────────────────────────────
hw_col, _ = st.columns([3,2])
with hw_col:
    st.markdown("""
    <div class="sf-section-label">How It Works</div>
    <div class="sf-section-heading">Three steps to a healthier farm</div>
    <div class="sf-section-sub" style="margin-bottom:28px">Our AI pipeline runs automatically. No expertise required.</div>
    """, unsafe_allow_html=True)

    steps = [
        ("01", "📤 Upload",  "Take a clear photo of the affected leaf and upload it via drag-and-drop or file picker."),
        ("02", "🧠 Analyze", "Our 3-stage AI pipeline — CNN → Vision → LLM — processes the image in seconds."),
        ("03", "📋 Results", "Receive a full diagnosis: disease name, confidence score, and step-by-step treatment plan."),
    ]
    for num,title,body in steps:
        st.markdown(f"""
        <div class="sf-step">
            <div class="sf-step-num">{num}</div>
            <div>
                <div class="sf-step-title">{title}</div>
                <div class="sf-step-body">{body}</div>
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown("<div style='height:56px'></div>", unsafe_allow_html=True)

# ── TRUST SECTION ─────────────────────────────────────────────
st.markdown("""
<div class="sf-section-label">Trusted Technology</div>
<div class="sf-section-heading">Built on world-class AI infrastructure</div>
<div class="sf-section-sub">SmartFarm AI integrates the most advanced models available.</div>
""", unsafe_allow_html=True)

t1,t2,t3 = st.columns(3)
trust = [
    ("🧠", "TensorFlow CNN",     "Custom-trained convolutional neural network with optimized architecture for plant pathology."),
    ("👁️", "Google Gemini",      "State-of-the-art multimodal AI for advanced image understanding and symptom description."),
    ("💬", "Grok (Groq LLM)",    "Fast, intelligent language model generating expert-level, farmer-friendly treatment advice."),
]
for col,(icon,title,body) in zip([t1,t2,t3], trust):
    with col:
        st.markdown(f"""
        <div class="sf-card" style="text-align:center">
            <div style="font-size:2rem;margin-bottom:12px">{icon}</div>
            <div class="sf-card-title" style="text-align:center">{title}</div>
            <div class="sf-card-body" style="text-align:center">{body}</div>
        </div>""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────
st.sidebar.markdown("### 🌾 SmartFarm AI")
st.sidebar.markdown("<span style='color:#475569;font-size:0.85rem'>AI-powered plant disease detection</span>", unsafe_allow_html=True)
st.sidebar.divider()
if st.sidebar.button("🩺 Go to Diagnosis Tool", use_container_width=True):
    st.switch_page("pages/1_🩺_Diagnosis_Tool.py")
st.sidebar.divider()
st.sidebar.markdown("<span style='color:#334155;font-size:0.75rem'>Version 3.0 · Stable Release</span>", unsafe_allow_html=True)

render_footer()