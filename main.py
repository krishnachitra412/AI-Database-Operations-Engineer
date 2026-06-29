from src.core.orchestrator import execute

if __name__ == "__main__":

    print("\n==============================")
    print(" AI DATABASE OPS ENGINE START ")
    print("==============================\n")

    result = execute()

    print("\n==============================")
    print(" EXECUTION SUMMARY ")
    print("==============================\n")

    print(f"Incidents Found: {len(result['incidents'])}")

    print("\nSample AI Report:\n")
    if result["ai_reports"]:
        print(result["ai_reports"][0]["ai_report"])