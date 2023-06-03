&emsp;
# df.loc
Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：

>示例
```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 注意：返回结果其实就是一个 Pandas Series 数据
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
```


>示例
```python
import pandas as pd
# 也可以返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行和第二行
print(df.loc[[0, 1]])
```



>示例：使用 loc 属性返回指定索引对应到某一行
```py
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# 指定索引
print(df.loc["day2"])
```


>示例：提取含有字符串"Python" 的行
```python
data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df1 = pd.DataFrame(data)
df2 = df1[df1.loc[:,"grammer"]=="Python"]
df3 = df1[df1["grammer"] == "Python"]
print(df2)
print(df3)
```


>示例：提取 score 列中值大于 3 的行

```py
import numpy as np
import pandas as pd
data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df1 = pd.DataFrame(data)
df2 = df1[df1.loc[:,"score"] > 3]
df3 = df1[(df1["score"]>3) & (df1["score"]<7)]
print(df2)
print(df3)
```


>示例：提取 score 列值大于3小于7的行
```py
import numpy as np
import pandas as pd

data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df1 = pd.DataFrame(data)
df2 = df1[df1.loc[:,"score"] > 3]
df3 = df2[df1[df1.loc[:,"score"] > 3].loc[:,"score"] < 7]
df4 = df1[(df1["score"]>3) & (df1["score"]<7)]
print(df2)
print(df3)
print(df4)
```
