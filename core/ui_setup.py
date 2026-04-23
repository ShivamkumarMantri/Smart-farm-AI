import streamlit as st

def inject_global_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

        /* BG */
        .stApp {
            background: #070B14 !important;
        }
        .main .block-container {
            background:
                radial-gradient(ellipse 700px 400px at 10% -5%,  rgba(16,185,129,0.045) 0%, transparent 70%),
                radial-gradient(ellipse 500px 350px at 90% 90%, rgba(6,182,212,0.03) 0%, transparent 70%),
                transparent !important;
            padding-top: 0 !important;
            max-width: 1140px !important;
        }

        /* Hide Streamlit chrome */
        #MainMenu,footer { visibility: hidden; }
        header[data-testid="stHeader"] { display: none !important; }

        /* Scrollbar */
        ::-webkit-scrollbar { width: 4px; }
        ::-webkit-scrollbar-track { background: #070B14; }
        ::-webkit-scrollbar-thumb { background: linear-gradient(#10B981,#06B6D4); border-radius: 4px; }

        /* ── NAVBAR ─────────────────────────────── */
        .sf-nav {
            position: sticky; top: 0; z-index: 9999;
            display: flex; align-items: center; justify-content: space-between;
            padding: 0 48px; height: 68px;
            background: rgba(7,11,20,0.85);
            backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
            border-bottom: 1px solid rgba(255,255,255,0.06);
            margin-bottom: 0;
        }
        .sf-nav::after {
            content:''; position:absolute; bottom:-1px; left:0; right:0; height:1px;
            background: linear-gradient(90deg, transparent 0%, #10B981 40%, #06B6D4 70%, transparent 100%);
            opacity: 0.5;
        }
        .sf-nav-logo {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1.2rem; font-weight: 800; color: #F1F5F9;
            display: flex; align-items: center; gap: 10px; letter-spacing: -0.3px;
        }
        .sf-nav-logo-icon {
            width: 34px; height: 34px; border-radius: 9px;
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            display: flex; align-items: center; justify-content: center;
            font-size: 1rem;
            box-shadow: 0 0 14px rgba(16,185,129,0.4);
        }
        .sf-nav-links { display: flex; gap: 32px; }
        .sf-nav-links a {
            color: #64748B; text-decoration: none;
            font-size: 0.85rem; font-weight: 500; letter-spacing: 0.1px;
            transition: color 0.2s;
        }
        .sf-nav-links a:hover { color: #E2E8F0; }
        .sf-nav-cta {
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            color: #fff !important; border: none; border-radius: 9px;
            padding: 9px 22px; font-size: 0.84rem; font-weight: 600;
            cursor: pointer; text-decoration: none;
            box-shadow: 0 2px 14px rgba(16,185,129,0.35);
            transition: box-shadow 0.25s, transform 0.25s;
        }
        .sf-nav-cta:hover { box-shadow: 0 4px 24px rgba(16,185,129,0.55); transform: translateY(-1px); }

        /* ── HERO ────────────────────────────────── */
        .sf-hero { padding: 80px 0 60px; }
        .sf-hero-tag {
            display: inline-flex; align-items: center; gap: 8px;
            background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.2);
            color: #34D399; border-radius: 100px; padding: 5px 14px;
            font-size: 0.75rem; font-weight: 600; letter-spacing: 0.5px;
            text-transform: uppercase; margin-bottom: 24px;
        }
        .sf-hero-tag-dot {
            width: 6px; height: 6px; border-radius: 50%; background: #10B981;
            box-shadow: 0 0 6px #10B981;
            animation: blink 2s infinite;
        }
        @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.3} }
        .sf-hero-heading {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 3.4rem; font-weight: 800; line-height: 1.1;
            letter-spacing: -2px; margin: 0 0 20px;
        }
        .sf-hero-heading .grad {
            background: linear-gradient(135deg, #10B981 0%, #34D399 40%, #06B6D4 80%, #818CF8 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
        }
        .sf-hero-heading .white { color: #F1F5F9; }
        .sf-hero-sub {
            font-size: 1.08rem; color: #64748B; line-height: 1.7;
            max-width: 520px; margin-bottom: 36px; font-weight: 400;
        }
        .sf-btn-primary {
            display: inline-flex; align-items: center; gap: 8px;
            background: linear-gradient(135deg, #10B981, #059669);
            color: #fff; border: none; border-radius: 12px;
            padding: 13px 28px; font-size: 0.92rem; font-weight: 600;
            cursor: pointer; text-decoration: none;
            box-shadow: 0 4px 20px rgba(16,185,129,0.35);
            transition: all 0.25s; font-family: 'Inter', sans-serif;
        }
        .sf-btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(16,185,129,0.5); }
        .sf-btn-secondary {
            display: inline-flex; align-items: center; gap: 8px;
            background: transparent; color: #94A3B8;
            border: 1px solid rgba(255,255,255,0.1); border-radius: 12px;
            padding: 13px 28px; font-size: 0.92rem; font-weight: 500;
            cursor: pointer; text-decoration: none;
            transition: all 0.25s; font-family: 'Inter', sans-serif;
        }
        .sf-btn-secondary:hover { border-color: rgba(255,255,255,0.2); color: #E2E8F0; background: rgba(255,255,255,0.03); }
        .sf-hero-btns { display: flex; gap: 14px; flex-wrap: wrap; }

        /* ── SECTION LABEL ───────────────────────── */
        .sf-section-label {
            font-size: 0.72rem; font-weight: 700; letter-spacing: 1.5px;
            text-transform: uppercase; color: #10B981; margin-bottom: 10px;
        }
        .sf-section-heading {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 2rem; font-weight: 800; color: #E2E8F0;
            letter-spacing: -0.8px; margin-bottom: 8px;
        }
        .sf-section-sub { font-size: 0.92rem; color: #475569; line-height: 1.65; margin-bottom: 36px; }

        /* ── GLASS CARDS ─────────────────────────── */
        .sf-card {
            background: rgba(255,255,255,0.025);
            backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 20px; padding: 28px;
            transition: transform 0.3s, border-color 0.3s, box-shadow 0.3s;
            position: relative; overflow: hidden;
        }
        .sf-card::before {
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(16,185,129,0.4), transparent);
            opacity: 0; transition: opacity 0.3s;
        }
        .sf-card:hover { transform: translateY(-5px); border-color: rgba(16,185,129,0.2); box-shadow: 0 16px 40px rgba(0,0,0,0.4), 0 0 40px rgba(16,185,129,0.06); }
        .sf-card:hover::before { opacity: 1; }
        .sf-card-icon {
            width: 44px; height: 44px; border-radius: 12px; margin-bottom: 16px;
            display: flex; align-items: center; justify-content: center; font-size: 1.3rem;
        }
        .sf-card-icon.green { background: rgba(16,185,129,0.12); }
        .sf-card-icon.teal  { background: rgba(6,182,212,0.12); }
        .sf-card-icon.violet{ background: rgba(139,92,246,0.12); }
        .sf-card-icon.amber { background: rgba(245,158,11,0.12); }
        .sf-card-title {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1rem; font-weight: 700; color: #E2E8F0; margin-bottom: 8px;
        }
        .sf-card-body { font-size: 0.84rem; color: #475569; line-height: 1.65; }

        /* ── HOW IT WORKS ────────────────────────── */
        .sf-step {
            display: flex; gap: 20px; align-items: flex-start; padding: 24px;
            background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05);
            border-radius: 16px; margin-bottom: 14px;
            transition: border-color 0.3s, transform 0.3s;
        }
        .sf-step:hover { border-color: rgba(16,185,129,0.2); transform: translateX(4px); }
        .sf-step-num {
            min-width: 42px; height: 42px; border-radius: 12px;
            background: linear-gradient(135deg, #10B981, #059669);
            color: #fff; font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1rem; font-weight: 800;
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 4px 14px rgba(16,185,129,0.3);
        }
        .sf-step-title { font-family: 'Plus Jakarta Sans', sans-serif; font-size: 0.95rem; font-weight: 700; color: #E2E8F0; margin-bottom: 4px; }
        .sf-step-body  { font-size: 0.82rem; color: #475569; line-height: 1.55; }

        /* ── STAT CARDS ──────────────────────────── */
        .sf-stat {
            text-align: center; padding: 28px 20px;
            background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.06);
            border-radius: 20px; transition: border-color 0.3s, box-shadow 0.3s;
        }
        .sf-stat:hover { border-color: rgba(16,185,129,0.2); box-shadow: 0 0 30px rgba(16,185,129,0.05); }
        .sf-stat-num {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 2.4rem; font-weight: 800; letter-spacing: -1px;
            background: linear-gradient(135deg, #10B981, #06B6D4);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;
        }
        .sf-stat-label { font-size: 0.8rem; color: #475569; margin-top: 4px; font-weight: 500; }

        /* ── RESULT CARD ─────────────────────────── */
        .sf-result {
            background: rgba(255,255,255,0.025); border: 1px solid rgba(16,185,129,0.2);
            border-radius: 20px; padding: 28px;
            box-shadow: 0 0 40px rgba(16,185,129,0.06);
        }
        .sf-result-badge {
            display: inline-flex; align-items: center; gap: 6px;
            background: rgba(16,185,129,0.1); border: 1px solid rgba(16,185,129,0.2);
            color: #34D399; border-radius: 8px;
            padding: 5px 12px; font-size: 0.73rem; font-weight: 600; letter-spacing: 0.5px; text-transform: uppercase;
        }
        .sf-disease-name {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1.5rem; font-weight: 800; color: #F1F5F9; letter-spacing: -0.5px; margin: 12px 0 4px;
        }
        .sf-confidence {
            font-size: 0.85rem; color: #64748B; margin-bottom: 20px;
        }
        .sf-confidence span { color: #34D399; font-weight: 700; }

        /* ── TOAST ───────────────────────────────── */
        .sf-toast {
            position: fixed; bottom: 28px; right: 28px;
            background: rgba(16,185,129,0.12); border: 1px solid rgba(16,185,129,0.3);
            backdrop-filter: blur(16px); border-radius: 14px;
            padding: 14px 20px; color: #34D399;
            font-size: 0.85rem; font-weight: 500; z-index: 9999;
            box-shadow: 0 8px 30px rgba(0,0,0,0.4);
            animation: slideUp 0.4s ease;
        }
        @keyframes slideUp { from{opacity:0;transform:translateY(20px)} to{opacity:1;transform:translateY(0)} }

        /* ── FOOTER ──────────────────────────────── */
        .sf-footer {
            margin-top: 80px; padding: 48px 0 32px;
            border-top: 1px solid rgba(255,255,255,0.06);
        }
        .sf-footer-grid {
            display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 40px; margin-bottom: 40px;
        }
        .sf-footer-brand {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 1.1rem; font-weight: 800; color: #E2E8F0; margin-bottom: 12px;
        }
        .sf-footer-desc { font-size: 0.82rem; color: #334155; line-height: 1.7; max-width: 240px; }
        .sf-footer-col-title { font-size: 0.72rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase; color: #475569; margin-bottom: 14px; }
        .sf-footer-link { display: block; color: #334155; text-decoration: none; font-size: 0.82rem; margin-bottom: 8px; transition: color 0.2s; }
        .sf-footer-link:hover { color: #34D399; }
        .sf-footer-bottom {
            display: flex; justify-content: space-between; align-items: center;
            padding-top: 24px; border-top: 1px solid rgba(255,255,255,0.04);
            font-size: 0.76rem; color: #1E293B;
        }
        .sf-footer-socials { display: flex; gap: 14px; }
        .sf-footer-socials a {
            color: #334155; text-decoration: none; font-size: 0.8rem;
            transition: color 0.2s;
        }
        .sf-footer-socials a:hover { color: #34D399; }

        /* ── GLOBAL OVERRIDES ─────────────────────── */
        h1,h2,h3,h4,h5 { font-family:'Plus Jakarta Sans',sans-serif !important; }
        h1 {
            font-size:2.2rem!important; font-weight:800!important; letter-spacing:-1px!important;
            background:linear-gradient(135deg,#E2E8F0,#94A3B8);
            -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
        }
        h2 { color:#CBD5E1!important; font-weight:700!important; letter-spacing:-0.5px!important; }
        h3 { color:#94A3B8!important; font-weight:600!important; }
        p,li { font-family:'Inter',sans-serif!important; }

        div.stButton>button {
            font-family:'Inter',sans-serif!important; font-weight:600!important;
            border:none!important; border-radius:11px!important;
            background:linear-gradient(135deg,#10B981 0%,#059669 100%)!important;
            color:#fff!important; box-shadow:0 2px 14px rgba(16,185,129,0.3)!important;
            transition:all 0.25s!important;
        }
        div.stButton>button:hover { transform:translateY(-2px)!important; box-shadow:0 6px 24px rgba(16,185,129,0.45)!important; }

        div[data-testid="stDownloadButton"]>button {
            font-family:'Inter',sans-serif!important; font-weight:600!important;
            border-radius:11px!important; border:1px solid rgba(16,185,129,0.3)!important;
            background:transparent!important; color:#34D399!important; transition:all 0.25s!important;
        }
        div[data-testid="stDownloadButton"]>button:hover { background:rgba(16,185,129,0.08)!important; }

        div[data-testid="stFileUploader"] {
            border:1.5px dashed rgba(16,185,129,0.3)!important; border-radius:16px!important;
            background:rgba(16,185,129,0.02)!important; transition:all 0.25s!important;
        }
        div[data-testid="stFileUploader"]:hover { border-color:rgba(16,185,129,0.5)!important; background:rgba(16,185,129,0.04)!important; }

        section[data-testid="stSidebar"] { background:#06080F!important; border-right:1px solid rgba(255,255,255,0.05)!important; }

        .stTextInput>div>div>input, .stSelectbox>div>div {
            font-family:'Inter',sans-serif!important;
            background:rgba(15,23,36,0.8)!important;
            border:1px solid rgba(255,255,255,0.08)!important;
            border-radius:10px!important; color:#E2E8F0!important;
        }

        [data-testid="stMetric"] {
            background:rgba(255,255,255,0.025)!important;
            border:1px solid rgba(255,255,255,0.07)!important;
            border-radius:16px!important; padding:20px!important;
            transition:border-color 0.3s,box-shadow 0.3s!important;
        }
        [data-testid="stMetric"]:hover { border-color:rgba(16,185,129,0.2)!important; box-shadow:0 4px 20px rgba(0,0,0,0.3)!important; }
        [data-testid="stMetricLabel"] { font-family:'Inter',sans-serif!important; font-size:0.72rem!important; color:#475569!important; text-transform:uppercase!important; letter-spacing:0.7px!important; }
        [data-testid="stMetricValue"] { font-family:'Plus Jakarta Sans',sans-serif!important; font-weight:800!important; color:#E2E8F0!important; font-size:1.6rem!important; }

        [data-testid="stExpander"] { background:rgba(255,255,255,0.02)!important; border:1px solid rgba(255,255,255,0.06)!important; border-radius:14px!important; }
        [data-testid="stExpander"]:hover { border-color:rgba(16,185,129,0.15)!important; }

        .stProgress>div>div>div>div { background:linear-gradient(90deg,#10B981,#06B6D4)!important; border-radius:4px!important; }
        .stProgress>div>div>div { background:rgba(16,185,129,0.08)!important; border-radius:4px!important; }

        hr { border:none!important; height:1px!important; background:rgba(255,255,255,0.06)!important; margin:28px 0!important; }
        [data-testid="stAlert"] { border-radius:12px!important; }
        .stSpinner>div>div { border-top-color:#10B981!important; }
        .glass-card { background:rgba(255,255,255,0.025); backdrop-filter:blur(12px); border:1px solid rgba(255,255,255,0.07); border-radius:20px; padding:28px; transition:transform 0.3s,border-color 0.3s; }
        .glass-card:hover { transform:translateY(-5px); border-color:rgba(16,185,129,0.2); }
        .glass-card h3 { color:#E2E8F0!important; font-size:1rem!important; }
        .glass-card p { color:#475569; font-size:0.85rem; line-height:1.65; }
        </style>
    """, unsafe_allow_html=True)


def render_navbar():
    st.markdown("""
        <nav class="sf-nav">
            <div class="sf-nav-logo">
                <div class="sf-nav-logo-icon">🌾</div>
                SmartFarm AI
            </div>
            <div class="sf-nav-links">
                <a href="#">Home</a>
                <a href="#">Diagnosis</a>
                <a href="#">History</a>
                <a href="#">Insights</a>
            </div>
            <a class="sf-nav-cta" href="#">⚡ Start Diagnosis</a>
        </nav>
    """, unsafe_allow_html=True)


def render_footer():
    st.markdown("""
        <div class="sf-footer">
            <div class="sf-footer-grid">
                <div>
                    <div class="sf-footer-brand">🌾 SmartFarm AI</div>
                    <div class="sf-footer-desc">AI-powered crop disease detection for the next generation of farmers. Built with deep learning, designed for impact.</div>
                </div>
                <div>
                    <div class="sf-footer-col-title">Product</div>
                    <a class="sf-footer-link" href="#">Diagnosis Tool</a>
                    <a class="sf-footer-link" href="#">Farm Analytics</a>
                    <a class="sf-footer-link" href="#">AI Features</a>
                    <a class="sf-footer-link" href="#">Roadmap</a>
                </div>
                <div>
                    <div class="sf-footer-col-title">Resources</div>
                    <a class="sf-footer-link" href="#">Documentation</a>
                    <a class="sf-footer-link" href="#">API Reference</a>
                    <a class="sf-footer-link" href="#">Blog</a>
                    <a class="sf-footer-link" href="#">Support</a>
                </div>
                <div>
                    <div class="sf-footer-col-title">Company</div>
                    <a class="sf-footer-link" href="#">About</a>
                    <a class="sf-footer-link" href="#">Team</a>
                    <a class="sf-footer-link" href="#">Contact</a>
                    <a class="sf-footer-link" href="#">Privacy</a>
                </div>
            </div>
            <div class="sf-footer-bottom">
                <div>© 2025–26 SmartFarm AI. Empowering sustainable agriculture with AI.</div>
                <div class="sf-footer-socials">
                    <a href="#">GitHub</a>
                    <a href="#">Twitter</a>
                    <a href="#">LinkedIn</a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)


def initialize_ui():
    inject_global_styles()
    render_navbar()
