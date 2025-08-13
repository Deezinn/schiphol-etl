from src.pipeline.schiphol_extract import SchipholExtract
from src.pipeline.schiphol_transform import SchipholTransform
from src.pipeline.schiphol_entity import SchipholEntity
from src.pipeline.schiphol_mapper import SchipholMapper

# from src.pipeline.load import save_in_csv
from ..constants import URLAPI


class Job:
   def __init__(self):
      self.schipolExtract = SchipholExtract()
      self.schipholMapper = SchipholMapper()
      self.schipolEntity = SchipholEntity()
      self.schipolTransform = None

   def initJob(self):
      rawContent = self.schipolExtract.get_Data_FromApi(URLAPI)
      separatedContent= self.schipholMapper.load_from_contents(rawContent)
      entitys = self.schipolEntity.from_dict(separatedContent)
      if entitys:
         self.schipolTransform = SchipholTransform(entitys)
         self.schipolTransform.transform_flights()
         self.schipolTransform.transform_aircraftTypes()
         self.schipolTransform.transform_airlines()
         self.schipolTransform.transform_destinations()
      # return save_in_csv(processContent['dataframe'], processContent['tag'])
