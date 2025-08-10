from .jobs.job_process_aircrafttypes import JobAircraftTypes
from .jobs.job_process_airlines import JobAirlines
from .jobs.job_process_destinations import JobDestinations
from .jobs.job_process_flights import JobFlights

class SchipholOrchestrator:
  def __init__(self):
    self.jobs = [
      JobAircraftTypes(),
      JobAirlines(),
      JobDestinations(),
      JobFlights()
    ]

  def run_all(self):
    for job in self.jobs:
        job.initJob()


if __name__ == "__main__":
  orchestrator = SchipholOrchestrator()
  orchestrator.run_all()
