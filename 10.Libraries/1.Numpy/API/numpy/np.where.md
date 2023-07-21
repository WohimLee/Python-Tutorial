&emsp;
# np.where



```py
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
result = np.where(arr > 3, "A", "B")
print(result)

```
Output:
```
['B' 'B' 'B' 'A' 'A']
```

```py

# occ_predict    = occ.copy()
# occ_predict[occ >= 0.5] = 1
# occ_predict[occ < 0.5] = 0
occ_predict = np.where(occ >= 0.5, 1, -1)
```