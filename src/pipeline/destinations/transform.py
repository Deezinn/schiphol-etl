import json

import pandas as pd


class Transform:
    def __init__(self):
        pass

    def transformToDataframe(self, contents):
        aircraft = contents["destinations"]
        df = pd.DataFrame(aircraft)
        return {"dataframe": df,
            "tag": "destinations"}
