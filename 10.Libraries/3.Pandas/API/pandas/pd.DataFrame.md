&emsp;
# pd.DataFrame

>示例
```py
import numpy as np
import pandas as pd

data = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index   = ['Ohio', 'Colorado', 'Utah', 'New York'],
    columns = ['one', 'two', 'three', 'four'])
data[data < 5] =0
print(data)
```



>示例
```python
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.arange(16).reshape((4, 4)),
    index   = ['Ohio', 'Colorado', 'Utah', 'New York'],
    columns = ['one', 'two', 'three', 'four'])

print(data)
print(data['two'])
print(data[['one', 'three']])
print(data[:2])
print(t := (data['three'] > 5))
print(data[t])
```

