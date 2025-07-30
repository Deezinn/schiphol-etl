import pandas as pd
from .extract import FlightsHttp

def save_in_csv():
   air = FlightsHttp().getFlights('https://api.schiphol.nl/public-flights/flights?sort=%2BscheduleTime')
   dataframe = pd.DataFrame(air['flights'])
   dataframe.to_csv('src/data/flights.csv', index_label='index')
   return dataframe

save_in_csv()


