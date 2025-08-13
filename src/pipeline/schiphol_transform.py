import pandas as pd
from src.pipeline.schiphol_entity import SchipholEntity

class SchipholTransform:
   def __init__(self, entitys: SchipholEntity):
      self.entitys = entitys

   def transform_flights(self):
      if not self.entitys.flights:
         return []
      print(self.entitys.flights)

   def transform_airlines(self):
      if not self.entitys.airlines:
         return []
      print(self.entitys.airlines)

   def transform_destinations(self):
      if not self.entitys.destinations:
         return []
      print(self.entitys.destinations)

   def transform_aircraftTypes(self):
      if not self.entitys.aircrafttypes:
         return []
      print(self.entitys.aircrafttypes)

