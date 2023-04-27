&emsp;
# Pandas 数据结构 - DataFrame
- DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。
- DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共同用一个索引）。
- DataFrame 是一个二维的数组结构，类似二维数组。



>DataFrame 构造方法
```python
pandas.DataFrame( data, index, columns, dtype, copy)
```
- 参数说明：

    - data：一组数据(ndarray、series, map, lists, dict 等类型)。
    - index：索引值，或者可以称为行标签。
    - columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
    - dtype：数据类型。
    - copy：拷贝数据，默认为 False。

&emsp;
# 1 创建DataFrame
&emsp;
>示例 1：使用列表创建
```python
import pandas as pd

data = [['Google',10],['Baidu',12],['Wiki',13]]
# 指定列
df = pd.DataFrame(data,columns=['Site','Age'],dtype=float)
print(df)
```

&emsp;
>示例 2：使用 ndarrays 创建
```python
# 使用 ndarrays 创建，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。

import pandas as pd

data = {'Site':['Google', 'Baidu', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print (df)
```


&emsp;
>示例 3：使用字典创建
```python
# 还可以使用字典（key/value），其中字典的 key 为列名
import pandas as pd

data = {
'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

df = pd.DataFrame(data)
# 没有对应的部分数据为 NaN
print(df)


data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df = pd.DataFrame(data)
print(df)
```

&emsp;
# 2 基础操作
&emsp;
>示例 1
```py
import pandas as pd
data = {
'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002, 2003],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}

df = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three',
'four', 'five','six'])
# 列在数据中找不到，就会在结果中产生缺失值
print(df)
# 查看属性
print(df.columns)
```
&emsp;
## 2.1 增


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


&emsp;
## 2.2 删
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



&emsp;
## 2.3 改

>示例1 ：reindex修改行、列

```py
import pandas as pd
import numpy as np

frame1 = pd.DataFrame(np.arange(9).reshape((3, 3)),index=['a', 'c', 'd'])
frame2 = frame1.reindex(['a', 'd','c'])
frame3 = frame1.reindex([2,1,0,3],axis=1)
print(frame2)
print(frame3)
```

>示例 2
```py
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
data[data < 5] =0
print(data)
```

>示例 3：填充 NaN 值
```python
data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}
df = pd.DataFrame(data)
df.fillna(0,inplace=True)
print(df,'\n')
```

&emsp;
## 2.4 查

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



&emsp;
# 2 索引
Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1，以此类推：

&emsp;
>示例 1
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

>示例 2：
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

>示例 4：使用 loc 属性返回指定索引对应到某一行
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

>示例 5：提取含有字符串"Python" 的行
```python
data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df1 = pd.DataFrame(data)
df2 = df1[df1.loc[:,"grammer"]=="Python"]
df3 = df1[df1["grammer"] == "Python"]
print(df2)
print(df3)
```

>示例 6：提取 score 列中值大于3的行

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

>示例 8：提取 score 列值大于3小于7的行
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

>示例 9：统计 grammer 列中每种编程语言出现的次数
```python 
import numpy as np
import pandas as pd
data = {"grammer":["Python","C","Java","GO",np.nan,"SQL","PHP","Python"],
       "score":[1,2,np.nan,4,5,6,7,10]}

df1 = pd.DataFrame(data)
print(df1["grammer"].value_counts())
```