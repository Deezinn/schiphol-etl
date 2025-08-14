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

         # isso vai para a camada de load apenas salvando em .csv para fazer o EDA e tratar os dados corretamente
      if isinstance(flightsDataframe, pd.DataFrame):
         flightsDataframe.to_csv(f'src/data/raw/{entityKey}.csv')

   def transform_airlines(self):
      airlinesDataframe = None
      entityKey = 'airlines'
      if not self.entitys[entityKey]:
         return []
      else:
         airlinesDataframe = pd.DataFrame(self.entitys[entityKey])

      # isso vai para a camada de load apenas salvando em .csv para fazer o EDA e tratar os dados corretamente
      if isinstance(airlinesDataframe, pd.DataFrame):
         airlinesDataframe.to_csv(f'src/data/raw/{entityKey}.csv')

   def transform_destinations(self):
      destinationsDataframe = None
      entityKey = 'destinations'
      if not self.entitys[entityKey]:
         return []
      else:
         destinationsDataframe = pd.DataFrame(self.entitys[entityKey])

      # isso vai para a camada de load apenas salvando em .csv para fazer o EDA e tratar os dados corretamente
      if isinstance(destinationsDataframe, pd.DataFrame):
         destinationsDataframe.to_csv(f'src/data/raw/{entityKey}.csv')

   def transform_aircraftTypes(self):
      aircraftTypes = None
      entityKey = 'aircraftTypes'
      if not self.entitys[entityKey]:
         return []
      else:
         aircraftTypes = pd.DataFrame(self.entitys[entityKey])
      # isso vai para a camada de load apenas salvando em .csv para fazer o EDA e tratar os dados corretamente
      if isinstance(aircraftTypes, pd.DataFrame):
         aircraftTypes.to_csv(f'src/data/raw/{entityKey}.csv')

   def load_all(self):
      self.transform_aircraftTypes()
      self.transform_airlines()
      self.transform_destinations()
      self.transform_flights()
