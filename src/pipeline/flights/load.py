import pandas as pd
from .extract import FlightsHttp

def save_in_csv():
   air = FlightsHttp().getFlights('https://api.schiphol.nl/public-flights/airlines?sort=%2Biata')
   dataframe = pd.DataFrame(air['airlines'])
   dataframe.to_csv('flights.csv', index_label='index')
   return dataframe

print(save_in_csv())
