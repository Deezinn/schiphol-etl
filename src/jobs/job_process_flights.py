from src.pipeline.common.extract import SchipholHttp
from src.pipeline.flights.transform import Transform
class JobFlights:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      rawContent = self.schipol.getFlights()

      self.schipolTransform.transformToDataframe(rawContent)
      return None


job = JobFlights()
job.initJob()

