from .jobs.job_process import Job

class SchipholOrchestrator:
  def __init__(self):
    self.job = Job()

  def run_all(self):
    self.job.initJob()


if __name__ == "__main__":
  orchestrator = SchipholOrchestrator()
  orchestrator.run_all()
