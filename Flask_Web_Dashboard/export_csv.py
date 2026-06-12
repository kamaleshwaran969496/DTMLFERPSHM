import sqlite3
import pandas as pd

conn = sqlite3.connect("soldier_health.db")

df = pd.read_sql_query(
    "SELECT * FROM readings",
    conn
)

df.to_csv("soldier_health_log.csv", index=False)

conn.close()

print("CSV Exported Successfully!")