&emsp;
# 字典
- 字典是另一种可变容器模型，且可存储任意类型对象。
- 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 
- 键必须是唯一的，但值则不必。
- 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。


>示例
```python
dict0 = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }
```

&emsp;
# 1 访问字典里的值
把相应的键放入到方括号中，如下实例:

>示例
```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
```

如果用字典里没有的键访问数据，会输出错误
>示例
```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
print ("dict['Alice']: ", dict['Alice'])
```
&emsp;
# 2 修改字典
向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

>示例
```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
dict['Age'] = 8               # 更新 Age
dict['School'] = "菜鸟教程"  # 添加信息
 
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

&emsp;
# 3 删除字典元素
- 能删单一的元素也能清空字典，清空只需一项操作。
- 显示删除一个字典用del命令

>示例
```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典
 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# 但这会引发一个异常，因为用执行 del 操作后字典不再存在：
'''
Traceback (most recent call last):
  File "test.py", line 9, in <module>
    print ("dict['Age']: ", dict['Age'])
TypeError: 'type' object is not subscriptable
'''
```

&emsp;
# 4 字典键的特性
&emsp;&emsp;字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

>示例
```python
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print ("dict['Name']: ", dict['Name'])
```
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

>示例
```python
dict = {['Name']: 'Runoob', 'Age': 7}
 
print ("dict['Name']: ", dict['Name'])
# 以上实例输出结果：
'''
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    dict = {['Name']: 'Runoob', 'Age': 7}
TypeError: unhashable type: 'list'
'''
```

&emsp;
# 5 字典内置函数&方法
## 5.1 内置函数
函数|描述
|:--|:--|
len(dict)|计算字典元素个数，即键的总数。	
str(dict)|输出字典，可以打印的字符串表示。	
type(variable)|返回输入的变量类型，如果变量是字典就返回字典类型。	
&emsp;
## 5.2 Python字典包含了以下内置方法

>dict.clear()
- 删除字典内所有元素

>dict.keys()
- 返回字典的所有key

>dict.values()
- 返回字典的所有values

>dict.update(dict2)
- 把字典 dict2 的键值对更新到dict里




>radiansdict.clear()
```python
dict = {'Name': 'Zara', 'Age': 7}
print ("字典长度 : %d" %  len(dict))
dict.clear()
print ("字典删除后长度 : %d" %  len(dict))
```

>key in dict
```python
dict = {'Name': 'Runoob', 'Age': 7}
 
# 检测键 Age 是否存在
if  'Age' in dict:
    print("键 Age 存在")
else :
    print("键 Age 不存在")
 
# 检测键 Sex 是否存在
if  'Sex' in dict:
    print("键 Sex 存在")
else :
    print("键 Sex 不存在")
 
 
# not in
 
# 检测键 Age 是否存在
if  'Age' not in dict:
    print("键 Age 不存在")
else :
    print("键 Age 存在")
```

>pop(key[,default])
```python
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print(pop_obj)
```

>popitem()
```python
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)  
print(site)
```