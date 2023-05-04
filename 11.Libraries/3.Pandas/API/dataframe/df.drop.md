&emsp;
# df.drop



>df.drop
- 丢掉某行/列
- df.drop('columns',axis=1,inplace='True')
  - inplace: True 改变原始数据; False 不改变原始数据



>示例 ：删除行、列
```py
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(9).reshape((3, 3)),index=['a', 'c', 'd'])
data = frame.drop(['a'])
print(data)
print("----------------------")
data = frame.drop(1, axis=1)
print(data)
```
