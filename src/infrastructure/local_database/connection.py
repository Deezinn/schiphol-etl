import sqlite3

class SqliteConnect:
  def __init__(self, db_path):
    self.db_path = db_path

  def init_connection(self, query = None):
    if self.db_path:
      import os
      os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

      try:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        print("Inicializando o banco de dados")
        if query:
          cursor.execute(query)
          result = cursor.fetchall()
          if result:
            print('Consulta processada!')
            cursor.close()
        else:
          raise ValueError("Não consegui processar a query, provavelmente veio nulo ou sintaxe errada")
      except sqlite3.Error as error:
        print("erro no sqlite", error)
      finally:
        if conn:
          conn.close()
          print("Conexão finalizada!")
