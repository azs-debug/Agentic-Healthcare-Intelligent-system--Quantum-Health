# 🏥 Geospatial Truth Healthcare System (Agentic AI Dashboard)

An AI-powered healthcare recommendation and geospatial intelligence system that suggests the most suitable hospitals based on medical need, trust score, crisis conditions, and location awareness.

The system combines **data engineering, geospatial visualization, explainable AI (Glass Box UI), and an agent-based decision layer (in development)** to assist patients and administrators in healthcare decision-making.

---

## 🚀 Project Overview

This project helps users find the most suitable hospital using:
- Natural language medical queries
- Hospital trust scoring system
- Crisis-based regional analysis
- Real-time geospatial visualization
- Explainable AI decision tracing

It also provides an **admin dashboard** for identifying “Medical Desert” regions where healthcare resources are insufficient.

---

## 🧠 Key Features

### 👤 Patient View
- Enter natural language medical needs (e.g., “ICU with ventilator required”)
- Auto-detects user location
- Filters hospitals based on relevance
- Ranks hospitals using trust score + crisis score
- Shows interactive geospatial hospital map
- Provides routing to best hospital (OSRM-based)
- Displays AI explanation (Glass Box UI)

---

### 🗺️ Geospatial Truth Map
- Built using PyDeck
- Color-coded hospital markers:
  - 🟢 Green → High trust / verified hospital
  - 🟡 Yellow → Moderate reliability
  - 🔴 Red → Medical desert / high risk
- Interactive tooltips for hospital insights
- Ranking-aware visualization (Best hospital highlighted)

---

### 📊 Admin Dashboard
- PIN code level crisis analysis
- Medical Desert heatmap visualization
- Crisis Ratio calculation: Crisis Score = Population Density / Facility Capability
- Identification of high-risk healthcare regions

---

### 🪟 Glass Box (Explainability Layer)
Each hospital displays:
- Reason for recommendation
- Trust score interpretation
- Crisis score explanation
- Evidence-based verification notes
- Transparency of AI decision-making process

---

## 🏗️ System Architecture
User Query (Natural Language)
↓
Agent Layer (Rule-based / Future LLM Integration)
↓
Hospital Filtering & Ranking Engine
↓
Trust Score + Crisis Score Computation
↓
Streamlit Visualization Layer
↓
Outputs:
├── Geospatial Map (PyDeck)
├── Routing System (OSRM)
├── Glass Box Explanation UI
└── Admin Analytics Dashboard

---

## 📁 Project Structure
Dashboard for quantum health/
│
├── app/
│ ├── main.py
│ ├── components/
│ │ ├── map_view.py
│ │ ├── routing.py
│ │ ├── admin_view.py
│ │ ├── glassbox.py
│ │
│ ├── utils/
│ │ ├── data_loader.py
│ │ ├── location.py
│ │ ├── agent_runner.py
│ │ ├── agent_adapter.py
│ │ ├── pincode_analytics.py
│
├── data/
│ ├── engineered_data.csv
│
├── .venv/
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone <repo-url>
cd "Dashboard for quantum health"
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
streamlit run app/main.py
```
📦 Requirements
streamlit
pandas
pydeck
requests


🌍 Routing System

Uses OSRM (Open Source Routing Machine):

http://router.project-osrm.org

Features:

Shortest path routing
Real-time hospital navigation visualization
Safe fallback handling for missing routes
📊 Data Features
Hospital name
Latitude & longitude
Specialties
Trust score (0–1)
Crisis ratio
Equipment availability
Verified medical capabilities
PIN code / region mapping
🧠 Future Improvements
Full LLM-powered medical agent (GPT / Gemini integration)
Real-time hospital availability tracking
Ambulance ETA prediction system
Semantic search over medical conditions
Live traffic-aware routing
Hospital capacity forecasting
⚠️ Current Limitations
Agent layer is rule-based (not fully LLM integrated yet)
Dataset is static (no live hospital API integration)
Routing depends on external OSRM service
Some inference logic is simulated
🎯 Project Goal

To build a transparent, explainable, and intelligent healthcare decision system that bridges the gap between:

Medical Need → Hospital Capability → Geographic Accessibility

👨‍💻 Team

Developed as a 3-member project focusing on:

Agentic AI system design
Geospatial analytics
Healthcare intelligence dashboard
⭐ License

Academic / Hackathon Project — for educational use only.


--- 

If you want next upgrade, I can also generate:
- :contentReference[oaicite:0]{index=0}  
- :contentReference[oaicite:1]{index=1}  
- :contentReference[oaicite:2]{index=2}
