from dataclasses import dataclass

@dataclass
class DestinationsModel:
  """
  Classe de modelo da entidade Destinations.
  """
  id: int
  country: str
  iata: str
  publicName: str
  city: str
