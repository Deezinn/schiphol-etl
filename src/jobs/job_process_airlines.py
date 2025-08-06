from src.pipeline.common.extract import SchipholHttp
from src.pipeline.airlines.transform import Transform


class JobAirlines:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      rawContent = self.schipol.getAirlines()

      self.schipolTransform.transformToDataframe(rawContent)

      return None


job = JobAirlines()
job.initJob()

