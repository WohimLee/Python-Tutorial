&emsp;
# series.mean



>示例 7：计算 score 列平均值
```python
import numpy as np
import pandas as pd

data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df1 = pd.DataFrame(data)
df2 = df1.loc[:,"score"].mean()
df3 = df1["score"].mean()
print(df2)
print(df3)
```




&emsp;
# series.var



&emsp;
# series.std