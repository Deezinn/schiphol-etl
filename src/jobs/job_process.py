from src.pipeline.schiphol_extract import SchipholExtract
from src.pipeline.schiphol_transform import SchipholTransform
from src.domain.mappers.schiphol_mapper import SchipholMapper

# from src.pipeline.load import save_in_csv
from ..constants import URLAPI


class Job:
   def __init__(self):
      self.schipolExtract = SchipholExtract()
      self.schipholMapper = SchipholMapper()
      self.schipolTransform = None

   def initJob(self):
      rawContent = self.schipolExtract.get_Data_FromApi(URLAPI)
      separatedContent = self.schipholMapper.load_from_contents(rawContent)
      if separatedContent:
         self.schipolTransform = SchipholTransform(separatedContent)
         self.schipolTransform.load_all()
      # return save_in_csv(processContent['dataframe'], processContent['tag'])
