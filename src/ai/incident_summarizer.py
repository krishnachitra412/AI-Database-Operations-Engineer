from src.ai.llm_client import generate_response
from src.ai.prompt_builder import build_incident_prompt

def generate_incident_summary(incident: dict):
    prompt = build_incident_prompt(incident)
    return generate_response(prompt)