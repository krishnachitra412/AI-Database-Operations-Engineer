# ==================================================
# DATABASE INVENTORY
# ==================================================

GET_ALL_DATABASES = """
SELECT
    database_id,
    database_name,
    database_size_gb,
    growth_rate_percent
FROM ops.database_inventory
ORDER BY database_name;
"""


# ==================================================
# SERVER INVENTORY
# ==================================================

GET_ALL_SERVERS = """
SELECT
    server_id,
    server_name,
    environment,
    cpu_cores,
    total_memory_gb,
    created_date
FROM ops.server_inventory
ORDER BY server_name;
"""


# ==================================================
# BACKUP COMPLIANCE
# ==================================================

GET_BACKUP_COMPLIANCE = """
SELECT
    d.database_id,
    d.database_name,
    b.last_backup_time,
    b.backup_status
FROM ops.backup_status b
INNER JOIN ops.database_inventory d
    ON b.database_id = d.database_id
ORDER BY d.database_name;
"""


# ==================================================
# FAILED JOBS
# ==================================================

GET_JOB_HISTORY = """
SELECT
    j.job_id,
    d.database_name,
    j.job_name,
    j.execution_time,
    j.status,
    j.duration_seconds
FROM ops.job_execution_history j
INNER JOIN ops.database_inventory d
    ON j.database_id = d.database_id
ORDER BY j.execution_time DESC;
"""


GET_FAILED_JOBS = """
SELECT
    j.job_id,
    d.database_name,
    j.job_name,
    j.execution_time,
    j.status,
    j.duration_seconds
FROM ops.job_execution_history j
INNER JOIN ops.database_inventory d
    ON j.database_id = d.database_id
WHERE j.status = 'FAILED'
ORDER BY j.execution_time DESC;
"""


# ==================================================
# INCIDENTS
# ==================================================

GET_ALL_INCIDENTS = """
SELECT
    i.incident_id,
    d.database_name,
    i.incident_type,
    i.severity,
    i.incident_time
FROM ops.incident_history i
INNER JOIN ops.database_inventory d
    ON i.database_id = d.database_id
ORDER BY i.incident_time DESC;
"""


GET_HIGH_SEVERITY_INCIDENTS = """
SELECT
    i.incident_id,
    d.database_name,
    i.incident_type,
    i.severity,
    i.incident_time
FROM ops.incident_history i
INNER JOIN ops.database_inventory d
    ON i.database_id = d.database_id
WHERE i.severity = 'HIGH'
ORDER BY i.incident_time DESC;
"""


# ==================================================
# DATABASE GROWTH ANALYSIS
# ==================================================

GET_DATABASE_GROWTH = """
SELECT
    database_id,
    database_name,
    database_size_gb,
    growth_rate_percent
FROM ops.database_inventory
ORDER BY growth_rate_percent DESC;
"""