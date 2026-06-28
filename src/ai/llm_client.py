def generate_response(prompt: str, model: str = "gpt-4o-mini"):
    return f"""
[MOCK AI RESPONSE]

Executive Summary:
This is a simulated incident analysis for testing purposes.

Technical Analysis:
The system detected a backup failure condition in the database environment.

Recommended Actions:
1. Check SQL Agent jobs
2. Validate storage space
3. Re-run backup job

Raw Prompt Received:
{prompt}
"""