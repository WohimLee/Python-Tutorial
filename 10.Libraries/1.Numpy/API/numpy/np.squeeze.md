&emsp;

# np.squeeze
- numpy.squeeze 函数从给定数组的形状中删除一维的条目
    ```python
    numpy.squeeze(arr, axis)
    ```
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
