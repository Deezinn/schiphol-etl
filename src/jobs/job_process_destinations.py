from src.pipeline.common.extract import SchipholHttp
from src.pipeline.destinations.transform import Transform
from src.pipeline.destinations.load import save_in_csv
class JobDestinations:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = Transform()

   def initJob(self):
      rawContent = self.schipol.getDestinations()

      processContent = self.schipolTransform.transformToDataframe(rawContent)
      print(processContent)
      save_in_csv(processContent)

if __name__ == "__main__":
   job = JobDestinations()
   job.initJob()

