from src.monitors.database_monitor import get_database_inventory
from src.monitors.backup_monitor import get_backup_status
from src.analysis.backup_analyzer import analyze_backup_compliance
from src.ai.incident_summarizer import generate_incident_summary


def run_pipeline():

    print("\n🚀 Starting AI DB Operations Pipeline...\n")

    # STEP 1: DATA INGESTION
    databases = get_database_inventory()
    backups = get_backup_status()

    print("✅ Data ingestion completed")

    # DEBUG
    print("\n=== BACKUP DATA TYPE ===")
    print(type(backups))

    print("\n=== BACKUP DATA ===")
    print(backups.head())

    # STEP 2: ANALYSIS ENGINE
    incidents = analyze_backup_compliance(backups)

    print(f"\n⚠️ Incidents detected: {len(incidents)}")

    # STEP 3: AI ENRICHMENT
    ai_reports = []

    for incident in incidents:

        ai_output = generate_incident_summary(incident)

        ai_reports.append(
            {
                "incident": incident,
                "ai_report": ai_output
            }
        )

    print("🧠 AI summarization completed")

    return {
        "databases": databases,
        "incidents": incidents,
        "ai_reports": ai_reports
    }