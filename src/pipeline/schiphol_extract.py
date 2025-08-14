import pandas as pd
import requests
import json
from requests import ConnectionError, ConnectTimeout, HTTPError, JSONDecodeError
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
      except AttributeError as e:
         raise AttributeError("A atribuição ao atributo da classe 'self.__objUrlApi' falhou.") from e
      except IndexError as e:
         raise IndexError("A identação falhou, verifique o código.") from e
      except Exception as e:
         raise RuntimeError("Não conseguiu processar as urls.") from e
      else:
         try:
            for link in self.__objUrlApi.values():
               tempData = requests.get(link, headers=credentials)
               tempData.raise_for_status()
               if tempData.status_code == 200:
                  self.__content.append(tempData.json())
               else:
                  raise ValueError(f"Deu erro -> status_code: {tempData.status_code}")
         except:
            pass
         else:
            return self.__content

