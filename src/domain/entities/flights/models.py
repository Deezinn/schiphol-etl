#
from dataclasses import dataclass
from datetime import date

@dataclass
class FlightsModel:
  """
  Classe de modelo da entidade Flights.
  """
  id: int
  lastUpdatedAt: date
  actualLandingTime: date
  aircraftType: str
  baggageClaim: str
  estimatedLandingTime: date
  expectedTimeOnBelt: date
  flightDirection: str
  flightName: str
  flightNumber: int
  isOperationalFlight: bool
  mainFlight: str
  prefixIATA: str
  prefixICAO: str
  airlineCode: int
  publicFlightState: str
  route: str
  scheduleDateTime: date
  scheduleDate: date
  serviceType: str
  schemaVersion: float
  codeshares: int

