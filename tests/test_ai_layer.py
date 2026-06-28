from src.ai.incident_summarizer import generate_incident_summary

sample_incident = {
    "database": "SalesDB",
    "issue": "Backup not completed for 40 hours",
    "severity": "HIGH",
    "timestamp": "2026-06-28"
}

result = generate_incident_summary(sample_incident)

print("\n===== AI INCIDENT REPORT =====\n")
print(result)