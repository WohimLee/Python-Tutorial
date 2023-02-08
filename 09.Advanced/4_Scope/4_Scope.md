
&emsp;
# 1 作用域

- 作用域就是一个 Python 程序可以直接访问命名空间的区域。

- 在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。

- Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值。

变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。

&emsp;
## 1.1 四种作用域：

- L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
- E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
- G（Global）：当前脚本的最外层，比如当前模块的全局变量。
- B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。

>示例
```python 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
```


&emsp;
## 1.2 Built-in —— 内建作用域
内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。在Python3.0中，可以使用以下的代码来查看到底预定义了哪些变量

>示例
```python
import builtins
print(dir(builtins))
```

Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：

>示例
```python
if True:
    msg = 'I am from Runoob'
print(msg)
'I am from Runoob'

def test():
    msg_inner = 'I am from Runoob'
print(msg_inner)
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'msg_inner' is not defined'''
```
- 示例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
- 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问

&emsp;
## 1.3 Global —— 全局作用域
定义在函数外的拥有全局作用域，而全局变量可以在整个程序范围内访问。
```python
str1 = "Aaaaaaaa"

def print1():
    print(str1)

def print2():
    # print(str1) # 报错，没有定义
    str1 = "bbbbbb"
    print(str1)

print1()
print2()
```


&emsp;
## 1.4 Local —— 局部作用域
- 定义在函数内部的变量拥有一个局部作用域，局部变量只能在其被声明的函数内部访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

- 当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。
>示例
```python
total = 888 # 这是一个全局变量

def sum( arg1, arg2 ):
    global total # 加 global 关键字，函数作用域内的 total 都是指全局的 total
    print(total)
    total = arg1 + arg2 # total 在这里是局部变量.
    print(total)

sum(10, 20)
print(total)
```


&emsp;
## 1.5 Enclosing —— 闭包

如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：

>示例
```python
def outer():
    num = 10
    def inner():
        # nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
```

