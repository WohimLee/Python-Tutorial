&emsp;
# JSON


# JSON函数区别
>序列化
- 变量从内存中变成可存储或传输的过程称之为序列化序列化是将对象状态转化为可保存或可传输格式的过程
- dump 和 dumps 都实现了序列化
&emsp;
>反序列化
- 变量内容从序列化的对象重新读到内存里称之为反序列化，反序列化是流转换为对象
- load 和 loads 都实现反序列化


&emsp;
## 1 load 和 loads （反序列化）
>load
- 针对文件句柄，将json格式的字符转换为dict，从文件中读取 (将string转换为dict)
```py
a_json = json.load(open('demo.json','r'))
```

>loads
- 针对内存对象，将string转换为dict (将string转换为dict)
```py
a = json.loads('{'a':'1111','b':'2222'}')
```

&emsp;
## 2 dump 和 dumps（序列化）

>dump
- 将dict类型转换为json字符串格式，写入到文件 （易存储）
```py
a_dict = {'a':'1111','b':'2222'}
json.dump(a_dict, open('demo.json', 'w')
```
>dumps
- 将dict转换为string (易传输)
```py
a_dict = {'a':'1111','b':'2222'}
a_str = json.dumps(a_dict)
```
## 3 总结
- 根据序列化和反序列的特性
    - loads： 是将string转换为dict
    - load： 是将里json格式字符串转化为dict，读取文件
    - dumps： 是将dict转换为string
    - dump： 是将dict类型转换为json格式字符串，存入文件

## JSON进阶
### 序列化
```py
# 使用class对象的__dict__方法
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
import json
s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))
```

### 反序列化
```py
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
```
### 实用案例
```py
def load_json(path):
    with open(path) as f:
        # data = f.read()
        data = json.load(f)
    return data
```