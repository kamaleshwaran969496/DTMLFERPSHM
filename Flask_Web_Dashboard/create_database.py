import sqlite3

conn = sqlite3.connect("soldier_health.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS readings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    bpm REAL,
    spo2 REAL,
    temperature REAL,
    humidity REAL,
    ax INTEGER,
    ay INTEGER,
    az INTEGER,
    latitude REAL,
    longitude REAL
)
""")

conn.commit()
conn.close()

print("Database created successfully!")