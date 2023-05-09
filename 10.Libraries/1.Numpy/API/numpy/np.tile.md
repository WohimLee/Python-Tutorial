&emsp;
# np.tile


```py
import numpy as np

channels = 6
groups = 2
kernel_size = 2
a1 = np.zeros((channels, int(channels / groups), kernel_size, kernel_size))
# print(a1)
index1 = np.arange(channels)
index2 = np.tile(np.arange(int(channels / groups)), groups)
# index2 = np.arange(int(channels/groups))

a1[index1, index2, :, :] = 0.1 # shape=(6, 2, 2)
a1[index1, :, :, :] = 0.1      # shape=(6, 3, 2, 2)
print(index2)
```