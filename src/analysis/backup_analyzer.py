from datetime import datetime


def analyze_backup_compliance(df):

    findings = []

    current_time = datetime.now()

    for _, row in df.iterrows():

        backup_age = (
            current_time -
            row["last_backup_time"]
        ).total_seconds() / 3600

        if backup_age > 24:

            findings.append(
                {
                    "database": row["database_name"],
                    "issue": "Backup Older Than 24 Hours",
                    "severity": "HIGH"
                }
            )

    return findings