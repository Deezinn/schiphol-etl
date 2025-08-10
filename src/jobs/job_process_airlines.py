from src.pipeline.common.extract import SchipholHttp
from src.pipeline.airlines.transform import Transform
from src.pipeline.common.load import save_in_csv

class JobAirlines:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      rawContent = self.schipol.getAirlines()

      processContent = self.schipolTransform.transformToDataframe(rawContent)
      save_in_csv(processContent['dataframe'], processContent['tag'])
      return processContent

