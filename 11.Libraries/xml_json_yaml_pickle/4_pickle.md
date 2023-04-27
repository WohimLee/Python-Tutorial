



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