&emsp;
# df.to_csv
- CSV（Comma-Separated Values，逗号分隔值，分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）
- CSV 是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用



>to_csv
- 将 DataFrame 存储为 csv 文件：

>示例
```python
import pandas as pd
   
# 三个字段 name, site, age
nme = ["Google", "Apple", "Taobao", "Wiki"]
st = ["www.google.com", "www.apple.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
   
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv('site.csv')
```

执行成功后，我们打开 site.csv 文件，显示结果如下：

