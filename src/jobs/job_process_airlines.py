from src.pipeline.common.extract import SchipholHttp

class JobAirlines:
   def __init__(self):
      self.schipol = SchipholHttp()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      return self.schipol.getAirlines()


job = JobAirlines()
print(job.initJob())

