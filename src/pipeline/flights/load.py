import pandas as pd


def save_in_csv(dataframe):
   dataframe.to_csv('src/data/flights.csv')
   return dataframe

