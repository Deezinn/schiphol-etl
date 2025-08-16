import sqlite3
import os
class SqliteDatabase:
  def __init__(self, db_path):
    self.db_path = db_path
    if self.db_path:
      os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

  def execute_query(self, query = None):
    try:
      with sqlite3.connect(self.db_path) as connection:
        print("Conexão iniciada")
        cursor = connection.cursor()
        print("Iniciando query")
        cursor.execute(query)
        print("Query finalizada")
        print("Conexão finalizada")
        connection.commit()
    except sqlite3.Error as e:
      raise f"Erro{e}"
