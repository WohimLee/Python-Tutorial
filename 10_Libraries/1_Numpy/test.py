import numpy as np


a1 = np.array([1, 2, 3], dtype=int)
a2 = np.array([1, 2, 3], dtype="float32")
a3 = np.array([1, 2, 3], dtype=np.int8)

print(a1.dtype)
print(a2.dtype)
print(a3.dtype)


