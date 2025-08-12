import json

import pandas as pd


class SchipholTransform:
   def __init__(self):
      self.__flights = None
      self.__airlines = None
      self.__destinations = None
      self.__aircrafttypes = None

   def loadContentContext(self,contents):
      for content in contents:
         if list(content.keys())[0] == 'flights':
            self.__flights = list(content.values())[0]
         if list(content.keys())[0] == 'airlines':
            self.__airlines = list(content.values())[0]
         if list(content.keys())[0] == 'destinations':
            self.__destinations = list(content.values())[0]
         if list(content.keys())[0] == 'aircrafttypes':
            self.__aircrafttypes = list(content.values())[0]
      return ''

   def printConten(self):
      dataframe1 = pd.DataFrame(self.__flights)
      dataframe2 = pd.DataFrame(self.__airlines)
      dataframe3 = pd.DataFrame(self.__destinations)
      dataframe4 = pd.DataFrame(self.__aircrafttypes)
      print(dataframe1)
