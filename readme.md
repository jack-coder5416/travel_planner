# 🌍 AI Travel Planner using CrewAI

An intelligent multi-agent AI travel planning system built using **CrewAI**, **Streamlit**, and **OpenRouter LLMs** that generates complete personalized travel itineraries with destination research, local recommendations, and optimized travel planning.

---

# ✨ Features

✅ Multi-Agent AI Architecture  
✅ Intelligent Travel Planning  
✅ Real-Time Agent Workflow Visualization  
✅ Beautiful Modern Streamlit UI  
✅ OpenRouter LLM Integration  
✅ Hidden Gems & Local Recommendations  
✅ Dynamic Itinerary Generation  
✅ Downloadable Travel Plans  
---

# 🖼️ User Interface Preview

## 🌌 Main Dashboard

Replace with screenshot:

```md
![Dashboard](images/dashboard.png)
```

---

## 🤖 Agent Workflow Section

```md
![Agents](images/agents.png)
```

---

## 🌍 Generated Travel Plan

```md
![Result](images/result.png)
```

---

# 🧠 Multi-Agent Architecture

The application uses a **CrewAI sequential multi-agent workflow**.

```text
User Input
    │
    ▼
🏙️ City Selection Agent
    │
    ▼
🧠 Local Expert Agent
    │
    ▼
💼 Travel Concierge Agent
    │
    ▼
📄 Final Travel Plan
```

---

# 🤖 Agents Overview

## 🏙️ City Selection Agent

Responsible for:
- Destination research
- Weather analysis
- Safety checks
- Seasonal recommendations
- Budget optimization

---

## 🧠 Local Expert Agent

Responsible for:
- Hidden gems
- Food recommendations
- Attractions
- Cultural experiences
- Local insights

---

## 💼 Travel Concierge Agent

Responsible for:
- Day-wise itinerary
- Hotel recommendations
- Budget planning
- Transportation
- Schedule optimization

---

# ⚙️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Streamlit | Frontend UI |
| CrewAI | Multi-Agent Framework |
| OpenRouter | LLM Gateway |
| DeepSeek V4 Flash | AI Model |
| Serper API | Web Search |
| Browserless | Website Scraping |
| LangChain Tools | Tool Integration |
| GitHub | Version Control |
| Streamlit Cloud | Deployment |

---

# 🏗️ System Architecture

```text
                ┌──────────────────────┐
                │     Streamlit UI     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │     CrewAI Crew      │
                └──────────┬───────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼

┌────────────────┐ ┌────────────────┐ ┌────────────────┐
│ City Selection │ │  Local Expert  │ │ Travel Planner │
│     Agent      │ │     Agent      │ │     Agent      │
└────────────────┘ └────────────────┘ └────────────────┘
        │                  │                  │
        └──────────┬───────┴──────────┬───────┘
                   ▼                  ▼

          ┌──────────────────────────────┐
          │      OpenRouter + LLM        │
          └──────────────────────────────┘
```

---

# 🚀 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/jack-coder5416/travel_planner
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Streamlit App

```bash
streamlit run streamlit_app.py
```

---

# 🌐 Deployment

This project can be deployed easily using:

- Streamlit Community Cloud
- GitHub

Secrets can be securely managed using Streamlit Secrets Manager.

---

# 🔥 Future Improvements

- Google Maps Integration
- Flight APIs
- Hotel Booking APIs
- PDF Export
- Voice Assistant
- AI Chat Travel Assistant
- Memory & RAG
- Real-Time Weather
- Expense Optimization
- Multi-language Support

---

# 📈 Potential Use Cases

- AI Travel Startup MVP
- Hackathon Project
- Portfolio Project
- AI Agent Demonstration
- Personalized Trip Planning
- Travel Recommendation Platform

---

# 👨‍💻 Author

## Jatin Pal

Software Engineer | AI Engineer

- AI Agents
- CrewAI
- Generative AI
- FastAPI
- React
- RAG Systems
- Multi-Agent Workflows

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
🚀 Contribute improvements  

---

# 📜 License

MIT License

---

# ❤️ Built With

- CrewAI
- Streamlit
- OpenRouter
- DeepSeek
- Python
- LangChain
