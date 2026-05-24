import streamlit as st
from datetime import datetime, timedelta
import time

from src.travel_planner.crew import TravelPlannerCrew


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown(
    """
    <style>

    /* FORCE DARK MODE */

    html, body, [class*="css"] {
        background-color: #0e1117 !important;
        color: white !important;
    }

    .stApp {
        background-color: #0e1117;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    .hero-title {
        font-size: 56px;
        font-weight: 800;
        background: linear-gradient(90deg,#00DBDE,#FC00FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #d1d5db;
        margin-bottom: 35px;
        line-height: 1.7;
    }

    .card {
        background-color: #161b22;
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.35);
    }

    .agent-card {
        background: linear-gradient(135deg,#1f2937,#111827);
        padding: 22px;
        border-radius: 18px;
        border: 1px solid #374151;
        margin-bottom: 18px;
        transition: 0.3s ease;
    }

    .agent-card:hover {
        transform: translateY(-4px);
        border: 1px solid #7c3aed;
    }

    .result-card {
        background: linear-gradient(135deg,#111827,#1e293b);
        padding: 30px;
        border-radius: 22px;
        border: 1px solid #374151;
        margin-top: 20px;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg,#2563eb,#7c3aed);
        color: white;
        border-radius: 14px;
        height: 55px;
        font-size: 18px;
        font-weight: 700;
        border: none;
    }

    .stButton > button:hover {
        opacity: 0.92;
    }

    .stDownloadButton > button {
        width: 100%;
        border-radius: 14px;
        height: 50px;
        font-weight: 700;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================
# HEADER
# =========================

st.markdown(
    """
    <div class='hero-title'>🌍 AI Travel Planner</div>

    <div class='hero-subtitle'>
    Plan intelligent trips using CrewAI multi-agent systems.
    Get destination recommendations, local insights,
    travel itineraries and hidden gems powered by AI.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# MAIN LAYOUT
# =========================

left_col, right_col = st.columns([1.1, 1])


# =========================
# LEFT SECTION
# =========================

with left_col:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## ✈️ Trip Information")

    country = st.text_input(
        "Country / Destination",
        placeholder="Example: India, Japan, Switzerland"
    )

    current_date = st.date_input(
        "Trip Starting Date",
        value=datetime.today(),
        min_value=datetime.today(),
        max_value=datetime.today() + timedelta(days=180)
    )

    number_of_days = st.slider(
        "Number of Days",
        min_value=1,
        max_value=30,
        value=5
    )

    end_date = current_date + timedelta(days=number_of_days)

    st.info(f"📅 Estimated End Date: {end_date}")

    plan_trip = st.button("🚀 Generate AI Travel Plan")

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# RIGHT SECTION
# =========================

with right_col:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.markdown("## 🤖 AI Agent Workflow")

    st.markdown(
        """
        <div class='agent-card'>
            <h4>🏙️ City Selection Agent</h4>
            <p>
            Finds the best cities and destinations based on weather,
            popularity, safety and travel experience.
            </p>
        </div>

        <div class='agent-card'>
            <h4>🧠 Local Expert Agent</h4>
            <p>
            Discovers attractions, hidden gems,
            food places and local experiences.
            </p>
        </div>

        <div class='agent-card'>
            <h4>💼 Travel Concierge Agent</h4>
            <p>
            Creates complete itineraries,
            travel schedules and optimized planning.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================
# RUN CREW
# =========================

if plan_trip:

    if not country:
        st.error("Please enter a destination.")
        st.stop()

    inputs = {
        "country": country,
        "current_date": str(current_date),
        "number_of_days": number_of_days
    }

    st.markdown("---")

    progress_bar = st.progress(0)

    status = st.empty()

    city_box = st.empty()
    local_box = st.empty()
    concierge_box = st.empty()

    final_result = st.empty()

    try:

        # =========================
        # AGENT 1
        # =========================

        status.info("🏙️ City Selection Agent Working...")

        city_box.markdown(
            """
            <div class='agent-card'>
            <h3>🏙️ City Selection Agent</h3>

            ✅ Researching best cities  
            ✅ Checking weather conditions  
            ✅ Comparing destinations  
            ✅ Finding tourist attractions  
            </div>
            """,
            unsafe_allow_html=True
        )

        progress_bar.progress(25)

        time.sleep(1)

        # =========================
        # AGENT 2
        # =========================

        status.info("🧠 Local Expert Agent Working...")

        local_box.markdown(
            """
            <div class='agent-card'>
            <h3>🧠 Local Expert Agent</h3>

            ✅ Searching hidden gems  
            ✅ Finding cafes & restaurants  
            ✅ Exploring local culture  
            ✅ Looking for experiences  
            </div>
            """,
            unsafe_allow_html=True
        )

        progress_bar.progress(50)

        time.sleep(1)

        # =========================
        # AGENT 3
        # =========================

        status.info("💼 Travel Concierge Agent Working...")

        concierge_box.markdown(
            """
            <div class='agent-card'>
            <h3>💼 Travel Concierge Agent</h3>

            ✅ Preparing itinerary  
            ✅ Optimizing schedule  
            ✅ Planning transportation  
            ✅ Creating final travel experience  
            </div>
            """,
            unsafe_allow_html=True
        )

        progress_bar.progress(75)

        time.sleep(1)

        # =========================
        # EXECUTE CREW
        # =========================

        status.info("🤖 CrewAI is generating final plan...")

        result = TravelPlannerCrew().crew().kickoff(
            inputs=inputs
        )

        progress_bar.progress(100)

        status.success("✅ Travel plan generated successfully!")

        final_result.markdown(
            f"""
            <div class='result-card'>
                <h2>🌟 Your AI Generated Travel Plan</h2>
                <br>
                {str(result)}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.download_button(
            label="📥 Download Travel Plan",
            data=str(result),
            file_name="travel_plan.txt",
            mime="text/plain"
        )

    except Exception as e:

        st.error(
            f"Error while running CrewAI: {str(e)}"
        )


# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown(
    """
    <center>
    <h4>Made by Jatin Pal (paljatin479@gmail.com)</h4>
    </center>
    """,
    unsafe_allow_html=True
)