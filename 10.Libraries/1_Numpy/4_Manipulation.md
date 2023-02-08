&emsp;
# Numpy 数组操作

&emsp;
# 1 修改数组形状
&emsp;
## 1.1 numpy.reshape
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


&emsp;
## 1.2 numpy.ndarray.flatten
- numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组，格式如下：
```python
ndarray.flatten(order='C')
```
参数说明：
- order：'C' -- 按行，'F' -- 按列，'A' -- 原顺序，'K' -- 元素在内存中的出现顺序。
>示例
```python
import numpy as np
 
a = np.arange(12).reshape(3, 4)

b1 = a.flatten(order='C')
b2 = a.flatten(order='F')
b3 = a.flatten(order='A')
b4 = a.flatten(order='K')
print(a)
print("-------------------")
print("C: ", b1)
print("F: ", b2)
print("A: ", b3)
print("K: ", b4)
```

&emsp;
# 2 翻转数组
&emsp;
## 2.1 numpy.transpose
- numpy.transpose 函数用于对换数组的维度，格式如下：
```python
numpy.transpose(arr, axes)
ndarray.transpose(axes)
```
参数说明:

- arr：要操作的数组
- axes：整数列表，对应维度，通常所有维度都会对换，可以传入元组做维度转换。

>示例
```python
import numpy as np

# 示例1：转置数组
a = np.arange(12).reshape(3,4)
print(a)
print(np.transpose(a))


# 示例2：模拟图片维度转换的例子
a = np.arange(300).reshape(3,10,10) # 3通道，10x10像素的图片
a_r = a.reshape(10, 10, 3)
a_t = a.transpose((1,2,0))
print(a[0])
print(a_r[..., 0]) # 取出来的像素跟原来像素不一致
print(a_t[..., 0]) # 取出来的像素就是原来通道的像素
```

&emsp;
## 2.2 numpy.ndarray.T 
- 类似 numpy.transpose：

>示例
```python
import numpy as np
 
a = np.arange(12).reshape(3,4)
print (a)
print (a.T)
```

&emsp;
## 2.3 numpy.swapaxes
- numpy.swapaxes 函数用于交换数组的两个轴，格式如下：
```python 
numpy.swapaxes(arr, axis1, axis2)
ndarray.swapaxes(axis1, axis2)
```
- arr：输入的数组
- axis1：对应第一个轴的整数
- axis2：对应第二个轴的整数

```python   
import numpy as np

# transpose 和 swapaxes 对比
a = np.arange(300).reshape(3,10,10) 
a_t = a.transpose((0, 2, 1))
a_s = a.swapaxes(1, 2)
print(a_t[0])
print(a_s[0])
```
&emsp;
# 3 修改数组维度

>numpy.expand_dims
- numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状，函数格式如下:
```python
numpy.expand_dims(arr, axis)
```
参数说明：
- arr：输入数组
- axis：新轴插入的位置

>示例
```python
import numpy as np
 
a = np.arange(24).reshape(3, 2, 4)
b = np.expand_dims(a, 0)
c = np.expand_dims(a, 1)
d = np.expand_dims(a, 2)
e = np.expand_dims(a, 3)

print(b.shape)
print(c.shape)
print(d.shape)
print(e.shape)
```

>numpy.squeeze

- numpy.squeeze 函数从给定数组的形状中删除一维的条目，函数格式如下：
```python
numpy.squeeze(arr, axis)
```
参数说明：

- arr：输入数组
- axis：整数或整数元组，用于选择形状中一维条目的子集

>示例
```python
import numpy as np
 
a = np.arange(24).reshape(1, 3, 1, 2, 4)
b = np.squeeze(a)
c = np.squeeze(a, 0)

print(b.shape)
print(c.shape)
```

>None 的使用
```python
import numpy as np

a = np.arange(24).reshape(3, 2, 4)
print(a.shape)
b1 = a[None]
b2 = a[..., None]
b3 = a[0, None, ...]
print(b1.shape)
print(b2.shape)
print(b3.shape)
```


