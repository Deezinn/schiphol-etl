from src.pipeline.common.extract import SchipholHttp
from src.pipeline.aircrafttypes.transform import Transform
from src.pipeline.aircrafttypes.load import save_in_csv

class JobAircraftTypes:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      rawContent = self.schipol.getAircrafttypes()

      processContent = self.schipolTransform.transformToDataframe(rawContent)

      save_in_csv(processContent)
      return processContent

if __name__ == "__main__":
   job = JobAircraftTypes()
   job.initJob()

