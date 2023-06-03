
&emsp;
# np.empty
numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组：
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
# np.zeros
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
# np.ones
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
```


&emsp;
# np.eye