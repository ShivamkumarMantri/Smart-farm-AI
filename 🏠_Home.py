import streamlit as st
from core.ui_setup import initialize_ui, render_footer

initialize_ui()

# ─── Hero ─────────────────────────────────────────────────────
st.markdown('<div class="main-header" style="font-size:2.4rem;font-weight:900;background:linear-gradient(90deg,#11B27B,#4ADE80);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">🌾 SmartFarm AI</div>', unsafe_allow_html=True)
st.markdown('<p style="color:#64748b;font-size:1.05rem;margin-bottom:24px;">Advanced Pathological Intelligence for Sustainable Farming</p>', unsafe_allow_html=True)

col_hero1, col_hero2 = st.columns([2, 1])

with col_hero1:
    st.image(
        "https://images.unsplash.com/photo-1523348837708-15d4a09cfac2?auto=format&fit=crop&w=800&q=80",
        use_column_width=True,
    )

with col_hero2:
    st.markdown("### 🚀 Our Mission")
    st.write("""
    SmartFarm AI leverages state-of-the-art **Deep Learning** and **Advanced AI Vision** to 
    provide farmers with instant, accurate, and actionable crop health diagnostics. 

    By identifying diseases early, we help **reduce crop loss** and minimize the use of harmful chemicals.
    """)
    if st.button("🌱 Get Started Now", type="primary", use_container_width=True):
        st.switch_page("pages/1_🩺_Diagnosis_Tool.py")

st.divider()

# ─── Stats Strip ──────────────────────────────────────────────
s1, s2, s3, s4 = st.columns(4)
s1.metric("🌿 Diseases Detected", "38+", delta="Growing")
s2.metric("🎯 Average Accuracy", "94.2%", delta="↑ 2.1%")
s3.metric("⚡ Avg Response Time", "< 3s")
s4.metric("🚀 AI Pipeline Stages", "3")

st.divider()

# ─── Technology Stack ─────────────────────────────────────────
st.header("🔬 Our Technology Stack")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="glass-card">
        <h3>🧠 Deep Learning (CNN)</h3>
        <p>A custom-trained Convolutional Neural Network analyzes leaf patterns to identify common diseases with high precision.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <h3>👁️ Advanced AI Vision</h3>
        <p>For complex cases, Gemini Vision provides deep pathological analysis to describe symptoms and estimate severity.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="glass-card">
        <h3>💾 Long-Term Memory</h3>
        <p>ChromaDB vector database allows the system to recall past diagnoses and improve accuracy over time.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ─── How It Works ─────────────────────────────────────────────
st.header("🛠️ How It Works")
hw1, hw2, hw3 = st.columns(3)
with hw1:
    st.markdown("""<div class="glass-card" style="text-align:center">
        <h2 style="font-size:2rem">📤</h2><h3>1. Upload</h3>
        <p>Take a clear photo of the affected plant leaf and upload it.</p></div>""", unsafe_allow_html=True)
with hw2:
    st.markdown("""<div class="glass-card" style="text-align:center">
        <h2 style="font-size:2rem">🧠</h2><h3>2. Analyze</h3>
        <p>Our AI pipeline processes the image through CNN → Vision → LLM.</p></div>""", unsafe_allow_html=True)
with hw3:
    st.markdown("""<div class="glass-card" style="text-align:center">
        <h2 style="font-size:2rem">📋</h2><h3>3. Report</h3>
        <p>Receive a detailed treatment plan and prevention tips instantly.</p></div>""", unsafe_allow_html=True)

# ─── Sidebar ─────────────────────────────────────────────────
st.sidebar.title("🌿 SmartFarm AI")
st.sidebar.markdown("Advanced Crop Health Diagnosis")
st.sidebar.divider()
st.sidebar.markdown("""
    > *"Precision in Diagnosis, Excellence in Harvest."*
""")

render_footer()