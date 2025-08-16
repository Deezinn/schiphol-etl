from src.pipeline.schiphol_extract import SchipholExtract
from src.pipeline.schiphol_transform import SchipholTransform
from src.infrastructure.parser.schiphol_contents_parser import SchipholContentsParser
from src.infrastructure.local_database.sqlite_execute import SqliteDatabase
# from src.pipeline.load import save_in_csv
from ..constants import URLAPI, default_path_db_local


class Job:
   def __init__(self):
      self.schipolExtract = SchipholExtract()
      self.schipholContentsParser = SchipholContentsParser()
      self.schipolTransform = None
      if default_path_db_local:
         self.sqliteDatabase = SqliteDatabase(default_path_db_local)

   def init_job(self):
      rawContent = self.schipolExtract.get_Data_FromApi(URLAPI)
      separatedContent = self.schipholContentsParser.load_from_contents(rawContent)
      if separatedContent:
         self.schipolTransform = SchipholTransform(separatedContent)
         self.schipolTransform.load_all()
      self.sqliteDatabase.execute_query(
         """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER
        )
    """ # teste
      )
      # return save_in_csv(processContent['dataframe'], processContent['tag'])
