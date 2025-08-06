from src.pipeline.common.extract import SchipholHttp
from src.pipeline.destinations.transform import Transform

class JobDestinations:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      rawContent = self.schipol.getDestinations()

      self.schipolTransform.transformToDataframe(rawContent)
      return None

job = JobDestinations()
job.initJob()

