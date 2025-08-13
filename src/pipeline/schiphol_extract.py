import pandas as pd
import requests
import json

from ..config.env_credentials import credentials

class SchipholExtract:
   def __init__(self):
      self.__objUrlApi = {}
      self.__content = []

   def get_Data_FromApi(self, urls):
      if not urls:
         raise InterruptedError("Não achei as urls.")

      if not isinstance(urls, list):
         raise TypeError("O tipo das urls é diferente, só aceita lista que contém objetos.")

      try:
         for idx, data in enumerate(urls):
            self.__objUrlApi[list(data.keys())[0]] = list(data.values())[0]

      except Exception as e:
         raise ValueError('')
      else:
         try:
            for link in self.__objUrlApi.values():

               tempData = requests.get(link, headers=credentials)
               tempData.raise_for_status()

               if tempData.status_code == 200:
                  self.__content.append(tempData.json())
         except:
            pass
         else:
            return self.__content

