&emsp;
# Python 基础语法
# 1 第一个 Python 程序
## 1.1 交互式编程
只需要终端中输入 python 命令就可以启动交互式编程，提示窗口如下：
```
$ python
Python 2.7.17 (default, Feb 27 2021, 15:10:58) 
[GCC 7.5.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

在 python 提示符中输入以下文本信息，然后按 Enter 键查看运行效果：
```python
>>> print("Hello, Python!")
```

&emsp;
## 1.2 脚本式编程
- 代码写在 .py 文件中，然后在终端执行 .py 文件，就是脚本式编程

>test.py
```python
print("Hello, Python!")
```

>在终端中执行命令
```
$ python test.py
```


&emsp;
# 2 Python 命名规则
- 在 Python 里，标识符由 `字母、数字、下划线` 组成
- 在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头
- Python 中的标识符是 `区分大小写` 的
- 以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入
- 以双下划线开头的 \_\_foo 代表类的 `私有成员`，以双下划线开头和结尾的 \_\_foo__ 代表 Python 的特殊方法，如 \_\_init__() 代表类的构造函数。

Python 可以同一行显示多条语句，方法是用分号 `;` 分开，如：
```
print('hello', end=" ");print('kiwi');
```

&emsp;
# 3 Python 保留字符
下面的列表显示了在 Python 中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。所有 Python 的关键字只包含小写字母。

<div align=center>
    <image src="imgs/1.png" width=800>
</div>


&emsp;
# 4 行和缩进
Python 严格控制缩进格式，每个缩进层要使用相同的缩进，如： `tab` 或 `两个空格` 或 `四个空格` , 切记不能混用，建议缩进统一使用 tab，不使用 space，否则会容易出错

>示例
```python
if True:
    print ("True")
else:
    print ("False")
```
以下代码将会执行错误：
>实例
```python
if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
  print ("False")
```
- 报错
    ```
    IndentationError: unindent does not match any outer indentation level
    ```
    - 错误表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。


&emsp;
# 5 续行符
Python 使用斜杠 `\` 作为续行符

>示例
```python
total = item_one + \
        item_two + \
        item_three

#语句中包含 [], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

&emsp;
# 6 Python 引号
- 单引号( ' )：单引号中可以包含双引号
- 双引号( " )：双引号中可以包含单引号
- 三引号( ''' 或 """ )：通常用来写大段注释

>示例
```python
example1 = 
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
```

&emsp;
# 7 Python注释
## 7.1 单行注释采用 # 开头。

>示例
```python
# 注释
print ("Hello, Python!")  # 注释
输出结果：

Hello, Python!
注释可以在语句或表达式行末：

name = "Madisetti" # 这是一个注释
```
&emsp;
## 7.2 多行注释使用三个单引号(''')或三个双引号(""")。

>示例
```python
'''
多行注释，使用单引号。
多行注释，使用单引号。
多行注释，使用单引号。
'''

"""
多行注释，使用双引号。
多行注释，使用双引号。
多行注释，使用双引号。
"""
```

&emsp;
## 7.3 特殊注释
Python中有两句特殊的注释，通常是在 Python 版本不确定或者想手动指定 Python 版本的时候使用
```python
#!/usr/bin/python3
# -- coding=utf-8 -- 
```
- 第一行用来指定 Python 解析器的路径
- 第二行用来指定编码格式

&emsp;
# 8 基本的输入与输出
```python
a = input("请输入任意内容...")
print(a)
```