&emsp;
# 4 连接数组

## 4.1 numpy.concatenate
- numpy.concatenate 函数用于沿指定轴连接`相同形状`的`两个`或`多个`数组，格式如下：
```python
numpy.concatenate((a1, a2, ...), axis)
```
参数说明：

- a1, a2, ...：相同类型的数组
- axis：沿着它连接数组的轴，默认为 0

>示例
```python
import numpy as np

a = np.arange(24).reshape(3, 2, 4)
b = np.arange(24).reshape(3, 2, 4)

c = np.concatenate((a, b), axis=0)

print(a)
print("------------------------")
print(b)
print("------------------------")
print(c.shape)
```

&emsp;
## 4.2 numpy.stack
- numpy.stack 函数用于沿`新轴`连接数组序列，格式如下：
```python
numpy.stack(arrays, axis)
```
参数说明：

- arrays相同形状的数组序列
- axis：返回数组中的轴，输入数组沿着它来堆叠

>示例
```python
import numpy as np

a = np.arange(24).reshape(3, 2, 4)
b = np.arange(24).reshape(3, 2, 4)
c = np.arange(24).reshape(3, 2, 4)
d = np.arange(24).reshape(3, 2, 4)


res = np.stack((a, b, c, d), axis=0) # 第0维变成 4
print(res.shape)
res = np.stack((a, b, c, d), axis=1) # 第1维变成 4
print(res.shape)
res = np.stack((a, b, c, d), axis=2) # 第2维变成 4
print(res.shape)
```

&emsp;
## 4.3 numpy.hstack
- numpy.hstack 是 numpy.stack 函数的变体，它通过`水平堆叠（堆叠第1维）`来生成数组。

>示例
```python
import numpy as np

a = np.arange(24).reshape(3, 2, 4)
b = np.arange(24).reshape(3, 2, 4)
c = np.arange(24).reshape(3, 2, 4)
d = np.arange(24).reshape(3, 2, 4)

res = np.hstack((a, b, c, d)) 
print(res.shape)

a = np.arange(24).reshape(1, 3, 2, 4)
b = np.arange(24).reshape(1, 3, 2, 4)
c = np.arange(24).reshape(1, 3, 2, 4)
d = np.arange(24).reshape(1, 3, 2, 4)

res = np.hstack((a, b, c, d)) 
print(res.shape)

a = np.arange(24).reshape(1, 1, 3, 2, 4)
b = np.arange(24).reshape(1, 1, 3, 2, 4)
c = np.arange(24).reshape(1, 1, 3, 2, 4)
d = np.arange(24).reshape(1, 1, 3, 2, 4)

res = np.hstack((a, b, c, d)) 
print(res.shape)
```

&emsp;
## 4.4 numpy.vstack
- numpy.vstack 是 numpy.stack 函数的变体，它通过`垂直堆叠（堆叠第0维）`来生成数组。

>示例
```python
import numpy as np

a = np.arange(24).reshape(3, 2, 4)
b = np.arange(24).reshape(3, 2, 4)
c = np.arange(24).reshape(3, 2, 4)
d = np.arange(24).reshape(3, 2, 4)

res = np.vstack((a, b, c, d)) 
print(res.shape)

a = np.arange(24).reshape(1, 3, 2, 4)
b = np.arange(24).reshape(1, 3, 2, 4)
c = np.arange(24).reshape(1, 3, 2, 4)
d = np.arange(24).reshape(1, 3, 2, 4)

res = np.vstack((a, b, c, d)) 
print(res.shape)

a = np.arange(24).reshape(1, 1, 3, 2, 4)
b = np.arange(24).reshape(1, 1, 3, 2, 4)
c = np.arange(24).reshape(1, 1, 3, 2, 4)
d = np.arange(24).reshape(1, 1, 3, 2, 4)

res = np.vstack((a, b, c, d)) 
print(res.shape)
```