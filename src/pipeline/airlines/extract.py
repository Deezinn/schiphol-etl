import requests
from ...config.env_credentials import credentials

class AirlinesHttp:
   def __init__(self):
      pass

   def getAirlines(self, url):
      result = requests.get(url, headers=credentials)
      return print(result.text)


air = AirlinesHttp().getAirlines('https://api.schiphol.nl/public-flights/airlines?page=1&sort=%2Biata')
