&emsp;
# Pandas 数据结构 - Series


&emsp;
# 1 创建 Series

>示例 1：创建一个简单的 Series
```python
import pandas as pd

a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)
```


>示例 2：使用 key/value 对象，类似字典来创建 Series
```python
import pandas as pd

sites = {1: "Google", 2: "Baidu", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar)
```

&emsp;
# 2 设置 Series 名称参数

>示例 1
```python
import pandas as pd

sites = {1: "Google", 2: "Baidu", 3: "Wiki"}
myvar = pd.Series(sites, index = [1, 2], name = "Series-TEST")
print(myvar)
```


&emsp;
# 3 索引

>示例 1：查看索引列、数据列
```python
import pandas as pd
list1 = [1, 2, 3]
list2 = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
res1 = pd.Series(list1)
res2 = pd.Series(list2)
print(res1.index)
print(res2.index)
print(res1.values)
print(res2.values)
```

>示例 2：索引
```python
import pandas as pd
a = [1, 2, 3]
myvar = pd.Series(a)
# 如果没有指定索引，索引值就从 0 开始，我们可以根据索引值读取数据
print(myvar[1])
```


>示例 3：指定索引值
```python
import pandas as pd

a = ["Google", "Baidu", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
```

>示例 4：根据索引值读取数据
```py
import pandas as pd

a = ["Google", "Baidu", "Wiki"]
# 
myvar = pd.Series(a, index = ["x", "y", "z"])
#字典的 key 变成了索引值
print(myvar["y"])
```

&emsp;
# 4 切片
- 类似NumPy的切片操作

>示例
```py
import pandas as pd

obj = pd.Series([4,7,-5,3], index=['d','f','b','c'])
print(obj[1:3])
print(obj['b':'c'])
print(obj[1::2])

```

&emsp;
# 5 运算
- NumPy中数组运算，在Series中都可以使用，并且Series进行数组运算的时候，索引与值之间的映射关系不会发生改变

>示例
```python
import pandas as pd

obj1 = pd.Series([4,7,-5,3], index=['d','f','b','c'])
# 更改索引
obj1.index = ['one','two','three','four']
obj2 = pd.Series([195, 73,1], index=['a','b','one'])
print(obj1 + obj2)
```


