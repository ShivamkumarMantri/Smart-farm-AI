import streamlit as st

def inject_global_styles():
    """Professional, enterprise-grade design system."""
    st.markdown("""
        <style>
        /* ══════════════════════════════════════════
           FONTS
           ══════════════════════════════════════════ */
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', -apple-system, sans-serif !important;
        }

        /* ══════════════════════════════════════════
           PROFESSIONAL BACKGROUND GRADIENT
           ══════════════════════════════════════════ */
        .stApp {
            background: linear-gradient(135deg,
                #060B14 0%,
                #0A1628 30%,
                #071220 60%,
                #040C18 100%) !important;
        }
        .main .block-container {
            background:
                radial-gradient(ellipse 900px 600px at 15% 0%,   rgba(16, 185, 129, 0.07) 0%, transparent 70%),
                radial-gradient(ellipse 700px 500px at 85% 100%, rgba(14, 165, 233, 0.05) 0%, transparent 70%),
                radial-gradient(ellipse 500px 400px at 50% 50%,  rgba(99,  102, 241, 0.03) 0%, transparent 70%),
                transparent !important;
            padding-top: 0 !important;
            max-width: 1100px !important;
        }

        /* ══════════════════════════════════════════
           HIDE STREAMLIT CHROME
           ══════════════════════════════════════════ */
        #MainMenu { visibility: hidden; }
        header[data-testid="stHeader"] { display: none !important; }
        footer { display: none !important; }

        /* ══════════════════════════════════════════
           SCROLLBAR
           ══════════════════════════════════════════ */
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: #060B14; }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #10B981, #0EA5E9);
            border-radius: 4px;
        }

        /* ══════════════════════════════════════════
           PROFESSIONAL HEADER
           ══════════════════════════════════════════ */
        .sf-header {
            position: sticky; top: 0; z-index: 999;
            padding: 0 40px;
            height: 64px;
            display: flex; align-items: center; justify-content: space-between;
            background: rgba(6, 11, 20, 0.90);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255,255,255,0.06);
            margin-bottom: 40px;
        }
        .sf-header-left { display: flex; align-items: center; gap: 12px; }
        .sf-header-logo {
            width: 32px; height: 32px; border-radius: 8px;
            background: linear-gradient(135deg, #10B981, #059669);
            display: flex; align-items: center; justify-content: center;
            font-size: 1rem;
            box-shadow: 0 0 16px rgba(16,185,129,0.3);
        }
        .sf-header-brand {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.15rem;
            font-weight: 700;
            color: #F1F5F9;
            letter-spacing: -0.3px;
        }
        .sf-header-divider {
            width: 1px; height: 20px;
            background: rgba(255,255,255,0.1);
        }
        .sf-header-tagline {
            font-size: 0.78rem;
            color: #475569;
            font-weight: 400;
            letter-spacing: 0.2px;
        }
        .sf-header-right { display: flex; align-items: center; gap: 12px; }
        .sf-header-badge {
            display: inline-flex; align-items: center; gap: 6px;
            background: rgba(16,185,129,0.08);
            color: #34D399;
            border: 1px solid rgba(16,185,129,0.2);
            border-radius: 6px;
            padding: 5px 12px;
            font-size: 0.72rem;
            font-weight: 600;
            font-family: 'DM Sans', sans-serif;
            letter-spacing: 0.4px;
            text-transform: uppercase;
        }
        .sf-status-dot {
            width: 6px; height: 6px; border-radius: 50%;
            background: #10B981;
            box-shadow: 0 0 6px #10B981;
            animation: pulse-dot 2s infinite;
        }
        @keyframes pulse-dot {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }

        /* ══════════════════════════════════════════
           PROFESSIONAL FOOTER
           ══════════════════════════════════════════ */
        .sf-footer {
            margin-top: 80px;
            padding: 36px 40px 28px;
            border-top: 1px solid rgba(255,255,255,0.06);
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 20px;
            align-items: center;
        }
        .sf-footer-left {}
        .sf-footer-brand-row {
            display: flex; align-items: center; gap: 8px; margin-bottom: 6px;
        }
        .sf-footer-brand-name {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.95rem; font-weight: 700; color: #E2E8F0;
        }
        .sf-footer-copy {
            font-size: 0.76rem; color: #334155; line-height: 1.6;
        }
        .sf-footer-stack {
            font-size: 0.73rem; color: #1E3A4A; margin-top: 2px;
        }
        .sf-footer-stack span { color: #0E7A5A; font-weight: 500; }
        .sf-footer-right {}
        .sf-footer-links {
            display: flex; gap: 20px; justify-content: flex-end;
        }
        .sf-footer-links a {
            color: #334155; text-decoration: none;
            font-size: 0.78rem; font-weight: 500;
            transition: color 0.2s;
        }
        .sf-footer-links a:hover { color: #34D399; }

        /* ══════════════════════════════════════════
           TYPOGRAPHY
           ══════════════════════════════════════════ */
        h1, h2, h3, h4 {
            font-family: 'Space Grotesk', sans-serif !important;
        }
        h1 {
            font-size: 2.4rem !important;
            font-weight: 800 !important;
            letter-spacing: -1.5px !important;
            line-height: 1.15 !important;
            background: linear-gradient(135deg, #E2E8F0 0%, #94A3B8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        h2 {
            font-size: 1.5rem !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px !important;
            color: #CBD5E1 !important;
        }
        h3 {
            font-size: 1.05rem !important;
            font-weight: 600 !important;
            color: #94A3B8 !important;
        }
        p, li, label { font-family: 'DM Sans', sans-serif !important; }

        /* ══════════════════════════════════════════
           ACCENT / LABEL OVERRIDES (keep green for data)
           ══════════════════════════════════════════ */
        .accent-green { color: #10B981 !important; }
        .accent-blue  { color: #0EA5E9 !important; }

        /* ══════════════════════════════════════════
           BUTTONS
           ══════════════════════════════════════════ */
        div.stButton > button {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.88rem !important;
            letter-spacing: 0.2px !important;
            border: none !important;
            border-radius: 10px !important;
            background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
            color: #fff !important;
            padding: 10px 22px !important;
            box-shadow: 0 2px 12px rgba(16,185,129,0.25), inset 0 1px 0 rgba(255,255,255,0.12) !important;
            transition: all 0.25s ease !important;
        }
        div.stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 24px rgba(16,185,129,0.4) !important;
        }
        div.stButton > button:active {
            transform: translateY(0px) !important;
        }

        /* ══════════════════════════════════════════
           DOWNLOAD BUTTON
           ══════════════════════════════════════════ */
        div[data-testid="stDownloadButton"] > button {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 10px !important;
            border: 1px solid rgba(16,185,129,0.3) !important;
            background: transparent !important;
            color: #34D399 !important;
            transition: all 0.25s ease !important;
        }
        div[data-testid="stDownloadButton"] > button:hover {
            background: rgba(16,185,129,0.08) !important;
            border-color: rgba(16,185,129,0.5) !important;
        }

        /* ══════════════════════════════════════════
           GLASS CARDS
           ══════════════════════════════════════════ */
        .glass-card {
            background: rgba(15, 23, 36, 0.7);
            border: 1px solid rgba(255,255,255,0.06);
            border-radius: 16px;
            padding: 28px 32px;
            margin-bottom: 16px;
            transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
        }
        .glass-card:hover {
            border-color: rgba(16,185,129,0.2);
            box-shadow: 0 12px 40px rgba(0,0,0,0.4), 0 0 0 1px rgba(16,185,129,0.08);
            transform: translateY(-3px);
        }
        .glass-card h3 {
            color: #E2E8F0 !important;
            font-size: 1rem !important;
            font-weight: 600 !important;
            margin-bottom: 8px !important;
        }
        .glass-card p { color: #64748B; font-size: 0.88rem; line-height: 1.65; }

        /* ══════════════════════════════════════════
           FILE UPLOADER
           ══════════════════════════════════════════ */
        div[data-testid="stFileUploader"] {
            border: 1.5px dashed rgba(16,185,129,0.3) !important;
            border-radius: 14px !important;
            padding: 2rem !important;
            background: rgba(16,185,129,0.02) !important;
            transition: all 0.25s ease !important;
        }
        div[data-testid="stFileUploader"]:hover {
            border-color: rgba(16,185,129,0.5) !important;
            background: rgba(16,185,129,0.04) !important;
        }

        /* ══════════════════════════════════════════
           INPUTS & SELECTBOX
           ══════════════════════════════════════════ */
        .stTextInput > div > div > input,
        .stSelectbox > div > div {
            font-family: 'DM Sans', sans-serif !important;
            background: rgba(15,23,36,0.8) !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 10px !important;
            color: #E2E8F0 !important;
            transition: border-color 0.25s, box-shadow 0.25s !important;
        }
        .stTextInput > div > div > input:focus {
            border-color: rgba(16,185,129,0.5) !important;
            box-shadow: 0 0 0 3px rgba(16,185,129,0.1) !important;
        }

        /* ══════════════════════════════════════════
           SIDEBAR
           ══════════════════════════════════════════ */
        section[data-testid="stSidebar"] {
            background: #060B14 !important;
            border-right: 1px solid rgba(255,255,255,0.05) !important;
        }
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            font-family: 'Space Grotesk', sans-serif !important;
            color: #CBD5E1 !important;
        }

        /* ══════════════════════════════════════════
           METRICS
           ══════════════════════════════════════════ */
        [data-testid="stMetric"] {
            background: rgba(15,23,36,0.6) !important;
            border: 1px solid rgba(255,255,255,0.07) !important;
            border-radius: 14px !important;
            padding: 20px !important;
            transition: border-color 0.25s, box-shadow 0.25s !important;
        }
        [data-testid="stMetric"]:hover {
            border-color: rgba(16,185,129,0.2) !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
        }
        [data-testid="stMetricLabel"] {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.75rem !important;
            color: #475569 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.6px !important;
        }
        [data-testid="stMetricValue"] {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            color: #E2E8F0 !important;
            font-size: 1.6rem !important;
        }
        [data-testid="stMetricDelta"] {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.78rem !important;
        }

        /* ══════════════════════════════════════════
           EXPANDERS
           ══════════════════════════════════════════ */
        [data-testid="stExpander"] {
            background: rgba(15,23,36,0.5) !important;
            border: 1px solid rgba(255,255,255,0.06) !important;
            border-radius: 12px !important;
            transition: border-color 0.25s !important;
        }
        [data-testid="stExpander"]:hover {
            border-color: rgba(16,185,129,0.2) !important;
        }
        [data-testid="stExpander"] summary {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 500 !important;
            color: #94A3B8 !important;
        }

        /* ══════════════════════════════════════════
           PROGRESS
           ══════════════════════════════════════════ */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #10B981, #34D399) !important;
            border-radius: 4px !important;
        }
        .stProgress > div > div > div {
            background: rgba(16,185,129,0.08) !important;
            border-radius: 4px !important;
        }

        /* ══════════════════════════════════════════
           DIVIDER
           ══════════════════════════════════════════ */
        hr {
            border: none !important;
            height: 1px !important;
            background: rgba(255,255,255,0.06) !important;
            margin: 28px 0 !important;
        }

        /* ══════════════════════════════════════════
           ALERTS
           ══════════════════════════════════════════ */
        [data-testid="stAlert"] {
            border-radius: 12px !important;
            font-family: 'DM Sans', sans-serif !important;
            border-width: 1px !important;
        }
        div.element-container:has([data-testid="stAlert"]) {
            font-family: 'DM Sans', sans-serif !important;
        }

        /* ══════════════════════════════════════════
           SPINNER
           ══════════════════════════════════════════ */
        .stSpinner > div > div {
            border-top-color: #10B981 !important;
        }

        /* ══════════════════════════════════════════
           BADGE
           ══════════════════════════════════════════ */
        .badge {
            background: rgba(16,185,129,0.1);
            color: #34D399;
            padding: 3px 12px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            border: 1px solid rgba(16,185,129,0.2);
            font-family: 'DM Sans', sans-serif;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }
        </style>
    """, unsafe_allow_html=True)


