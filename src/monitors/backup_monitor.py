import pandas as pd

from src.db_connection import get_connection
from src.sql_queries import GET_BACKUP_COMPLIANCE


def get_backup_status():

    conn = get_connection()

    df = pd.read_sql(
        GET_BACKUP_COMPLIANCE,
        conn
    )

    conn.close()

    return df