
&emsp;

# np.expand_dims
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

&emsp;
# None 的使用
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
