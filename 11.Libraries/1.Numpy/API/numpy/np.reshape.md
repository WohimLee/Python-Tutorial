

# np.reshape
- numpy.reshape 函数可以在不改变数据的条件下修改形状，格式如下： 
```python
numpy.reshape(arr, newshape, order='C')
```
- arr：要修改形状的数组
- newshape：整数或者整数数组，新的形状应当兼容原有形状
- order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'k' -- 元素在内存中的出现顺序。

>示例
```python
import numpy as np

a = np.arange(12)
# 两种使用方法
b = np.reshape(a, (3, 4)) # 方法一
c = a.reshape(4, 3)       # 方法二
print(b)
print(c)
```