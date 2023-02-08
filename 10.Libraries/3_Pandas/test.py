import numpy as np
import pandas as pd

data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df = pd.DataFrame(data)
print(df["grammer"].value_counts())
