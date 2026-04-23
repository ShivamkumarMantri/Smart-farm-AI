import streamlit as st
import json
import plotly.graph_objects as go
import plotly.express as px
from pathlib import Path
from collections import Counter
from core.ui_setup import initialize_ui, render_footer

initialize_ui()

# ─── Sidebar ─────────────────────────────────────────────────
st.sidebar.title("🌿 SmartFarm AI")
st.sidebar.markdown("Advanced Crop Health Diagnosis")
st.sidebar.divider()
st.sidebar.info("History is powered by ChromaDB & Local Vector Memory.")

# ─── Title ───────────────────────────────────────────────────
st.title("📊 Farm Analytics Dashboard")
st.markdown("Track crop health trends, diagnoses over time, and system performance.")

# ─── Load History ────────────────────────────────────────────
MEMORY_FILE = Path("data/memory/embeddings.json")

if not MEMORY_FILE.exists() or not MEMORY_FILE.stat().st_size:
    st.info("📭 No diagnosis history found yet. Run some analyses in the Diagnosis Tool first!")
    render_footer()
    st.stop()

try:
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
except Exception as e:
    st.error(f"Error loading history: {e}")
    render_footer()
    st.stop()

if not history:
    st.info("📭 History is currently empty.")
    render_footer()
    st.stop()

# ─── Pre-process data ─────────────────────────────────────────
entries = list(history.values())
total = len(entries)
diseases = [e.get("diagnosis", "Unknown") for e in entries]
confidences = [e.get("confidence", 0.0) for e in entries]
avg_conf = sum(confidences) / len(confidences) if confidences else 0
disease_counts = Counter(diseases)
most_common = disease_counts.most_common(1)[0] if disease_counts else ("None", 0)

# ─── KPI Metrics ─────────────────────────────────────────────
st.markdown("### 📈 Overview")
m1, m2, m3, m4 = st.columns(4)
m1.metric("🔬 Total Diagnoses", total)
m2.metric("🎯 Avg. AI Confidence", f"{avg_conf:.1%}")
m3.metric("🦠 Unique Diseases", len(disease_counts))
m4.metric("⚠️ Most Common", most_common[0].replace("_", " ")[:18] if most_common[0] != "None" else "N/A")

st.divider()

# ─── Charts ──────────────────────────────────────────────────
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("#### 🥧 Disease Distribution")
    if disease_counts:
        labels = [k.replace("_", " ") for k in disease_counts.keys()]
        values = list(disease_counts.values())
        fig_pie = go.Figure(go.Pie(
            labels=labels,
            values=values,
            hole=0.45,
            marker=dict(
                colors=px.colors.sequential.Greens_r[:len(labels)],
                line=dict(color="#0A0F14", width=2)
            ),
            textfont=dict(color="#E2E8F0"),
        ))
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            legend=dict(font=dict(color="#94A3B8")),
            margin=dict(t=10, b=10, l=10, r=10),
            height=300,
        )
        st.plotly_chart(fig_pie, use_container_width=True)

with chart_col2:
    st.markdown("#### 📊 Top Diseases (Bar)")
    top_n = disease_counts.most_common(6)
    if top_n:
        top_labels = [k.replace("_", " ") for k, _ in top_n]
        top_vals = [v for _, v in top_n]
        fig_bar = go.Figure(go.Bar(
            x=top_vals,
            y=top_labels,
            orientation="h",
            marker=dict(
                color=top_vals,
                colorscale="Greens",
                line=dict(color="rgba(0,0,0,0)")
            ),
            text=top_vals,
            textposition="outside",
            textfont=dict(color="#94A3B8"),
        ))
        fig_bar.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False, color="#475569"),
            yaxis=dict(color="#94A3B8"),
            margin=dict(t=10, b=10, l=10, r=10),
            height=300,
        )
        st.plotly_chart(fig_bar, use_container_width=True)

# ─── Confidence Trend ─────────────────────────────────────────
st.markdown("#### 📉 Confidence Score Trend")
conf_vals = [round(c * 100, 1) for c in confidences]
fig_line = go.Figure(go.Scatter(
    y=conf_vals,
    mode="lines+markers",
    line=dict(color="#11B27B", width=2),
    marker=dict(color="#4ADE80", size=7),
    fill="tozeroy",
    fillcolor="rgba(17,178,123,0.1)",
))
fig_line.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False, color="#475569", title="Diagnosis #"),
    yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)", color="#475569", title="Confidence (%)"),
    margin=dict(t=10, b=10, l=10, r=10),
    height=220,
)
st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# ─── Diagnosis History Log ────────────────────────────────────
st.markdown("### 🗂️ Diagnosis Log")
sorted_history = sorted(history.items(), key=lambda x: x[1].get("timestamp", ""), reverse=True)
for entry_id, data in sorted_history:
    with st.expander(f"📅 {data.get('timestamp', 'Unknown Date')} — {data.get('diagnosis', 'Unknown').replace('_', ' ')}"):
        conf_val = data.get("confidence", 0)
        st.markdown(f"**🎯 Confidence:** `{conf_val:.1%}`")
        st.progress(conf_val)
        st.markdown(data.get("diagnosis_text", "No details available."))
        st.caption(f"Entry ID: `{entry_id}`")

render_footer()
