from src.pipeline.common.extract import SchipholHttp

class JobAircraftTypes:
   def __init__(self):
      self.schipol = SchipholHttp()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      return self.schipol.getAircrafttypes()


job = JobAircraftTypes()
print(job.initJob())

