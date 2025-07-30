import requests
from requests import HTTPError # Importar os erros
from ...config.env_credentials import credentials

class FlightsHttp:
   def __init__(self):
      pass

   def getFlights(self, url):
      try:
         result = requests.get(url, headers=credentials)
      except Exception as e:
         raise e

      return result.json()

