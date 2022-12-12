&emsp;
# 控制语句

&emsp;
# 1 条件语句
Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。

Python 编程中 if 语句用于控制程序的执行，基本形式为：
```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
- 如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
- 如果 "condition_1" 为False，将判断 "condition_2"
- 如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
- 如果 "condition_2" 为False，将执行"statement_block_3"块语句
- 注意：
    - 每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
    - 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
>示例
```python
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
 
### 退出提示
input("点击 enter 键退出")
```


&emsp;
# 2 循环语句
## 2.1 while循环语句
Python 中 while 语句的一般形式：
```python
while 判断条件(condition)：
    执行语句(statements)……
```
>示例
```python
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))
```
&emsp;
## 2.2 while无限循环
我们可以通过设置条件表达式永远不为 false 来实现无限循环，实例如下：

>示例
```python
# var = 1
# while var == 1 :  # 表达式永远为 true
#    num = int(input("输入一个数字  :"))
#    print ("你输入的数字是: ", num)
 
# print ("Good bye!")


var = 1
while var:
    var = int(input("请输入一个数字："))
    print("你输入的数字是：", var)
print('Good bye!')
```

&emsp;
## 2.3 while和else
如果 while 后面的条件语句为 false 时，则执行 else 的语句块。

>语法格式
```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```
expr 条件语句为 true 则执行 statement(s) 语句块，如果为 false，则执行 additional_statement(s)。

>示例
```python
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```

&emsp;
## 2.4 for循环语句
Python for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。

>for循环的一般格式
```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```
>示例
```python
languages = ["C", "C++", "Perl", "Python"] 
for x in languages:
    print (x)
```
如果要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:

>示例
```python
for i in range(5):
    print(i)

for i in range(5,9):
    print(i)

for i in range(0, 10, 3) :
    print(i)

for i in range(-10, -100, -30) :
    print(i)

# 可以结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
```
&emsp;
## 2.5 循环嵌套
>Python for 循环嵌套语法：
```python
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
```
>Python while 循环嵌套语法：
```python
while expression:
   while expression:
      statement(s)
   statement(s)
```

>示例
```python
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " 是素数"
   i = i + 1
 
print("Good bye!")
```



&emsp;
# 4 break语句
- break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

- break语句用在 while 和 for 循环中。

```python
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print ('当前字母 :', letter)

var = 10                    # 第二个实例
while var > 0:              
   print ('当前变量值 :', var)
   var = var -1
   if var == 5:   # 当变量 var 等于 5 时退出循环
      break

print ("Good bye!")
```


&emsp;
# 5 continue语句
- continue 语句跳出本次循环，而break跳出整个循环。

- continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

- continue语句用在while和for循环中。
```python
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('当前变量值 :', var)
print("Good bye!")
```

&emsp;
# 6 pass语句
- pass 是空语句，是为了保持程序结构的完整性。

- pass 不做任何事情，一般用做占位语句。

>示例
```python
for letter in 'Python':
   if letter == 'h':
      pass
      print ('这是 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
```