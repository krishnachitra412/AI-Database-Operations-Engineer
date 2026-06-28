def build_incident_prompt(incident: dict):
    return f"""
You are a senior Database Operations Engineer working in a production environment.

Analyze the following database incident:

Database: {incident.get('database')}
Issue: {incident.get('issue')}
Severity: {incident.get('severity')}
Timestamp: {incident.get('timestamp', 'N/A')}

Your response must include:

1. Executive Summary (non-technical, business impact)
2. Technical Analysis (DBA level explanation)
3. Recommended Actions (step-by-step)
4. Risk if ignored

Keep it concise and production-ready.
"""