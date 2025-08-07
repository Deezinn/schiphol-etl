import json

import pandas as pd
import requests

from ...config.env_credentials import credentials
import time

class SchipholHttp:
   def __init__(self, url_config_path='urls.json'):
      self.__flightsApiUrl = None
      self.__airlinesApiUrl = None
      self.__destinationsApiUrl = None
      self.__aircrafttypesApiUrl = None
      self.url_config_path = url_config_path

   def getAirlines(self):
      try:
         result = requests.get(self.__airlinesApiUrl, headers=credentials)
      except Exception as e:
         raise e
      else:
         return result.json()

   def getDestinations(self):
      try:
         result = requests.get(self.__destinationsApiUrl, headers=credentials)
      except Exception as e:
         raise e
      else:
         return result.json()

   def getAircrafttypes(self):
      try:
         result = requests.get(self.__aircrafttypesApiUrl, headers=credentials)
      except Exception as e:
         raise e
      else:
         return result.json()

   def getFlights(self):
      try:
         result = requests.get(self.__flightsApiUrl, headers=credentials)
      except Exception as e:
         raise e
      else:
         return result.json()

   def getJsonUrl(self):
      try:
         with open(self.url_config_path, 'r') as file:
            self.__contentJson = json.load(file)
            return self.__contentJson
      except Exception as e:
         raise FileExistsError("Erro ao carregar arquivo", e)


   def getUrlApiFromJson(self):
      contentJson = self.getJsonUrl()
      for k,v in contentJson.items():
         match k:
            case 'flights':
               self.__flightsApiUrl = v
            case 'airlines':
               self.__airlinesApiUrl = v
            case 'destinations':
               self.__destinationsApiUrl = v
            case 'aircrafttypes':
               self.__aircrafttypesApiUrl = v
            case _:
               return "Não achamos a opção desejada"

      else:
         return 'Não achamos sua fonte de dados'

