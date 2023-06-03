&emsp;
# pd.DataFrame



>示例 2
```py
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
data[data < 5] =0
print(data)
```



>示例

```python
import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# 查找列，通过key查找
# print(data['two'])
# print(data['three', 'one', 'two'])

# # 查找行，切片
# print(data[:2])

# 查找行，布尔型数组选取
print(t := (data['three'] > 5))
print(data[t])
```


>示例 3：指定索引值
```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
```