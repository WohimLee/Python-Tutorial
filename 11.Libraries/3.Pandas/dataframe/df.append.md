
&emsp;
# df.append

>示例 ：添加行、列
```py
import pandas as pd
import numpy as np

data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}
df = pd.DataFrame(data)
print(df)

print("---------------------")
new_row = {"grammer":'perl',"score":90}
df = df.append(new_row, ignore_index=True)
print(df)
```