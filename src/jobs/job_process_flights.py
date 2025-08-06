from src.pipeline.common.extract import SchipholHttp

class JobFlights:
   def __init__(self):
      self.schipol = SchipholHttp()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      return self.schipol.getFlights()


job = JobFlights()
print(job.initJob())

