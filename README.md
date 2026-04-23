# 🌾 SmartFarm AI

> **AI-powered crop disease detection for the next generation of farmers.**  
> Detect. Diagnose. Treat — in under 10 seconds.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)](https://streamlit.io)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?style=flat-square&logo=tensorflow)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

---

## 🚀 What is SmartFarm AI?

SmartFarm AI is an intelligent crop health diagnostic system that combines:
- 🧠 **Custom CNN** for fast, high-accuracy disease detection
- 👁️ **Google Gemini Vision** for deep pathological analysis
- 💬 **Grok LLM** for farmer-friendly treatment advice
- 🌦️ **Real-time Weather Integration** for context-aware spray timing
- 💾 **ChromaDB Vector Memory** for long-term farm tracking

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔬 Disease Detection | 38+ plant diseases, up to 94% CNN accuracy |
| 👁️ AI Vision Analysis | Gemini Vision for complex or low-confidence cases |
| 🌦️ Weather-Aware Advice | Real-time weather via Open-Meteo — no API key needed |
| 📸 Multi-Image Upload | Upload up to 3 photos; majority vote for better accuracy |
| 📊 Farm Analytics Dashboard | Plotly charts: disease trends, confidence history |
| 💾 Long-Term Memory | ChromaDB caching for instant re-diagnosis |
| 📥 Downloadable Reports | Export complete diagnosis as a formatted text report |

---

## 🏗️ Architecture

```
User Upload (1-3 Images)
        │
        ▼
┌──────────────────┐
│   CNN Predictor   │ ← TensorFlow Keras model
│   (core/predict) │    38+ disease classes
└────────┬─────────┘
         │ confidence < 75%?
    Yes  ▼              No
┌────────────────┐  ┌──────────────────┐
│  Gemini Vision │  │ ChromaDB Cache   │
│  (AI Vision)   │  │ (Memory Service) │
└────────┬───────┘  └────────┬─────────┘
         │                   │
         ▼                   ▼
┌────────────────────────────────────┐
│         Grok LLM (Final Output)    │
│  + Weather Context (Open-Meteo)    │
└────────────────────────────────────┘
         │
         ▼
   Farmer-Friendly Report
```

---

## 📁 Project Structure

```
smartfarm-ai/
├── 🏠_Home.py                  # Landing page
├── pages/
│   ├── 1_🩺_Diagnosis_Tool.py  # Main diagnosis interface
│   └── 2_📊_Farm_History.py   # Analytics dashboard
├── core/
│   ├── predict.py              # CNN inference engine
│   ├── feature_extractor.py   # Embedding extractor (ChromaDB)
│   └── ui_setup.py            # Global design system & CSS
├── services/
│   ├── hybrid_predictor.py    # Main AI orchestration pipeline
│   ├── memory_service.py      # ChromaDB caching layer
│   └── weather_service.py     # Open-Meteo weather integration
├── ai_modules/
│   ├── llm_client.py          # Gemini Vision + Grok API clients
│   └── prompt_templates.py    # Centralized LLM prompt library
├── model/
│   ├── smartfarm_cnn_best_model.keras
│   └── class_indices.json
├── data/
│   └── memory/embeddings.json # JSON fallback memory
├── .env.example               # Environment variable template
└── requirements.txt
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/ShivamkumarMantri/Smart-farm-AI.git
cd Smart-farm-AI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API keys
```bash
cp .env.example .env
```
Edit `.env` and add your keys:
```env
GEMINI_API_KEY=your_google_gemini_api_key
GROK_API_KEY=your_groq_api_key
```

> **Note:** Weather data uses Open-Meteo (free, no API key required).

### 4. Run the app
```bash
python -m streamlit run "🏠_Home.py"
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌿 How to Use

1. **Home Page** → Learn about the system and click "Start Diagnosis"
2. **Diagnosis Tool** →
   - Upload 1–3 clear photos of the affected leaf
   - Select your crop type (or use auto-detect)
   - Enter your city for weather-aware advice (optional)
   - Click **Run AI Diagnosis**
3. **Results** → View disease name, confidence gauge, AI analysis, and treatment checklist
4. **Download** → Export your diagnosis report as a `.txt` file
5. **Farm History** → Track all past diagnoses with analytics charts

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit + Custom CSS (Glassmorphism) |
| CNN Model | TensorFlow / Keras |
| Vision AI | Google Gemini 2.5 Flash |
| Language Model | Grok via Groq API (LLaMA 3.3 70B) |
| Vector Database | ChromaDB (persistent) |
| Weather API | Open-Meteo (free, no key) |
| Charts | Plotly |

---

## 📊 Model Performance

- **Dataset:** PlantVillage (38 disease classes)
- **CNN Accuracy:** ~94.2% on validation set
- **Inference Time:** < 1s (CNN), < 10s (Full pipeline with LLM)
- **Memory:** ChromaDB similarity threshold: 0.98 (near-identical images)

---

## 🔮 Roadmap

- [ ] Mobile-responsive camera capture
- [ ] Disease heatmap by geographic region  
- [ ] Email report delivery
- [ ] Crop yield impact estimator
- [ ] Offline CNN-only mode

---

## 👨‍💻 Author

**Team SmartFarm** · Final Year Project 2025–26  
Built with ❤️ for sustainable agriculture

---

## 📄 License

MIT License — feel free to use, modify, and distribute.
