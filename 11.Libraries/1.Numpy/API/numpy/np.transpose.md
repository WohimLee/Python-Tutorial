
# numpy.transpose
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
