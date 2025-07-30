import pandas as pd
from .extract import FlightsHttp

def save_in_csv():
   air = FlightsHttp().getFlights('https://api.schiphol.nl/public-flights/flights?sort=%2BscheduleTime')
   dataframe = pd.DataFrame(air['airlines'])
   dataframe.to_csv('flights.csv', index_label='index')
   return dataframe

print(save_in_csv())


