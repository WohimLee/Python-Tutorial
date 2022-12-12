&emsp;
# Number

以下实例在变量赋值时 Number 对象将被创建：

var1 = 1
var2 = 10
使用del语句可以删除一些数字对象的引用。

del语句的语法是：
```python
del var1[,var2[,var3[....,varN]]]
```
>示例
```python
del var
del var_a, var_b
```
Python 支持三种不同的数值类型：

- 整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。

- 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）

- 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

我们可以使用十六进制和八进制来代表整数：
```python
number = 0xA0F    # 十六进制
number = 0o37     # 八进制
number = 0b100101 # 二进制
```

&emsp;
# 1 Python 数字类型转换
数据类型的转换，只需要将数据类型作为函数名即可。
```python
int(x)        # 将x转换为一个整数。
float(x)      # 将x转换到一个浮点数。
complex(x)    # 将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y) # 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
```

>示例
```python
a = 1.0
```
&emsp;
# 2 数学函数
函数	|返回值 ( 描述 )|
|:--|:--|
abs(x)	|返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	|返回数字的上入整数，如math.ceil(4.1) 返回 5
floor(x)	|返回数字的下舍整数，如math.floor(4.9)返回 4
exp(x)	|返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
log(x)	|如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	|返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	|返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	|返回给定参数的最小值，参数可以为序列。
pow(x, y)	|x**y 运算后的值。
round(x [,n])	|返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数，其实准确的说是保留值将保留到离上一位更近的一端。
sqrt(x)	|返回数字x的平方根。

>abs()示例
```python
print ("abs(-40) : ", abs(-40))
print ("abs(100.10) : ", abs(100.10))
```

>ceil()示例
```python
import math   # 导入 math 模块

print ("math.ceil(-45.17) : ", math.ceil(-45.17))
print ("math.ceil(100.12) : ", math.ceil(100.12))
print ("math.ceil(100.72) : ", math.ceil(100.72))
```
>floor()示例
```python
import math   # 导入 math 模块

print ("math.floor(-45.17) : ", math.floor(-45.17))
print ("math.floor(100.12) : ", math.floor(100.12))
print ("math.floor(100.72) : ", math.floor(100.72))
```

>exp()示例
```python
import math   # 导入 math 模块

print ("math.exp(-45.17) : ", math.exp(-45.17))
print ("math.exp(100.12) : ", math.exp(100.12))
print ("math.exp(100.72) : ", math.exp(100.72))
```

>log()示例
```python
import math   # 导入 math 模块

print ("math.log(100.12) : ", math.log(100.12))
print ("math.log(100.72) : ", math.log(100.72))
```

>log10()示例
```python
import math   # 导入 math 模块

print ("math.log10(100.12) : ", math.log10(100.12))
print ("math.log10(100.72) : ", math.log10(100.72))
print ("math.log10(119) : ", math.log10(119))
```

>max()示例
```python
print ("max(80, 100, 1000) : ", max(80, 100, 1000))
```

>min()示例
```python
print ("min(-80, -20, -10) : ", min(-80, -20, -10))
```

>pow()示例
```python
import math   # 导入 math 模块

print ("math.pow(100, 2) : ", math.pow(100, 2))
# 使用内置，查看输出结果区别
print ("pow(100, 2) : ", pow(100, 2))
print ("math.pow(100, -2) : ", math.pow(100, -2))
print ("math.pow(2, 4) : ", math.pow(2, 4))
print ("math.pow(3, 0) : ", math.pow(3, 0))
```

>round()示例
```python
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print ("round(-100.000056, 3) : ", round(-100.000056, 3))
```

>sqrt()示例
```python
import math   # 导入 math 模块
 
print ("math.sqrt(100) : ", math.sqrt(100))
print ("math.sqrt(7) : ", math.sqrt(7))
print ("math.sqrt(math.pi) : ", math.sqrt(math.pi))
```



&emsp;
# 3 随机数函数

函数	|描述
|:--|:--|
randrange ([start,] stop [,step])	|从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	|随机生成下一个实数，它在[0,1)范围内。
seed([x])	|改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	|将序列的所有元素随机排序

>randrange()示例
```python
import random
# 从 1-100 中选取一个奇数
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# 从 0-99 选取一个随机数
print ("randrange(100) : ", random.randrange(100))
```

>random()示例
```python
import random
# 第一个随机数
print ("random() : ", random.random())
# 第二个随机数
print ("random() : ", random.random())
```

>seed(x)示例
```python
import random

random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())
```

>shuffle()示例
```python
import random
list = [20, 16, 10, 5]
random.shuffle(list)
print ("随机排序列表 : ",  list)
random.shuffle(list)
print ("随机排序列表 : ",  list)
```



&emsp;
# 4 三角函数

函数	|描述|
|:--|:--|
sin(x)	|返回的x弧度的正弦值。
cos(x)	|返回x的弧度的余弦值。
tan(x)	|返回x弧度的正切值。
degrees(x)	|将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	|将角度转换为弧度

>sin()示例
```python
import math
print ("sin(math.pi) : ",  math.sin(math.pi))
print ("sin(math.pi/2) : ",  math.sin(math.pi/2))
```


>cos()示例
```python
import math
print ("cos(math.pi) : ",  math.cos(math.pi))
print ("cos(2*math.pi) : ",  math.cos(2*math.pi))
```


>tan()示例
```python
import math
print ("tan(math.pi) : ",  math.tan(math.pi))
print ("tan(math.pi/2) : ",  math.tan(math.pi/2))
print ("tan(math.pi/4) : ",  math.tan(math.pi/4))
```


>degree()示例
```python
import math
print ("degrees(math.pi) : ",  math.degrees(math.pi))
print ("degrees(math.pi/2) : ",  math.degrees(math.pi/2))
print ("degrees(math.pi/4) : ",  math.degrees(math.pi/4))
```


>radians()示例
```python
import math

print ("radians(90) : ",  math.radians(90))     # 1 弧度等于大概 57.3°
print ("radians(45) : ",  math.radians(45))
print ("radians(30) : ",  math.radians(30))
print ("radians(180) : ",  math.radians(180))  # 180 度的弧度为 π

print("180 / pi : ", end ="")
print (math.radians(180 / math.pi))
```


&emsp;
# 5 数学常量
常量|	描述
|:--|:--|
pi	|数学常量 pi（圆周率，一般以π来表示）
e	|数学常量 e，e即自然常数（自然常数）