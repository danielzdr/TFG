import sqlite3
from pathlib import Path
from datetime import datetime


class Ranking:
    def __init__(self, db_path=None):
        if db_path is None:
            db_path = Path(__file__).resolve().parent.parent / "data" / "ranking.db"
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
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
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_ranking_puntuacion ON ranking (puntuacion DESC, fecha ASC)"
            )

    def guardar_puntuacion(self, nombre: str, puntuacion: int, nivel: int):
        nombre = (nombre or "ANON").strip()[:20]
        if not nombre:
            nombre = "ANON"
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO ranking (nombre, puntuacion, nivel, fecha) VALUES (?, ?, ?, ?)",
                (nombre, puntuacion, nivel, fecha),
            )

    def obtener_top(self, limit=10):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT nombre, puntuacion, nivel, fecha FROM ranking "
                "ORDER BY puntuacion DESC, fecha ASC LIMIT ?",
                (limit,),
            )
            return cursor.fetchall()
