import json

import pandas as pd


class SchipholTransform:
   def __init__(self):
      self.__flights = None
      self.__airlines = None
      self.__destinations = None
      self.__aircrafttypes = None

   def loadContentContext(self,contents):
      mapping = {
            'flights': '_SchipholTransform__flights',
            'airlines': '_SchipholTransform__airlines',
            'destinations': '_SchipholTransform__destinations',
            'aircraftTypes': '_SchipholTransform__aircrafttypes'
      }

      for content in contents:
         key = list(content.keys())[0]
         value = list(content.values())[0]

         if key in mapping:
            setattr(self, mapping[key], value)

   def __repr__(self):
      return f"Flights: {self.__flights}, Airlines: {self.__airlines}, Destinations: {self.__destinations}, AircraftTypes: {self.__aircrafttypes}"


   def returnEntity(self):
      print(self.__airlines)
