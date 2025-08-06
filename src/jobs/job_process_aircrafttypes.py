from src.pipeline.common.extract import SchipholHttp
from src.pipeline.aircrafttypes.transform import Transform


class JobAircraftTypes:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      rawContent = self.schipol.getAircrafttypes()

      self.schipolTransform.transformToDataframe(rawContent)

      return self.schipol.getAircrafttypes()

if __name__ == "__main__":
   job = JobAircraftTypes()
   job.initJob()

