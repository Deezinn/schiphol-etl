import pandas as pd
import json
class Transform:
   def __init__(self):
      pass

   def transformToDataframe(self,contents):
      aircraft = contents['aircraftTypes']
      df = pd.DataFrame(aircraft)
      print(df)



