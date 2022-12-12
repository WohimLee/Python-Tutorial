&emsp;
# String

创建字符串很简单，只要为变量分配一个值即可。
>示例
```
var1 = 'Hello World!'
var2 = "Runoob"
```

&emsp;
# 1 访问字符串中的值
- Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。

- Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法
- 索引值以 0 为开始值，-1 为从末尾的开始位置。

>格式如下：
```python
变量[头下标:尾下标]
```

>示例
```python
var1 = 'Hello World!'
var2 = "Runoob"
 
print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])
```

&emsp;
# 2 字符串拼接
你可以截取字符串的一部分并与其他字段拼接

>示例
```python
var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!')
```

&emsp;
# 3 Python转义字符
在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。


转义字符|	描述
|:--|:--|
\ \(在行尾时)	|续行符	
\\\	|反斜杠符号	
\\'	|单引号	
\\"	|双引号	
\n	|换行	
\r	|回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。	



操作符	|描述	|实例
|:--|:--|:---|
\+	|字符串连接	|a + b 输出结果： HelloPython
\*	|重复输出字符串	|a*2 输出结果：HelloHello
[]	|通过索引获取字符串中字符	|a[1] 输出结果 e
[ : ]	|截取字符串中的一部分，遵循左闭右开原则，str[0:2] 是不包含第 3 个字符的。|	a[1:4] 输出结果 ell
in	|成员运算符 - 如果字符串中包含给定的字符返回 True	|'H' in a 输出结果 True
not in	|成员运算符 - 如果字符串中不包含给定的字符返回 True|	'M' not in a 输出结果 True
r/R	|原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。|	print( r'\n' ) print( R'\n' )
%	|格式字符串	


>示例
```python
a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')
```

&emsp;
# 4 Python 字符串格式化
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

在 Python 中，字符串格式化使用与 C 中 printf 函数一样的语法。

>示例
```python
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
```
>python字符串格式化符号

符   号	|描述
|:--|:--|
%c	 |格式化字符及其ASCII码
%s	 |格式化字符串
%d	 |格式化整数
%u	 |格式化无符号整型
%o	 |格式化无符号八进制数
%x	 |格式化无符号十六进制数
%X	 |格式化无符号十六进制数（大写）
%f	 |格式化浮点数字，可指定小数点后的精度
%e	 |用科学计数法格式化浮点数
%E	 |作用同%e，用科学计数法格式化浮点数
%g	 |%f和%e的简写
%G	 |%f 和 %E 的简写
%p	 |用十六进制数格式化变量的地址

>格式化数字

![](imgs/numbers.png)

>格式化操作符辅助指令

符号	|功能
|:--|:--|
\*	|定义宽度或者小数点精度
\-	|用做左对齐
\+	|在正数前面显示加号( + )
%	|'%%'输出一个单一的'%'

>示例
```python
a = 3.1415926
b = -4.55583473453
print(f"{a:.2f}")
print(f"{a:+.3f}")
print(f"{b:+.3f}")
print(f"{a:.0f}")
c = 5
print(f"{c:0>2d}")
print(f"{c:x<4d}")
d = 10000000
print(f"{d:,}")
print(f"{d:.2e}")
e = 0.25
print(f"{e:.2%}")
```

&emsp;
# 5 Python字符串输出的几种方法
## 5.1 %占位符  
```python
print ('我叫%s, 身高%scm'  % (name,height))   # 传入的值为元组，依次填充
```


## 5.2 format   


```python
# 顺序填坑：{} 占位符
print('姓名是 {}，年龄是 {}'.format('Tom',20))
print('姓名是 {1}，年龄是 {0}'.format('Tom',20))
print('姓名是 {0}，年龄是 {0}'.format('Tom',20))

# 变量填坑
print('姓名是:{name}，年龄是:{age}'.format(name='Tom',age=20))

# 变量中使用
name = Ada
age = 20
print('Name is {name},age is {age}'.format(name=name,age=age))
```


## 5.3. 格式化 f/F（最最最常用！）

```python
name = 'Tom'
age = 20
print(f'姓名是：{name},年龄是：{age}')

w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')

print(f'{1+2}')         # 使用表达式

# 在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果
x = 1
print(f'{x+1=}') 
```



&emsp;
# 6 Python三引号
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下

>示例
```python
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
```



&emsp;
# 7 Python 的字符串内建函数
Python 的字符串常用内建函数如下：

方法|	描述|
|:--|:--|
bytes.decode(encoding="utf-8", errors="strict")|Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
encode(encoding='UTF-8',errors='strict')|以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
endswith(suffix, beg=0, end=len(string))|检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
find(str, beg=0, end=len(string))|检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
index(str, beg=0, end=len(string))|跟find()方法一样，只不过如果str不在字符串中会报一个异常。
isalnum()|如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
isalpha()|如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
isdigit()|如果字符串只包含数字则返回 True 否则返回 False..
islower()|如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
isnumeric()|如果字符串中只包含数字字符，则返回 True，否则返回 False
join(seq)|以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
len(string)|返回字符串长度
lower()|转换字符串中所有大写字符为小写.
replace(old, new [, max])|把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。
split(str="", num=string.count(str))|以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串
splitlines([keepends])|按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
startswith(substr, beg=0,end=len(string))|检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
strip([chars])|去除字符串两边的空格

