import streamlit as st

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from src.core.pipeline import run_pipeline

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select View",
    [
        "Overview",
        "Incidents",
        "AI Reports"
    ]
)

# Page Configuration
st.set_page_config(
    page_title="AI Database Operations",
    layout="wide"
)

# Header
st.title("🚀 AI Database Operations Center")

st.write(
    "Database Monitoring and AI Incident Management Platform"
)

# Execute Pipeline
results = run_pipeline()

# KPI Metrics
database_count = len(results["databases"])
incident_count = len(results["incidents"])
ai_report_count = len(results["ai_reports"])

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Databases", database_count)

with col2:
    st.metric("Incidents", incident_count)

with col3:
    st.metric("AI Reports", ai_report_count)

# Incident Table
st.subheader("Detected Incidents")

if results["incidents"]:
    st.dataframe(results["incidents"])
else:
    st.success("No incidents detected")

# AI Reports
st.subheader("AI Incident Analysis")

if results["ai_reports"]:

    for report in results["ai_reports"]:

        st.markdown("---")

        st.write("Incident:")
        st.json(report["incident"])

        st.write("AI Analysis:")
        st.write(report["ai_report"])

else:
    st.info("No AI reports generated")