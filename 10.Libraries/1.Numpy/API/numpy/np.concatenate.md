

&emsp;
# np.concatenate
numpy.concatenate 函数用于沿指定 axis 连接 `相同形状` 的 `两个或多个`数组，格式如下：
```python
numpy.concatenate((a1, a2, ...), axis)
```
参数说明：

- a1, a2, ...：相同类型的数组
- axis: 沿着它连接数组的轴，默认为 0

>示例
```python
import numpy as np
a = np.arange(24).reshape(2, 3, 4)
b = np.arange(24).reshape(2, 3, 4)

c = np.concatenate((a, b), axis=0)
c = np.concatenate((a, b), axis=1)
c = np.concatenate((a, b), axis=2)

print(c.shape)
```