>bytes.decode()示例

bytes.decode(encoding='utf-8', errors="strict")
- encoding -- 要使用的编码，如"UTF-8"。
- errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
```python
str = "今天晴天"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
# 输出：
```

>encode()示例

encode(encoding='UTF-8',errors='strict')
- encoding -- 要使用的编码，如: UTF-8。
- errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
```python
str = "今天晴天"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
 
print(str)
 
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
 
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))
```


>endswith()示例

str.endswith(suffix[, start[, end]])
- suffix -- 该参数可以是一个字符串或者是一个元素。
- start -- 字符串中的开始位置。
- end -- 字符中结束位置。
```python
Str='example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))
```


>find()示例

str.find(str, beg=0, end=len(string))
- str -- 指定检索的字符串
- beg -- 开始索引，默认为0。
- end -- 结束索引，默认为字符串的长度。
```python
str1 = "example....wow!!!"
str2 = "exam"
 
print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))

info = 'abca'
print(info.find('a'))      # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0
print(info.find('a', 1))   # 从下标1开始，查找在字符串里第一个出现的子串：返回结果：3
print(info.find('3'))      # 查找不到返回-1
```


>index()示例

str.index(str, beg=0, end=len(string))
- str -- 指定检索的字符串
- beg -- 开始索引，默认为0。
- end -- 结束索引，默认为字符串的长度。

```python
str1 = " example....wow!!!"
str2 = "exam"

print (str1.index(str2))
print (str1.index(str2, 5))
print (str1.index(str2, 10))
```


>isalnum()示例
```python
str = "test2021"  # 字符串没有空格
print (str.isalnum())
 
str = "www.baidu.com"
print (str.isalnum())
```


>str.isalpha()示例
```python
str = "test"
print (str.isalpha())

# 字母和中文文字
str = "测试test"
print (str.isalpha())

str = "example....wow!!!"
print (str.isalpha())
```


>str.isdigit()示例
```python
str = "123456"
print (str.isdigit())

str = "example....wow!!!"
print (str.isdigit())
```


>str.islower()示例
```python
str = "TEST example....wow!!!"
print (str.islower())

str = "test example....wow!!!"
print (str.islower())
```


>str.isnumeric()示例
```python
str = "test2021"  
print (str.isnumeric())

str = "23443434"
print (str.isnumeric())
```


>join()示例
str.join(sequence)
- sequence -- 要连接的元素序列。
```python
s1 = "-"
s2 = ""
seq = ("t", "e", "s", "t") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))
```

>len()示例
```python
str = "test"
print(len(str))             # 字符串长度
6
l = [1,2,3,4,5]
print(len(l))               # 列表元素个数
```

>lower()示例
str.lower()
```python
str = "Test EXAMPLE....WOW!!!"
print( str.lower() )
```

>replace()示例
str.replace(old, new[, max])
- old -- 将被替换的子字符串。
- new -- 新字符串，用于替换old子字符串。
- max -- 可选字符串, 替换不超过 max 次
```python
str = "www.baidu.com"
print (str)
print (str.replace("baidu.com", "test.cn"))
 
str = "this is string example....wow!!!"
print (str.replace("is", "was", 3))
```


>split()示例

str.split(str="", num=string.count(str))
- str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
- num -- 分割次数。默认为 -1, 即分隔所有。
```python
str = "this is string example....wow!!!"
print (str.split( ))       # 以空格为分隔符
print (str.split('i',1))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符

txt = "Google#Baidu#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)
print(x)
```


>splitlines()示例
str.splitlines([keepends])
- keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。

```python
print('ab c\n\nde fg\rkl\r\n'.splitlines())
print('ab c\n\nde fg\rkl\r\n'.splitlines(True))
```

>startswith()示例

str.startswith(substr, beg=0,end=len(string))
- str -- 检测的字符串。
- substr -- 指定的子字符串。
- strbeg -- 可选参数用于设置字符串检测的起始位置。
- strend -- 可选参数用于设置字符串检测的结束位置。
```python
str = "this is string example....wow!!!"
print (str.startswith( 'this' ))   # 字符串是否以 this 开头
print (str.startswith( 'string', 8 ))  # 从第九个字符开始的字符串是否以 string 开头
print (str.startswith( 'this', 2, 4 )) # 从第2个字符开始到第四个字符结束的字符串是否以 this 开头
```

>strip()示例
str.strip([chars])
- chars -- 移除字符串头尾指定的字符序列。
- 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
```python
str = "*****this is **string** example....wow!!!*****"
print (str.strip( '*' ))  # 指定字符串 *
str = "123abcrunoob321"
print (str.strip( '12' ))  # 字符序列为 12
```