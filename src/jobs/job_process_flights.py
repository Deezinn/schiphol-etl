from src.pipeline.common.extract import SchipholHttp
from src.pipeline.flights.transform import Transform
from src.pipeline.common.load import save_in_csv
class JobFlights:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      rawContent = self.schipol.getFlights()

      processContent = self.schipolTransform.transformToDataframe(rawContent)
      save_in_csv(processContent['dataframe'], processContent['tag'])
      return processContent
