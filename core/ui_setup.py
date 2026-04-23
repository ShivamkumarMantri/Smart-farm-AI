import streamlit as st

def inject_global_styles():
    """Injects a premium header, footer, and full design system CSS."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

        /* ─── Base ─── */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        /* ─── Hide default Streamlit header/footer ─── */
        #MainMenu { visibility: hidden; }
        header[data-testid="stHeader"] { display: none !important; }
        footer { display: none !important; }

        /* ─── Custom Header ─── */
        .sf-header {
            position: sticky;
            top: 0;
            z-index: 999;
            width: 100%;
            padding: 12px 32px;
            background: rgba(10, 15, 20, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(17, 178, 123, 0.25);
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 24px;
        }
        .sf-header-brand {
            font-size: 1.3rem;
            font-weight: 900;
            background: linear-gradient(90deg, #11B27B, #4ADE80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            letter-spacing: -0.5px;
        }
        .sf-header-tagline {
            font-size: 0.8rem;
            color: #64748b;
            font-weight: 500;
        }
        .sf-header-badge {
            background: rgba(17,178,123,0.15);
            color: #4ADE80;
            border: 1px solid rgba(17,178,123,0.4);
            border-radius: 20px;
            padding: 4px 14px;
            font-size: 0.75rem;
            font-weight: 600;
        }

        /* ─── Custom Footer ─── */
        .sf-footer {
            margin-top: 60px;
            padding: 28px 32px;
            background: rgba(10, 15, 20, 0.7);
            backdrop-filter: blur(12px);
            border-top: 1px solid rgba(17, 178, 123, 0.2);
            text-align: center;
        }
        .sf-footer p {
            margin: 0;
            font-size: 0.82rem;
            color: #475569;
        }
        .sf-footer span {
            color: #11B27B;
            font-weight: 600;
        }
        .sf-footer .sf-footer-links {
            margin-top: 8px;
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .sf-footer .sf-footer-links a {
            color: #64748b;
            text-decoration: none;
            font-size: 0.8rem;
            transition: color 0.2s;
        }
        .sf-footer .sf-footer-links a:hover {
            color: #4ADE80;
        }

        /* ─── Buttons ─── */
        div.stButton > button {
            border: none;
            border-radius: 12px;
            background: linear-gradient(135deg, #11B27B 0%, #0D8F61 100%);
            color: white;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(17, 178, 123, 0.3);
            transition: all 0.3s ease;
        }
        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(17, 178, 123, 0.5) !important;
            color: #ffffff;
            background: linear-gradient(135deg, #13D190 0%, #0D8F61 100%);
        }

        /* ─── Titles ─── */
        h1 {
            background: linear-gradient(90deg, #11B27B, #4ADE80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
        }
        h2 { color: #E2E8F0 !important; font-weight: 700; }
        h3 { color: #4ADE80 !important; font-weight: 600; }

        /* ─── Input ─── */
        input, .stSelectbox > div > div {
            border-radius: 8px !important;
            border: 1px solid rgba(17, 178, 123, 0.5) !important;
        }

        /* ─── File Uploader ─── */
        div[data-testid="stFileUploader"] {
            border: 2px dashed #11B27B;
            border-radius: 15px;
            padding: 1.5rem;
            background-color: rgba(17, 178, 123, 0.05);
            transition: all 0.3s ease;
        }
        div[data-testid="stFileUploader"]:hover {
            background-color: rgba(17, 178, 123, 0.1);
            border-color: #4ADE80;
        }

        /* ─── Glass Cards ─── */
        .glass-card {
            background: rgba(30, 36, 43, 0.6);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            border: 1px solid rgba(17, 178, 123, 0.3);
        }

        /* ─── Sidebar ─── */
        section[data-testid="stSidebar"] {
            background-color: #0A0F14;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }

        /* ─── Badge ─── */
        .badge {
            background: rgba(17, 178, 123, 0.2);
            color: #4ADE80;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid rgba(17, 178, 123, 0.4);
            display: inline-block;
        }

        /* ─── Spinner ─── */
        .stSpinner > div > div {
            border-top-color: #4ADE80 !important;
        }

        /* ─── Metrics ─── */
        [data-testid="stMetric"] {
            background: rgba(30,36,43,0.5);
            border: 1px solid rgba(17,178,123,0.15);
            border-radius: 12px;
            padding: 14px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
        <div class="sf-header">
            <div>
                <div class="sf-header-brand">🌾 SmartFarm AI</div>
                <div class="sf-header-tagline">Advanced Pathological Intelligence for Sustainable Farming</div>
            </div>
            <div class="sf-header-badge">🟢 System Operational</div>
        </div>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown("""
        <div class="sf-footer">
            <p>🌿 <span>SmartFarm AI</span> &nbsp;|&nbsp; 2025–26 &nbsp;|&nbsp; Developed by Team SmartFarm</p>
            <p style="margin-top:4px;">Powered by <span>CNN</span> + <span>Gemini Vision</span> + <span>Grok LLM</span> + <span>ChromaDB</span></p>
            <div class="sf-footer-links">
                <a href="#">🏠 Home</a>
                <a href="#">🩺 Diagnosis</a>
                <a href="#">📊 Analytics</a>
                <a href="#">📖 About</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

def initialize_ui():
    """Full UI initialization: styles + header."""
    inject_global_styles()
    render_header()
