&emsp;
# 函数
- 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

- 函数能提高应用的模块性，和代码的重复利用率。

&emsp;
# 1 定义一个函数
- 你可以定义一个由自己想要功能的函数，以下是简单的规则：

    - 函数用 `def` 关键词定义，后接函数标识符名称和圆括号 ()
    - 圆括号内可以设置参数
    - 函数体内通常会有一些注释说明参数、返回值。
    - 函数内容以冒号 : 起始，并且缩进。
    - return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。


>语法

- Python 定义函数使用 def 关键字，一般格式如下：
```python
def 函数名（参数列表）:
    函数体
```
默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。

>示例
```python
# 以下 3 种形式等价
def hello() :
    print("Hello World!")

def hello() :
    print("Hello World!")
    return 

def hello() :
    print("Hello World!")
    return None

hello()

def max(a, b):
    if a > b:
        return a
    else:
        return b
 
a = 4
b = 5
print(max(a, b))

def area(width, height):
    return width * height
 
def print_welcome(name):
    print("Welcome", name)
 
print_welcome("aaaa")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))
```

&emsp;
# 2 函数调用
- 定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
>示例
```python
# 定义函数
def printme( str ):
   # 打印任何传入的字符串
   print (str)
   return
 
# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
```

&emsp;
# 3 参数传递
- 在 python 中，类型属于对象，变量是没有类型的

>示例
```python
a = [1,2,3]
a = "xxxxx"
```

- [1,2,3] 是 List 类型，"xxxxx" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

&emsp;
## 3.1 mutable与immutable对象
>python的变量

- 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

- 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。

- 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

>python 函数的参数传递：

- 不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。

- 可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

&emsp;
## 3.2 python 传不可变对象实例
通过 id() 函数来查看内存地址变化：

>示例
```python
def change(a):
    print(id(a))   # 指向的是同一个对象
    a=10
    print(id(a))   # 一个新对象
 
a=1
print(id(a))
change(a)
```

可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。

&emsp;
## 3.3 传可变对象实例
可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。

>示例
```python
# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist)
```

&emsp;
# 4 参数
以下是调用函数时可使用的正式参数类型：

- 必需参数
- 关键字参数
- 默认参数
- *args和**kwargs

&emsp;
## 4.1 必需参数
必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

调用 printme() 函数，你必须传入一个参数，不然会出现语法错误：

>示例
```python
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
printme()
'''
以上实例输出结果：

Traceback (most recent call last):
  File "test.py", line 10, in <module>
    printme()
TypeError: printme() missing 1 required positional argument: 'str'
'''
```

&emsp;
## 4.2 关键字参数
- 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

- 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

>示例1
```python
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
#调用printme函数
printme( str = "xxxxxx")
```

>示例2
```python
#可写函数说明
def printinfo( name, age ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="xxx" )
```

&emsp;
## 4.3 默认参数
调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：

>示例
```python
#可写函数说明
def printinfo( name, age = 35 ):
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="xxxx" )
print ("------------------------")
printinfo( name="xxxx" )
```

&emsp;
## 4.4 *args 和 **kwargs
&emsp;
### (1) 打包参数
- `*` 的作用：在函数定义中，收集所有的位置参数到一个新的元组，并将这个元组赋值给变量args

>示例
```python
def f(*args):  # args 只是约定俗称喜欢用，可以自定义
   print(args)

f()  # 输出：()
f(1) # 输出：(1,)
f(1, 2, 3, 4) # 输出：(1, 2, 3, 4)
```
- `**` 的作用：在函数定义中，收集关键字参数传递给一个字典，并将这个字典赋值给变量kwargs

>示例
```python
def f(**kwargs): # kwargs 只是约定俗称喜欢用，可以自定义
   print(kwargs)
f() # 输出：{}
f(a=1, b=2) # 输出：{'a': 1, 'b': 2}
```
&emsp;
### (2) 解包参数
>`*` 的作用

- 在函数调用中，* 能够将元组或者列表解包成不同的参数

```python
def func(a, b, c, d):
   print(a, b, c, d)

args = (1, 2, 3, 4)
func(*args) # 输出：1 2 3 4
args = [1, 2, 3, 4]
func(*args) # 输出：1 2 3 4
```

>`**` 的作用
- 在函数调用中，**会以键/值的形式解包一个字典，使其成为独立的关键字参数

```python
def func(a, b, c, d):
   print(a, b, c, d)

kwargs = {"a": 1, "b": 2, "c": 3, "d": 4}
func(**kwargs) # 输出：1 2 3 4

# 参数解包：将整个list当做参数传给函数
list = [1, 2, 4]
def add_fn(a, b, c):
   return a + b + c

sum = add_fn(*list)
print("参数解包：", sum)
```

声明函数时，参数中星号 * 可以单独出现

>示例
```python
def f(a,b,*,c):
    return a+b+c
```

&emsp;
### (3) 如果单独出现星号 * 后的参数必须用关键字传入。

>示例
```python
def f(a,b,*,c):
    return a+b+c

f(1,2,3)   # 报错
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: f() takes 2 positional arguments but 3 were given
'''
print(f(1,2,c=3)) # 正常
# 输出：6
```

&emsp;
# 5 匿名函数
- python 使用 lambda 来创建匿名函数。

- 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

- lambda 只是一个表达式，函数体比 def 简单很多。
- lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
- lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
- 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法

>lambda 函数语法
```python
lambda [arg1 [,arg2,.....argn]]:expression
```

>示例
```python
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
def func(arg1, arg2):
    return arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", func( 10, 20 ))
```

&emsp;
# 6 return语句
return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，以下实例演示了 return 语句的用法：

>示例
```python
# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)
```
