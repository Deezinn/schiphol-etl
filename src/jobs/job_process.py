from src.pipeline.schiphol_extract import SchipholExtract
from src.pipeline.schiphol_transform import SchipholTransform
from src.infrastructure.parser.schiphol_contents_parser import SchipholContentsParser
from src.infrastructure.local_database.connection import SqliteConnect
# from src.pipeline.load import save_in_csv
from ..constants import URLAPI, default_path_db_local


class Job:
   def __init__(self):
      self.schipolExtract = SchipholExtract()
      self.schipholContentsParser = SchipholContentsParser()
      self.schipolTransform = None
      if default_path_db_local:
         self.sqliteConnect = SqliteConnect(default_path_db_local)

   def initJob(self):
      rawContent = self.schipolExtract.get_Data_FromApi(URLAPI)
      separatedContent = self.schipholContentsParser.load_from_contents(rawContent)
      if separatedContent:
         self.schipolTransform = SchipholTransform(separatedContent)
         self.schipolTransform.load_all()
      self.sqliteConnect.init_connection(query="""
         CREATE TABLE Employees (
            EmployeeID INT PRIMARY KEY,
            FirstName VARCHAR(50),
            LastName VARCHAR(50),
            Email VARCHAR(100) NOT NULL,
            HireDate DATE
         );
      """)
      # return save_in_csv(processContent['dataframe'], processContent['tag'])
