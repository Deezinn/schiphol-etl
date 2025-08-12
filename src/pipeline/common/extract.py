
import time

import pandas as pd
import requests

from ...config.env_credentials import credentials
from ...json.load_json import JsonLoad
from ...constants import URLAPI

class SchipholHttp:
   def __init__(self):
      self.__objUrlApi = {}
      self.__content = []

   def getDataFromApi(self, urls):
      if not urls:
         raise InterruptedError("Não achei as urls.")

      if type(urls):
         raise TypeError("O tipo das urls é diferente, só aceita lista que contém objetos.")

      try:
         for data in urls:
            self.__objUrlApi[list(data.keys())[0]] = list(data.values())[0]
      except Exception as e:
         raise ValueError('')
      else:
         try:
            for link in self.__objUrlApi.values():
               tempData = requests.get(link, headers=credentials)
               tempData.raise_for_status()
               if tempData.status_code == 200:
                  self.__content.append(tempData.text)
         except:
            pass
         else:
            return self.__content
