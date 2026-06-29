import streamlit as st
import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from src.core.pipeline import run_pipeline

# MUST BE THE FIRST STREAMLIT COMMAND
st.set_page_config(
    page_title="AI Database Operations",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select View",
    [
        "Overview",
        "Incidents",
        "AI Reports"
    ]
)

# Header
st.title("🚀 AI Database Operations Center")

st.write(
    "Database Monitoring and AI Incident Management Platform"
)

# Execute Pipeline
results = run_pipeline()

# Common Metrics
database_count = len(results["databases"])
incident_count = len(results["incidents"])
ai_report_count = len(results["ai_reports"])

# ==========================
# OVERVIEW PAGE
# ==========================
if page == "Overview":

    st.subheader("Operations Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Databases",
            database_count
        )

    with col2:
        st.metric(
            "Incidents",
            incident_count
        )

    with col3:
        st.metric(
            "AI Reports",
            ai_report_count
        )

    st.markdown("---")

    st.subheader("Recent Incident Summary")

    if results["incidents"]:

        st.dataframe(
            results["incidents"],
            use_container_width=True
        )

    else:

        st.success(
            "No incidents detected"
        )

# ==========================
# INCIDENTS PAGE
# ==========================
elif page == "Incidents":

    st.subheader("Detected Incidents")

    if results["incidents"]:

        st.dataframe(
            results["incidents"],
            use_container_width=True
        )

    else:

        st.success(
            "No incidents detected"
        )

# ==========================
# AI REPORTS PAGE
# ==========================
elif page == "AI Reports":

    st.subheader("AI Incident Analysis")

    if results["ai_reports"]:

        for report in results["ai_reports"]:

            st.markdown("---")

            st.write("### Incident")

            st.json(
                report["incident"]
            )

            st.write("### AI Analysis")

            st.write(
                report["ai_report"]
            )

    else:

        st.info(
            "No AI reports generated"
        )