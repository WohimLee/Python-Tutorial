&emsp;
# pd.Series



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

>示例3 设置 Series 名称参数

```python
import pandas as pd

sites = {1: "Google", 2: "Baidu", 3: "Wiki"}
myvar = pd.Series(sites, index = [1, 2], name = "Series-TEST")
print(myvar)
```


>示例 3：指定索引值
```python
import pandas as pd

a = ["Google", "Baidu", "Wiki"]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
```