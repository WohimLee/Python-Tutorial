&emsp;
# 集合（set）
是一个无序的不重复元素序列。

可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

>创建格式
```python
parame = {value01,value02,...}
# 或者
set(value)
```

```python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                 # 这里演示的是去重功能
# 输出：{'orange', 'banana', 'pear', 'apple'}

print('orange' in basket )    # 快速判断元素是否在集合内
# 输出：True
print('crabgrass' in basket)
# 输出：False

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)                                 
# 输出：{'a', 'r', 'b', 'c', 'd'}
print(a - b)               # 集合a中包含而集合b中不包含的元素
# 输出：{'r', 'd', 'b'}
print(a | b)               # 集合a或b中包含的所有元素
# 输出：{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)               # 集合a和b中都包含了的元素
# 输出：{'a', 'c'}
print(a ^ b)               # 不同时包含于a和b的元素
# 输出：{'r', 'd', 'b', 'm', 'z', 'l'}
```

类似列表推导式，同样集合支持集合推导式(Set comprehension):

>示例
```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
# 输出：{'r', 'd'}
```

&emsp;
# 1 集合的基本操作

&emsp;
## 1.1 添加元素
>语法格式
```python
s.add( x )
```

- 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

>示例
```python
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
# 输出：{'Taobao', 'Facebook', 'Google', 'Runoob'}
```
还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：
```python
s.update( x ) # x 可以有多个，用逗号分开。
```
>示例
```python
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)
# 输出：{1, 3, 'Google', 'Taobao', 'Runoob'}
thisset.update([1,4],[5,6])  
print(thisset)
# 输出：{1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
```

&emsp;
## 1.2 移除元素
>语法格式
```
s.remove( x )
```
- 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

>示例
```python
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)
# 输出：{'Google', 'Runoob'}
thisset.remove("Facebook")   # 不存在会发生错误
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Facebook'
'''
```

此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：
```python
s.discard( x )
```

>示例
```python
thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)
# 输出：{'Taobao', 'Google', 'Runoob'}
```

我们也可以设置随机删除集合中的一个元素，语法格式如下：
```python
s.pop() 
```

>示例
```python
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
print(x)
```

set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

&emsp;
## 1.3 计算集合元素个数
>语法格式
```python
len(s)
```
- 计算集合 s 元素个数。

>示例
```python
thisset = set(("Google", "Runoob", "Taobao"))
len(thisset)
```

&emsp;
## 1.4 清空集合
>语法格式
```python
s.clear()
```
清空集合 s。

>示例
```python
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset)
set()
```

&emsp;
## 1.5 判断元素是否在集合中存在
>语法格式
```python
x in s
```
- 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。

>示例
```python
thisset = set(("Google", "Runoob", "Taobao"))
print("Runoob" in thisset)
# 输出：True
print("Facebook" in thisset)
# 输出：False
```

