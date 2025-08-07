import pandas as pd


def save_in_csv(dataframe):
   dataframe.to_csv('src/data/destinations.csv')
   return dataframe

