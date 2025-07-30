import pandas as pd
from .extract import AirlinesHttp

def save_in_csv():
   air = AirlinesHttp().getAirlines('https://api.schiphol.nl/public-flights/airlines?sort=%2Biata')
   dataframe = pd.DataFrame(air['airlines'])
   dataframe.to_csv('src/data/airlines.csv', index_label='index')
   return dataframe

save_in_csv()
