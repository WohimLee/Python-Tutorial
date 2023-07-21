

```py
import numpy as np

shape = (256, 256, 256)

# Generate all indices
indices = np.indices(shape)

print("Indices shape: ", indices.shape)
print("Indices example: ", indices[:, 0, 0])  # Example accessing the first set of indices
```