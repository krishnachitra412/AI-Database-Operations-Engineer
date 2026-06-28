import pandas as pd

from src.db_connection import get_connection
from src.sql_queries import GET_ALL_DATABASES


def get_database_inventory():

    conn = get_connection()

    df = pd.read_sql(
        GET_ALL_DATABASES,
        conn
    )

    conn.close()

    return df