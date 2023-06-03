
&emsp;

# np.expand_dims
- 在指定位置插入新的轴来扩展数组形状
    ```python
    numpy.expand_dims(arr, axis)
    ```
  - arr：输入数组
  - axis：新轴插入的位置
- 跟

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

