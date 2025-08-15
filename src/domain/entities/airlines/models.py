from dataclasses import dataclass

@dataclass
class AirlinesModel:
  """
  Classe de modelo da entidade Airlines.
  """
  id: int
  iata: str
  icao: str
  nvls: int
  publicName: str
