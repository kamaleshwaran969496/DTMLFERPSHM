import sqlite3

conn = sqlite3.connect("soldier_health.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM readings")

conn.commit()
conn.close()

print("Database Cleared Successfully!")