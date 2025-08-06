import pandas as pd
import json
class Transform:
   def __init__(self):
      pass

   def transformToDataframe(self,contents):
      aircraft = contents['airlines']
      df = pd.DataFrame(aircraft)
      print(df)



