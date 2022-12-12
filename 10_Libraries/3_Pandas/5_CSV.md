&emsp;
# Pandas CSV 文件
- CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）。

- CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用。

- Pandas 可以很方便的处理 CSV 文件，本文以 nba.csv 为例，你可以下载 nba.csv 或打开 nba.csv 查看。

>示例 1
```python
import pandas as pd
df = pd.read_csv('nba.csv')
print(df.to_string())
```
&emsp;
# 1 函数

&emsp;
## 1.1 to_string() 
- 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。

>示例 1
```py
import pandas as pd

df = pd.read_csv('nba.csv')

print(df)
```

&emsp;
## 1.2 to_csv() 
- 将 DataFrame 存储为 csv 文件：

>示例 1
```python
import pandas as pd
   
# 三个字段 name, site, age
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv('site.csv')
```

执行成功后，我们打开 site.csv 文件，显示结果如下：

&emsp;
# 2 数据处理

&emsp;
## 2.1 head()
- head( n ) 方法用于读取前面的 n 行，如果不填参数 n ，默认返回 5 行。

&emsp;
>示例
```py
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.head())

print(df.head(10))
```

&emsp;
## 2.2 tail()
- tail( n ) 方法用于读取尾部的 n 行，如果不填参数 n ，默认返回 5 行，空行各个字段的值返回 NaN。

>示例 1
```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.tail())
# 读取末尾 10 行
print(df.tail(10))
```

&emsp;
## 2.3 info()
- info() 方法返回表格的一些基本信息

>示例
```python
import pandas as pd

df = pd.read_csv('nba.csv')

print(df.info())
```