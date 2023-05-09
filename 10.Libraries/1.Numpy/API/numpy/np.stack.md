
&emsp;
# np.stack
numpy.stack 函数用于沿 `新轴` 连接数组序列，格式如下：
```python
numpy.stack(arrays, axis)
```

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
# np.hstack
- numpy.hstack 是 numpy.stack 函数的变体，它通过`水平堆叠（堆叠第1维）`来生成数组

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
# np.vstack
- numpy.vstack 是 numpy.stack 函数的变体，它通过`垂直堆叠（堆叠第0维）`来生成数组

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