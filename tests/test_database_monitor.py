from src.monitors.database_monitor import get_database_inventory

df = get_database_inventory()

print(df)