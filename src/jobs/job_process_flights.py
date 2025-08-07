from src.pipeline.common.extract import SchipholHttp
from src.pipeline.flights.transform import Transform
from src.pipeline.flights.load import save_in_csv

class JobFlights:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      rawContent = self.schipol.getFlights()

      processContent = self.schipolTransform.transformToDataframe(rawContent)
      print(processContent)
      save_in_csv(processContent)
      return processContent

if __name__ == "__main__":
   job = JobFlights()
   job.initJob()

