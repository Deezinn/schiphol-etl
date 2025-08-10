from src.pipeline.common.extract import SchipholHttp
from src.pipeline.aircrafttypes.transform import Transform
from src.pipeline.common.load import save_in_csv

class JobAircraftTypes:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      rawContent = self.schipol.getAircrafttypes()
      processContent = self.schipolTransform.transformToDataframe(rawContent)
      return save_in_csv(processContent['dataframe'], processContent['tag'])