def render_header():
    st.markdown("""
        <div class="sf-header">
            <div class="sf-header-left">
                <div class="sf-header-logo">🌾</div>
                <div class="sf-header-brand">SmartFarm AI</div>
                <div class="sf-header-divider"></div>
                <div class="sf-header-tagline">Pathological Intelligence for Agriculture</div>
            </div>
            <div class="sf-header-right">
                <div class="sf-header-badge">
                    <div class="sf-status-dot"></div>
                    All Systems Operational
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
        <div class="sf-footer">
            <div class="sf-footer-left">
                <div class="sf-footer-brand-row">
                    <div class="sf-footer-brand-name">🌾 SmartFarm AI</div>
                </div>
                <div class="sf-footer-copy">© 2025–26 Team SmartFarm. Built for sustainable agriculture.</div>
                <div class="sf-footer-stack">Powered by <span>CNN</span> · <span>Gemini Vision</span> · <span>Grok LLM</span> · <span>ChromaDB</span></div>
            </div>
            <div class="sf-footer-right">
                <div class="sf-footer-links">
                    <a href="#">Home</a>
                    <a href="#">Diagnosis</a>
                    <a href="#">Analytics</a>
                    <a href="#">About</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def initialize_ui():
    """Full UI initialization: styles + header."""
    inject_global_styles()
    render_header()
