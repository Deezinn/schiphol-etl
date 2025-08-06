from src.pipeline.common.extract import SchipholHttp

class JobDestinations:
   def __init__(self):
      self.schipol = SchipholHttp()

   def initJob(self):
      self.schipol.getUrlApiFromJson()
      return self.schipol.getDestinations()


job = JobDestinations()
print(job.initJob())

