from src.pipeline.extract import SchipholHttp
from src.pipeline.transform import SchipholTransform
from src.pipeline.load import save_in_csv
from ..constants import URLAPI


class Job:
   def __init__(self):
      self.schipol = SchipholHttp()
      self.schipolTransform = SchipholTransform()

   def initJob(self):
      rawContent = self.schipol.getDataFromApi(URLAPI)
      processContent = self.schipolTransform.loadContentContext(rawContent)
      self.schipolTransform.returnEntity()

      # return save_in_csv(processContent['dataframe'], processContent['tag'])



job = Job()
job.initJob()
