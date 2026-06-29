from src.database_monitor import get_database_data
from src.backup_monitor import get_backup_data
from src.backup_analyzer import analyze_backup
from src.ai.incident_summarizer import generate_incident_summary

def run_pipeline():

    print("\n🚀 Starting AI DB Operations Pipeline...\n")

    # STEP 1: DATA INGESTION
    databases = get_database_data()
    backups = get_backup_data()

    print("✅ Data ingestion completed")

    # STEP 2: ANALYSIS ENGINE
    incidents = []

    for backup in backups:
        analysis = analyze_backup(backup)
        if analysis:
            incidents.append(analysis)

    print(f"⚠️ Incidents detected: {len(incidents)}")

    # STEP 3: AI ENRICHMENT
    ai_reports = []

    for incident in incidents:
        ai_output = generate_incident_summary(incident)

        ai_reports.append({
            "incident": incident,
            "ai_report": ai_output
        })

    print("🧠 AI summarization completed")

    return {
        "databases": databases,
        "incidents": incidents,
        "ai_reports": ai_reports
    }