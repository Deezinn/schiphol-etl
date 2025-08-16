import pandas as pd

class SchipholTransform:
   def __init__(self, entitys):
      self.entitys = entitys

   def transform_flights(self):
      flightsDataframe = None
      entityKey = 'flights'
      if not self.entitys[entityKey]:
         return []
      else:
         flightsDataframe = pd.DataFrame(self.entitys[entityKey])
         if isinstance(flightsDataframe, pd.DataFrame):
            return flightsDataframe

   def transform_airlines(self):
      airlinesDataframe = None
      entityKey = 'airlines'
      if not self.entitys[entityKey]:
         return []
      else:
         airlinesDataframe = pd.DataFrame(self.entitys[entityKey])
         if isinstance(airlinesDataframe, pd.DataFrame):
            return airlinesDataframe

   def transform_destinations(self):
      destinationsDataframe = None
      entityKey = 'destinations'
      if not self.entitys[entityKey]:
         return []
      else:
         destinationsDataframe = pd.DataFrame(self.entitys[entityKey])
         if isinstance(destinationsDataframe, pd.DataFrame):
            return destinationsDataframe

   def transform_aircraftTypes(self):
      aircraftTypes = None
      entityKey = 'aircraftTypes'
      if not self.entitys[entityKey]:
         return []
      else:
         aircraftTypes = pd.DataFrame(self.entitys[entityKey])
         if isinstance(aircraftTypes, pd.DataFrame):
            return aircraftTypes

   def load_all(self):
      self.transform_aircraftTypes()
      self.transform_airlines()
      self.transform_destinations()
      self.transform_flights()
