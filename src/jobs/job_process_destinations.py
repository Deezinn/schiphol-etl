from src.pipeline.common.extract import SchipholHttp
from src.pipeline.destinations.transform import Transform
from src.pipeline.common.load import save_in_csv

class JobDestinations:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      rawContent = self.schipol.getDestinations()

      processContent = self.schipolTransform.transformToDataframe(rawContent)
      save_in_csv(processContent['dataframe'], processContent['tag'])


