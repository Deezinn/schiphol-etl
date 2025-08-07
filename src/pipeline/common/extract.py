
import time

import pandas as pd
import requests

from ...config.env_credentials import credentials
from ...json.load_json import JsonLoad


class SchipholHttp:
   def __init__(self):
      self.json = JsonLoad()
      if self.json:
         self.__flightsApiUrl = self.json.getJsonUrl()['flights']
         self.__airlinesApiUrl = self.json.getJsonUrl()['airlines']
         self.__destinationsApiUrl = self.json.getJsonUrl()['destinations']
         self.__aircrafttypesApiUrl = self.json.getJsonUrl()['aircrafttypes']


   def getAirlines(self):
      try:
         result = requests.get(self.__airlinesApiUrl, headers=credentials)
         result.raise_for_status()
      except Exception as e:
         raise e
      else:
         return result.json()

   def getDestinations(self):
      try:
         result = requests.get(self.__destinationsApiUrl, headers=credentials)
         result.raise_for_status()
      except Exception as e:
         raise e
      else:
         return result.json()

   def getAircrafttypes(self):
      try:
         result = requests.get(self.__aircrafttypesApiUrl, headers=credentials)
         result.raise_for_status()
      except Exception as e:
         raise e
      else:
         return result.json()

   def getFlights(self):
      try:
         result = requests.get(self.__flightsApiUrl, headers=credentials)
         result.raise_for_status()
      except Exception as e:
         raise e
      else:
         return result.json()

