import sqlite3
from pathlib import Path
import csv

DB = Path(__file__).resolve().parent.parent / "data" / "ranking.db"

# Ensure DB and table exist
conn = sqlite3.connect(DB)
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS ranking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        puntuacion INTEGER NOT NULL,
        nivel INTEGER NOT NULL,
        fecha TEXT NOT NULL
    )
    """
)
conn.commit()

cursor = conn.execute(
    "SELECT nombre, puntuacion, fecha FROM ranking ORDER BY puntuacion DESC, fecha ASC"
)
rows = cursor.fetchall()
conn.close()

out = Path(__file__).resolve().parent.parent / "data" / "ranking_export.csv"
with open(out, "w", newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(["nombre", "puntuacion", "fecha"])
    w.writerows(rows)

print(f"DB: {DB}")
print(f"Exported {len(rows)} rows to: {out}")
if rows:
    for r in rows:
        print(r)
else:
    print("No hay registros en la tabla 'ranking'.")
