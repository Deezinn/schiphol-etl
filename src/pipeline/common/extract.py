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
         return result.json()
      except Exception as e:
         raise e
      return print(self.contentFlights)

   def getDestinations(self):
      try:
         result = requests.get(self.__destinationsApiUrl, headers=credentials)
         return result.json()
      except Exception as e:
         raise e
      return print(self.contentFlights)

   def getAircrafttypes(self):
      try:
         result = requests.get(self.__aircrafttypesApiUrl, headers=credentials)
         return result.json()
      except Exception as e:
         raise e
      return print(self.contentFlights)

   def getFlights(self):
      try:
         result = requests.get(self.__flightsApiUrl, headers=credentials)
         return result.json()
      except Exception as e:
         raise e
      return print(self.contentFlights)

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
         if k == 'flights':
            self.__flightsApiUrl = v
         if k == 'airlines':
            self.__airlinesApiUrl = v
         if k == 'destinations':
            self.__destinationsApiUrl = v
         if k == 'aircrafttypes':
            self.__aircrafttypesApiUrl = v
      else:
         return 'Não achamos sua fonte de dados'

a = SchipholHttp()
a.getUrlApiFromJson()
print(a.getFlights(),'flights')
print(a.getAirlines(),'airlines')
print(a.getAircrafttypes(),'aircrafttypes')
print(a.getDestinations(),'destinations')
