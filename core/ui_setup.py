import streamlit as st

def initialize_ui():
    """Injects high-end, premium aesthetics into the Streamlit application globally."""
    st.markdown("""
        <style>
        /* Modern Glassmorphism Buttons */
        div.stButton > button {
            border: none;
            border-radius: 12px;
            background: linear-gradient(135deg, #11B27B 0%, #0D8F61 100%);
            color: white;
            font-weight: 600;
            box-shadow: 0 4px 15px rgba(17, 178, 123, 0.3);
            transition: all 0.3s ease;
            width: 100%;
        }
        div.stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(17, 178, 123, 0.5) !important;
            color: #ffffff;
            background: linear-gradient(135deg, #13D190 0%, #0D8F61 100%);
        }
        
        /* Input borders */
        input {
            border-radius: 8px !important;
            border: 1px solid rgba(17, 178, 123, 0.5) !important;
        }
        
        /* Gradient Main Titles */
        h1 {
            background: -webkit-linear-gradient(45deg, #11B27B, #4ADE80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
        }
        
        /* Secondary headers */
        h2 {
            color: #E2E8F0 !important;
            font-weight: 700;
        }
        
        h3 {
            color: #4ADE80 !important;
            font-weight: 600;
        }
        
        /* File Uploader Customization */
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
        
        /* Custom Cards */
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
        
        /* Sidebar styling */
        section[data-testid="stSidebar"] {
            background-color: #12161B;
            border-right: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        /* Status Badges */
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
        
        /* Spinner */
        .stSpinner > div > div {
            border-top-color: #4ADE80 !important;
        }
        </style>
    """, unsafe_allow_html=True)
