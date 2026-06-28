from src.monitors.backup_monitor import get_backup_status
from src.analysis.backup_analyzer import analyze_backup_compliance

df = get_backup_status()

results = analyze_backup_compliance(df)

for item in results:

    print(item)