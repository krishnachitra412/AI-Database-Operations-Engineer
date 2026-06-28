from src.db_connection import get_connection

try:
    conn = get_connection()
    print("Connection Successful")
    conn.close()

except Exception as e:
    print("Connection Failed")
    print(e)