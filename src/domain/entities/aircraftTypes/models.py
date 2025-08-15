from dataclasses import dataclass

@dataclass
class AircraftTypesModel:
  """
  Classe de modelo da entidade AircraftType.
  """
  id: int
  iataMain: int
  iataSub: int
  longDescription: str
  shortDescription: str
