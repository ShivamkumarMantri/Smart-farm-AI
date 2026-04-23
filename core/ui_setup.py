import streamlit as st

def inject_global_styles():
    """Injects a world-class, unique design system with custom fonts and animations."""
    st.markdown("""
        <style>
        /* ══════════════════════════════════════════════════
           FONTS: Space Grotesk (headings) + DM Sans (body)
           ══════════════════════════════════════════════════ */
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap');

        html, body, [class*="css"] {
            font-family: 'DM Sans', sans-serif !important;
            background-color: #040810 !important;
            color: #CBD5E1 !important;
        }

        /* ══════════════════════════════════════════════════
           ANIMATED BACKGROUND MESH
           ══════════════════════════════════════════════════ */
        .main .block-container {
            background: 
                radial-gradient(ellipse 80% 50% at 20% 10%, rgba(17,178,123,0.06) 0%, transparent 60%),
                radial-gradient(ellipse 60% 40% at 80% 80%, rgba(56,189,248,0.04) 0%, transparent 60%),
                #040810 !important;
            padding-top: 0 !important;
        }

        /* ══════════════════════════════════════════════════
           HIDE DEFAULT STREAMLIT CHROME
           ══════════════════════════════════════════════════ */
        #MainMenu { visibility: hidden; }
        header[data-testid="stHeader"] { display: none !important; }
        footer { display: none !important; }

        /* ══════════════════════════════════════════════════
           CUSTOM SCROLLBAR
           ══════════════════════════════════════════════════ */
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: #040810; }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #11B27B, #0891B2);
            border-radius: 10px;
        }

        /* ══════════════════════════════════════════════════
           GLOBAL HEADER
           ══════════════════════════════════════════════════ */
        .sf-header {
            position: sticky;
            top: 0;
            z-index: 999;
            width: 100%;
            padding: 14px 36px;
            background: rgba(4, 8, 16, 0.92);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border-bottom: 1px solid rgba(17, 178, 123, 0.2);
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 32px;
        }
        .sf-header::after {
            content: '';
            position: absolute;
            bottom: -1px;
            left: 0; right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #11B27B, #38BDF8, transparent);
            opacity: 0.6;
        }
        .sf-header-brand {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 1.45rem;
            font-weight: 800;
            background: linear-gradient(110deg, #11B27B 0%, #4ADE80 40%, #38BDF8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
        }
        .sf-header-tagline {
            font-size: 0.75rem;
            color: #475569;
            font-weight: 400;
            letter-spacing: 0.5px;
            margin-top: 2px;
        }
        .sf-header-badge {
            background: linear-gradient(135deg, rgba(17,178,123,0.15), rgba(56,189,248,0.1));
            color: #4ADE80;
            border: 1px solid rgba(17,178,123,0.35);
            border-radius: 100px;
            padding: 5px 16px;
            font-size: 0.75rem;
            font-weight: 600;
            font-family: 'DM Sans', sans-serif;
            letter-spacing: 0.3px;
            box-shadow: 0 0 12px rgba(17,178,123,0.15);
        }

        /* ══════════════════════════════════════════════════
           GLOBAL FOOTER
           ══════════════════════════════════════════════════ */
        .sf-footer {
            margin-top: 72px;
            padding: 32px 40px;
            background: rgba(4, 8, 16, 0.8);
            backdrop-filter: blur(20px);
            border-top: 1px solid transparent;
            background-clip: padding-box;
            position: relative;
            text-align: center;
        }
        .sf-footer::before {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, #11B27B 30%, #38BDF8 70%, transparent);
        }
        .sf-footer-brand {
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 800;
            font-size: 1.1rem;
            background: linear-gradient(110deg, #11B27B, #38BDF8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        .sf-footer p { margin: 4px 0; font-size: 0.8rem; color: #334155; }
        .sf-footer .sf-tech { color: #11B27B; font-weight: 600; }
        .sf-footer-links {
            margin-top: 12px;
            display: flex;
            justify-content: center;
            gap: 28px;
        }
        .sf-footer-links a {
            color: #475569;
            text-decoration: none;
            font-size: 0.78rem;
            font-weight: 500;
            transition: color 0.25s, text-shadow 0.25s;
        }
        .sf-footer-links a:hover {
            color: #4ADE80;
            text-shadow: 0 0 8px rgba(74,222,128,0.4);
        }

        /* ══════════════════════════════════════════════════
           TYPOGRAPHY
           ══════════════════════════════════════════════════ */
        h1, h2, h3, h4, h5 {
            font-family: 'Space Grotesk', sans-serif !important;
        }
        h1 {
            background: linear-gradient(110deg, #11B27B 0%, #4ADE80 50%, #38BDF8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            font-weight: 800 !important;
            letter-spacing: -1px !important;
        }
        h2 {
            color: #E2E8F0 !important;
            font-weight: 700 !important;
            letter-spacing: -0.5px !important;
        }
        h3 {
            color: #4ADE80 !important;
            font-weight: 600 !important;
        }
        p { line-height: 1.7; }

        /* ══════════════════════════════════════════════════
           PREMIUM BUTTONS
           ══════════════════════════════════════════════════ */
        div.stButton > button {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            letter-spacing: 0.3px;
            border: none !important;
            border-radius: 14px !important;
            background: linear-gradient(135deg, #11B27B 0%, #0D8F61 100%) !important;
            color: white !important;
            box-shadow: 0 4px 20px rgba(17, 178, 123, 0.35), inset 0 1px 0 rgba(255,255,255,0.15) !important;
            transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) !important;
            position: relative;
            overflow: hidden;
        }
        div.stButton > button::before {
            content: '';
            position: absolute;
            top: 0; left: -100%;
            width: 100%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            transition: left 0.5s ease;
        }
        div.stButton > button:hover {
            transform: translateY(-3px) scale(1.01) !important;
            box-shadow: 0 8px 30px rgba(17, 178, 123, 0.5), 0 0 20px rgba(17,178,123,0.3) !important;
        }
        div.stButton > button:hover::before { left: 100%; }

        /* ══════════════════════════════════════════════════
           GLASS CARDS (Enhanced with Glow)
           ══════════════════════════════════════════════════ */
        .glass-card {
            background: linear-gradient(135deg, rgba(17,25,35,0.8) 0%, rgba(10,15,20,0.9) 100%);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(17, 178, 123, 0.12);
            border-radius: 20px;
            padding: 28px;
            margin-bottom: 20px;
            transition: transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1),
                        box-shadow 0.35s ease,
                        border-color 0.35s ease;
            position: relative;
            overflow: hidden;
        }
        .glass-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 2px;
            background: linear-gradient(90deg, transparent, #11B27B, transparent);
            opacity: 0;
            transition: opacity 0.35s ease;
        }
        .glass-card:hover {
            transform: translateY(-6px) scale(1.01);
            box-shadow: 0 20px 40px rgba(0,0,0,0.5), 0 0 30px rgba(17,178,123,0.1);
            border-color: rgba(17, 178, 123, 0.3);
        }
        .glass-card:hover::before { opacity: 1; }

        /* ══════════════════════════════════════════════════
           FILE UPLOADER
           ══════════════════════════════════════════════════ */
        div[data-testid="stFileUploader"] {
            border: 2px dashed rgba(17,178,123,0.4) !important;
            border-radius: 18px !important;
            padding: 2rem !important;
            background: radial-gradient(ellipse at center, rgba(17,178,123,0.04) 0%, transparent 70%) !important;
            transition: all 0.3s ease !important;
        }
        div[data-testid="stFileUploader"]:hover {
            border-color: rgba(74,222,128,0.7) !important;
            background: radial-gradient(ellipse at center, rgba(17,178,123,0.08) 0%, transparent 70%) !important;
            box-shadow: 0 0 30px rgba(17,178,123,0.1) !important;
        }

        /* ══════════════════════════════════════════════════
           INPUTS & SELECTS
           ══════════════════════════════════════════════════ */
        .stTextInput > div > div > input,
        .stSelectbox > div > div {
            font-family: 'DM Sans', sans-serif !important;
            background: rgba(17,25,35,0.7) !important;
            border: 1px solid rgba(17,178,123,0.3) !important;
            border-radius: 12px !important;
            color: #E2E8F0 !important;
            transition: border-color 0.3s ease, box-shadow 0.3s ease !important;
        }
        .stTextInput > div > div > input:focus,
        .stSelectbox > div > div:focus-within {
            border-color: rgba(74,222,128,0.6) !important;
            box-shadow: 0 0 0 3px rgba(17,178,123,0.12) !important;
        }

        /* ══════════════════════════════════════════════════
           SIDEBAR
           ══════════════════════════════════════════════════ */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #040810 0%, #060D18 100%) !important;
            border-right: 1px solid rgba(17, 178, 123, 0.1) !important;
        }
        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            font-family: 'Space Grotesk', sans-serif !important;
        }

        /* ══════════════════════════════════════════════════
           METRICS
           ══════════════════════════════════════════════════ */
        [data-testid="stMetric"] {
            background: linear-gradient(135deg, rgba(17,25,35,0.9), rgba(10,15,20,0.95)) !important;
            border: 1px solid rgba(17,178,123,0.15) !important;
            border-radius: 16px !important;
            padding: 18px !important;
            transition: border-color 0.3s, box-shadow 0.3s !important;
        }
        [data-testid="stMetric"]:hover {
            border-color: rgba(17,178,123,0.35) !important;
            box-shadow: 0 0 20px rgba(17,178,123,0.1) !important;
        }
        [data-testid="stMetricLabel"] {
            font-family: 'DM Sans', sans-serif !important;
            font-size: 0.8rem !important;
            color: #64748B !important;
            letter-spacing: 0.5px !important;
        }
        [data-testid="stMetricValue"] {
            font-family: 'Space Grotesk', sans-serif !important;
            font-weight: 700 !important;
            color: #4ADE80 !important;
        }

        /* ══════════════════════════════════════════════════
           EXPANDERS
           ══════════════════════════════════════════════════ */
        [data-testid="stExpander"] {
            background: rgba(17,25,35,0.5) !important;
            border: 1px solid rgba(17,178,123,0.1) !important;
            border-radius: 14px !important;
            transition: border-color 0.3s !important;
        }
        [data-testid="stExpander"]:hover {
            border-color: rgba(17,178,123,0.3) !important;
        }

        /* ══════════════════════════════════════════════════
           SPINNER
           ══════════════════════════════════════════════════ */
        .stSpinner > div > div {
            border-top-color: #4ADE80 !important;
        }

        /* ══════════════════════════════════════════════════
           BADGE
           ══════════════════════════════════════════════════ */
        .badge {
            background: rgba(17, 178, 123, 0.15);
            color: #4ADE80;
            padding: 4px 14px;
            border-radius: 100px;
            font-size: 0.8rem;
            font-weight: 600;
            border: 1px solid rgba(17, 178, 123, 0.3);
            display: inline-block;
            font-family: 'DM Sans', sans-serif;
        }

        /* ══════════════════════════════════════════════════
           PROGRESS BAR
           ══════════════════════════════════════════════════ */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #11B27B, #4ADE80) !important;
            border-radius: 100px !important;
        }
        .stProgress > div > div > div {
            border-radius: 100px !important;
            background: rgba(17,178,123,0.1) !important;
        }

        /* ══════════════════════════════════════════════════
           DIVIDER
           ══════════════════════════════════════════════════ */
        hr {
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg, transparent, rgba(17,178,123,0.3), transparent) !important;
            margin: 24px 0 !important;
        }

        /* ══════════════════════════════════════════════════
           SUCCESS / INFO / WARNING ALERTS
           ══════════════════════════════════════════════════ */
        [data-testid="stAlert"] {
            border-radius: 14px !important;
            font-family: 'DM Sans', sans-serif !important;
        }

        /* ══════════════════════════════════════════════════
           DOWNLOAD BUTTON
           ══════════════════════════════════════════════════ */
        div[data-testid="stDownloadButton"] > button {
            font-family: 'DM Sans', sans-serif !important;
            font-weight: 600 !important;
            border-radius: 14px !important;
            border: 1px solid rgba(17,178,123,0.4) !important;
            background: rgba(17,178,123,0.1) !important;
            color: #4ADE80 !important;
            transition: all 0.3s ease !important;
        }
        div[data-testid="stDownloadButton"] > button:hover {
            background: rgba(17,178,123,0.2) !important;
            border-color: #4ADE80 !important;
            box-shadow: 0 0 15px rgba(17,178,123,0.25) !important;
        }
        </style>
    """, unsafe_allow_html=True)


def render_header():
    st.markdown("""
        <div class="sf-header">
            <div>
                <div class="sf-header-brand">🌾 SmartFarm AI</div>
                <div class="sf-header-tagline">Advanced Pathological Intelligence · Sustainable Agriculture</div>
            </div>
            <div class="sf-header-badge">🟢&nbsp; System Operational</div>
        </div>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
        <div class="sf-footer">
            <div class="sf-footer-brand">🌾 SmartFarm AI</div>
            <p style="margin-top:6px;">2025–26 &nbsp;·&nbsp; Developed by <span class="sf-tech">Team SmartFarm</span></p>
            <p>Powered by <span class="sf-tech">CNN</span> · <span class="sf-tech">Gemini Vision</span> · <span class="sf-tech">Grok LLM</span> · <span class="sf-tech">ChromaDB</span></p>
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
