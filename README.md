# Python 教程大纲（由浅入深）

## 第一阶段：基础入门
1. Python 简介与环境配置
   - Python 能做什么
   - 安装 Python 与常用 IDE（VSCode/PyCharm）
   - 编写第一个程序：print("Hello, world!")
2. 基本数据类型与变量
   - 数字（int, float）
   - 字符串（str）及基本操作
   - 布尔值（bool）
   - 变量命名与赋值
3. 运算符
   - 算术运算符：+ - * / // % **
   - 比较运算符：== != > < >= <=
   - 逻辑运算符：and or not
   - 赋值运算符：= += -= ...
4. 输入与输出
   - input() 获取用户输入
   - print() 输出信息
5. 流程控制
   - 条件语句：if / elif / else
   - 缩进规范
6. 循环语句
   - while 循环
   - for 循环与 range()
   - break 和 continue

## 第二阶段：数据结构与函数
1. 列表（list）
   - 创建、访问、切片、遍历
   - 常用方法：append(), pop(), sort()
2. 元组（tuple）与字符串进阶
   - 不可变序列
   - 解包、嵌套
   - 字符串格式化：f-string, % , format()
3. 字典（dict）
   - 创建、访问、增删改查
   - 遍历与嵌套字典
4. 集合（set）
   - 特点与常用操作
   - 并、交、差、子集判断
5. 函数基础
   - 定义与调用
   - 形参、实参、默认参数、关键字参数
   - return 返回值

## 第三阶段：进阶语法与代码组织
1. 作用域与命名空间
   - 局部变量与全局变量
   - global 与 nonlocal
2. 异常处理
   - try / except / finally / else
   - raise, assert
3. 模块与包
   - import / from ... import ...
   - __name__ == "__main__" 的意义
   - pip 安装第三方模块
4. 文件操作
   - 读写文本文件：open, read, write
   - 上下文管理器：with open()
   - 文件路径与编码
5. 函数进阶
   - 匿名函数 lambda
   - 高阶函数：map, filter, reduce
   - 列表/字典推导式

## 第四阶段：面向对象编程（OOP）
1. 类与对象
   - class 定义与实例化
   - 构造方法 __init__
   - 成员变量与方法
2. 封装、继承、多态
   - 私有属性与方法：_name, __name
   - 子类继承与方法重写
   - super() 的使用
3. 类的特殊方法
   - __str__, __repr__, __len__, __eq__
   - 运算符重载

## 第五阶段：常用库与实用技巧
1. 标准库简介
   - math, random, datetime, os, sys
2. 实用工具
   - 迭代器与生成器
   - 装饰器基础
   - zip, enumerate, any, all
3. 正则表达式（re 模块）
   - 匹配模式
   - 查找、替换、分组提取

## 第六阶段：项目实战与扩展
1. 命令行工具项目
2. 数据处理（csv, pandas 简介）
3. GUI 编程（tkinter）
4. 网络爬虫（requests, BeautifulSoup）
5. 期末综合项目

---

本教程适合零基础到进阶学习者，建议按顺序学习，每一阶段都配有实例与练习题，帮助你逐步掌握 Python 编程。

# 🐍 Python Tutorial (From Beginner to Advanced)

Welcome to the complete Python tutorial series. This course is designed to take you from zero to practical Python programming, step by step.

---

## 📚 Course Outline

| # | Chapter | Description |
|---|---------|-------------|
| 01 | [Introduction and Setup](./01-introduction-and-setup/) | Install Python, run your first script |
| 02 | [Basic Data Types and Variables](./02-basic-data-types-and-variables/) | Numbers, strings, booleans, and variables |
| 03 | [Operators and Expressions](./03-operators-and-expressions/) | Arithmetic, comparison, logic |
| 04 | [Control Flow: If-Else](./04-control-flow-if-else/) | Making decisions with if/elif/else |
| 05 | [Loops and Iteration](./05-loops-and-iteration/) | `for`, `while`, `break`, `continue` |
| 06 | [Lists and Basic Operations](./06-lists-and-basic-operations/) | Lists, indexing, slicing |
| 07 | [Tuples and Strings](./07-tuples-and-strings/) | Immutable sequences and string formatting |
| 08 | [Dictionaries and Nested Structures](./08-dictionaries-and-nested-structures/) | Key-value storage and loops |
| 09 | [Sets and Set Operations](./09-sets-and-set-operations/) | Unique elements and set math |
| 10 | [Functions and Parameters](./10-functions-and-parameters/) | Defining, calling, returning values |
| 11 | [Variable Scope and Namespace](./11-variable-scope-and-namespace/) | Local vs global, `global`, `nonlocal` |
| 12 | [Exception Handling](./12-exception-handling/) | `try`, `except`, `raise`, `assert` |
| 13 | [Modules and Packages](./13-modules-and-packages/) | `import`, pip, main function |
| 14 | [File Operations](./14-file-operations/) | Reading and writing files |
| 15 | [Advanced Functions](./15-advanced-functions-and-comprehensions/) | `lambda`, `map`, list comprehension |
| 16 | [Classes and Objects](./16-classes-and-objects/) | Basic OOP structure |
| 17 | [OOP: Encapsulation & Inheritance](./17-oop-encapsulation-inheritance/) | Inheritance, access control |
| 18 | [Magic Methods and Overloading](./18-magic-methods-and-operator-overloading/) | `__str__`, `__eq__`, operator overloading |
| 19 | [Standard Library Overview](./19-standard-library-overview/) | `math`, `random`, `datetime`, `os` |
| 20 | [Practical Python Tools](./20-practical-python-tools/) | Iterators, `zip`, `enumerate` |
| 21 | [Regular Expressions](./21-regular-expressions/) | Pattern matching and text search |
| 22 | [CLI Tools Project](./22-cli-tools-project/) | Build command-line apps |
| 23 | [Data Handling with CSV and Pandas](./23-data-handling-with-csv-and-pandas/) | `csv`, intro to `pandas` |
| 24 | [GUI Programming with Tkinter](./24-gui-programming-with-tkinter/) | Create simple desktop apps |
| 25 | [Web Scraping with Python](./25-web-scraping-with-python/) | Use `requests`, `BeautifulSoup` |
| 26 | [Final Projects](./26-final-projects/) | Capstone mini-projects |

---

