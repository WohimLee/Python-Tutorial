
&emsp;
# NumPy 创建数组
ndarray 对象由计算机内存的连续一维部分组成，并结合索引模式，将每个元素映射到内存块中的一个位置。内存块以行顺序(C样式)或列顺序(FORTRAN或MatLab风格，即前述的F样式)来保存元素。
&emsp;
# 1 基本方式
创建一个 ndarray 只需调用 NumPy 的 array 函数即可：
```python
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
```
参数说明：

- object	数组或嵌套的数列
- dtype	数组元素的数据类型，可选
- copy	对象是否需要复制，可选
- order	创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
- subok	默认返回一个与基类类型一致的数组
- ndmin	指定生成数组的最小维度


>示例
```python
import numpy as np 

# 实例 1
a = np.array([1,2,3])  
print (a)

# 实例 2
# 多于一个维度  
a = np.array([[1,  2],  [3,  4]])  

# 实例 3: 指定数据类型
a1 = np.array([1, 2, 3], dtype=int) # 只写 int float 默认是 64 位
a2 = np.array([1, 2, 3], dtype="float32")
a3 = np.array([1, 2, 3], dtype=np.int8)

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)
```

&emsp;
# 2 其它创建数组的方法
ndarray 数组也可以通过以下几种方式来创建。

&emsp;
## 2.1 numpy.empty
- numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
```python
numpy.empty(shape, dtype = float, order = 'C')
```
参数说明：

- shape	数组形状
- dtype	数据类型，可选
- order	有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

>示例
```python
import numpy as np 
a = np.empty([3,2], dtype = int) # shape 可以传 tuple
```
- 注意：数组元素为随机值，因为它们未初始化。

&emsp;
## 2.2 numpy.zeros
- 创建指定大小的数组，数组元素以 0 来填充：
```python
numpy.zeros(shape, dtype = float, order = 'C')
```
参数说明：

- shape	数组形状
- dtype	数据类型，可选
- order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组
>示例
```python
import numpy as np
 
# 默认为浮点数
x = np.zeros(5) 
print(x)
 
# 设置类型为整数
y = np.zeros((5,), dtype = np.int) 
print(y)
```

&emsp;
## 2.3 numpy.ones
- 创建指定形状的数组，数组元素以 1 来填充：
```python
numpy.ones(shape, dtype = None, order = 'C')
```
参数说明：

- shape	数组形状
- dtype	数据类型，可选
- order	'C' 用于 C 的行数组，或者 'F' 用于 FORTRAN 的列数组

>示例
```python
import numpy as np
 
# 默认为浮点数
x = np.ones(5) 
print(x)
 
# 自定义类型
x = np.ones([2,2], dtype = int)
print(x)
'''输出结果为：

[1. 1. 1. 1. 1.]
[[1 1]
 [1 1]]'''
```

&emsp;
# 3 NumPy 从已有的数组创建数组

>numpy.asarray
```python
numpy.asarray(a, dtype = None, order = None)
```
参数说明：

- a	任意形式的输入参数，可以是，列表, 列表的元组, 元组, 元组的元组, 元组的列表，多维数组
- dtype	数据类型，可选
- order	可选，有"C"和"F"两个选项,分别代表，行优先和列优先，在计算机内存中的存储元素的顺序。

>示例
```python
import numpy as np 

# 示例1：将列表转换为 ndarray
x =  [[1,2,3], [4,5,6]] 
a = np.asarray(x)  
print (a)
'''输出结果为：
[1  2  3]'''

# 示例2：将元组转换为 ndarray:
x =  ((1,2,3), (4,5,6)) 
a = np.asarray(x)  
print (a)
'''输出结果为：
[1  2  3]'''

# 示例3：设置了 dtype 参数：
x =  [1,2,3] 
a = np.asarray(x, dtype =  float)  
print (a)
'''输出结果为：
[ 1.  2.  3.]'''
```

&emsp;
# 4 NumPy 从数值范围创建数组

>numpy.arange
```python
numpy.arange(start, stop, step, dtype)
```
- 根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray。

参数说明：
- start	起始值，默认为0
- stop	终止值（不包含）
- step	步长，默认为1
- dtype	返回ndarray的数据类型，如果没有提供，则会使用输入数据的类型

>示例
```python
import numpy as np

# 示例1：生成 0 到 5 的数组:
x = np.arange(5)  
print (x)
'''输出结果如下：
[0  1  2  3  4]'''

# 示例2：设置返回类型位 float:
# 设置了 dtype
x = np.arange(5, dtype =  float)  
print (x)
'''输出结果如下：
[0.  1.  2.  3.  4.]'''

# 示例3：设置了起始值、终止值及步长：
x = np.arange(10,20,2)  
print (x)
'''输出结果如下：
[10  12  14  16  18]'''
```
