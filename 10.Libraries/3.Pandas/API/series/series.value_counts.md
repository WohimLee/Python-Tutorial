


>示例 9：统计 grammer 列中每种编程语言出现的次数
```python 
import numpy as np
import pandas as pd
data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df1 = pd.DataFrame(data)
print(df1["grammer"].value_counts())
```