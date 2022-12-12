&emsp;
# Numpy

NumPy 通常与 SciPy（Scientific Python）和 Matplotlib（绘图库）一起使用， 这种组合广泛用于替代 MatLab，是一个强大的科学计算环境，有助于我们通过 Python 学习数据科学或者机器学习。

SciPy 是一个开源的 Python 算法库和数学工具包。

SciPy 包含的模块有最优化、线性代数、积分、插值、特殊函数、快速傅里叶变换、信号处理和图像处理、常微分方程求解和其他科学与工程中常用的计算。

Matplotlib 是 Python 编程语言及其数值数学扩展包 NumPy 的可视化操作界面。

相关链接
- NumPy 官网 http://www.numpy.org/
- NumPy 源代码：https://github.com/numpy/numpy
- SciPy 官网：https://www.scipy.org/
- SciPy 源代码：https://github.com/scipy/scipy
- Matplotlib 官网：https://matplotlib.org/
- Matplotlib 源代码：https://github.com/matplotlib/matplotlib

安装NumPy（Linux）
```
~/anaconda3/envs/[自己的环境名]/bin/pip install pandas
```

&emsp;
# 1 NumPy Ndarray对象
NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。


&emsp;
# 2 NumPy 数据类型
&emsp;&emsp;numpy 支持的数据类型比 Python 内置的类型要多很多。下表列举了常用 NumPy 基本类型。

名称|	描述|
:--|:--
int8	|字节（-128 to 127）
int16	|整数（-32768 to 32767）
int32	|整数（-2147483648 to 2147483647）
int64	|整数（-9223372036854775808 to 9223372036854775807）
uint8	|无符号整数（0 to 255（2的8次方））
uint16	|无符号整数（0 to 65535（2的16次方））
uint32	|无符号整数（0 to 4294967295（2的32次方））
uint64	|无符号整数（0 to 18446744073709551615（2的64次方））
float16	|半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32	|单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	|双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位

- 拓展知识：浮点数在计算机中的表示方法：IEEE 754 标准
- numpy 的数值类型实际上是 dtype 对象的实例，并对应唯一的字符，包括 np.int32，np.float32，等等。

&emsp;
# 3 NumPy 数组属性

NumPy 的数组中比较重要 ndarray 对象属性有：

属性	|说明
:--|:--
ndarray.ndim	|轴的数量或维度的数量
ndarray.shape	|数组的维度，对于矩阵，n 行 m 列
ndarray.size	|数组元素的总个数，相当于 .shape 中 n*m 的值
ndarray.dtype	|ndarray 对象的元素类型
ndarray.itemsize	|ndarray 对象中每个元素的大小，以字节为单位

>ndarray.ndim
- ndarray.ndim 用于返回数组的维数，等于秩。

>示例
```python
import numpy as np 
 
a = np.arange(24)  
print (a.ndim)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2,4,3)  # b 现在拥有三个维度
print (b.ndim)
'''
输出结果为：

1
3
'''
```

>ndarray.shape
- ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目，即 ndim 属性。比如，一个二维数组，其维度表示"行数"和"列数"。

- ndarray.shape 也可以用于调整数组大小。

>示例
```python
import numpy as np  

a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)
'''
输出结果为：

(2, 3)
'''

# 调整数组大小。
a = np.array([[1,2,3],[4,5,6]]) 
a.shape =  (3,2)  
print (a)
'''
输出结果为：

[[1 2]
 [3 4]
 [5 6]]
'''
# NumPy 也提供了 reshape 函数来调整数组大小。
import numpy as np 
 
a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2)  
print (b)
'''
输出结果为：

[[1, 2] 
 [3, 4] 
 [5, 6]]
'''
```

>ndarray.itemsize
- ndarray.itemsize 以字节的形式返回数组中每一个元素的大小。

- 例如，一个元素类型为 float64 的数组 itemsize 属性值为 8(float64 占用 64 个 bits，每个字节长度为 8，所以 64/8，占用 8 个字节）。

>示例
```python
import numpy as np 
 
# 数组的 dtype 为 int8（一个字节）  
x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)
 
# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)
'''
输出结果为：
1
8
'''
```
