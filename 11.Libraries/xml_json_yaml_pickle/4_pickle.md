
&emsp;
# pickle
- python的pickle模块实现了基本的数据序列和反序列化。
  - pickle模块只能在python中使用，python中几乎所有的数据类型（列表，字典，集合，类等）都可以用pickle来序列化，
  - pickle序列化后的数据，可读性差，人一般无法识别。
  - 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
  - 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

基本接口：
```python
pickle.dump(obj, file, [,protocol])
```
有了 pickle 这个对象, 就能对 file 以读取的形式打开:
```python
x = pickle.load(file)
```
注解：
- 从 file 中读取一个字符串，并将它重构为原来的python对象。
- file: 类文件对象，有read()和readline()接口。
- protocol是序列化模式，默认值为0，表示以文本的形式序列化。protocol的值还可以是1或2，表示以二进制的形式序列化。

```python
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('./files/data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1) #  protocal 的值是负数， 使用最高 protocal 对 obj 压缩

output.close()

#实例 2
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('./files/data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
```



Python提供两个模块来实现序列化：
- cPickle 
- pickle

这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢。

- 变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling

- 变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
```py
try:
    import cPickle as pickle
except ImportError:
    import pickle
```

1.将内存对象存取到磁盘
```py
a = dict(a=1, b=2, c=3)
pickle.dumps(a)     # 将对象序列化为str然后存入文件
```

```py
a = dict(a=1, b=2, c=3)
pickle.dump(a, open('a.txt', 'wb')) # 使用dump直接把对象序列化为file-like Object，注意是二进制存储
```
2.从磁盘读取到内存对象

```py
pickle.load(open('a.txt', 'rb'))    #从file-like Object中直接反序列化出对象
```