&emsp;
# np.linalg 

## np.linalg.norm
- 范数
```py
import numpy as np

arr = np.array([1, 2, 3])
print(np.linalg.norm(arr, ord=1))
print(np.linalg.norm(arr, ord=2))
print(np.linalg.norm(arr))
```


&emsp;
## np.linalg.det
- 行列式
```py
import numpy as np

arr = np.array(
    [[1, 2, 1],
     [3, 3, 2],
     [2, 1, 4]]
)
print(np.linalg.det(arr))
```

&emsp;
## np.linalg.inv
- 矩阵的逆
```py
import numpy as np

m = np.arange(4).reshape(2, 2)
print(np.linalg.inv(m))
```