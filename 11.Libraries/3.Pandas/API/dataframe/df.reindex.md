&emsp;
# df.reindex

>示例1 ：reindex修改行、列

```py
import pandas as pd
import numpy as np

frame1 = pd.DataFrame(np.arange(9).reshape((3, 3)),index=['a', 'c', 'd'])
frame2 = frame1.reindex(['a', 'd','c'])
frame3 = frame1.reindex([2,1,0,3],axis=1)
print(frame2)
print(frame3)
```