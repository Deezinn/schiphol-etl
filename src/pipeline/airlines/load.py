import pandas as pd


def save_in_csv(dataframe):
   dataframe.to_csv('src/data/airlines.csv')
   return dataframe

