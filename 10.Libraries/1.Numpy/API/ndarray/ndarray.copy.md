&emsp;
# np.copy

```py
import numpy as np

arr1 = np.array([1, 2, 3])
# 浅拷贝
arr2 = arr1
# 深拷贝
arr3 = arr1.copy()

print("id(arr1): ", id(arr1))
print("id(arr2): ", id(arr2))
print("id(arr3): ", id(arr3))
```