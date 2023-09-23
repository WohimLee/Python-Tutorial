&emsp;
# np.dot
## 1-D Arrays
If both `a` and `b` are 1-D arrays, `np.dot(a, b)` computes the inner product of vectors, which is the sum of the pairwise products of their components:

$$\operatorname{dot}(a, b)=a_1 \cdot b_1+a_2 \cdot b_2+\ldots+a_n \cdot b_n$$

>Example: Dot Product of 1-D Arrays
```py
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = np.dot(a, b)
print("Dot product of a and b:", result)
```


&emsp;
## 2-D Arrays
If both a and b are 2-D arrays, np.dot(a, b) performs matrix multiplication. Though np.dot can be used for this purpose, it is more common to use `np.matmul` or the `@` operator for clarity.
>Example: Matrix Multiplication with 2-D Arrays
```py
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

result = np.dot(A, B)
print("Matrix multiplication of A and B:\n", result)
```


&emsp;
## 0-D Arrays (Scalars)
If either a or b is a 0-D array (a scalar), then np.dot(a, b) simply multiplies a and b. Again, it's more common to use `numpy.multiply(a, b)` or `a * b` for this.

>Example: Multiplication of Scalar
```py
import numpy as np

a = np.array(2)
b = np.array(3)

result = np.dot(a, b)
print("Multiplication of a and b:", result)
```


&emsp;
## N-D Array and 1-D Array
If `a` is an N-D array and `b` is a 1-D array, `np.dot(a, b)` performs a sum product over the last axis of `a` and `b`. Essentially, the last axis of `a` is contracted with `b`, effectively behaving like a series of dot products.
>Example: Sum Product Over Last Axis with N-D and 1-D Arrays
```py
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([1, 2])

result = np.dot(A, b)
print("Sum product over the last axis of A and b:", result)
```


&emsp;
## N-D Array and M-D Array
If `a` is an N-D array and b is an M-D array where $M≥2$, `np.dot(a, b)` performs a more general sum product over the last axis of `a` and the second-to-last axis of `b`. This would be similar to a more generalized form of matrix multiplication, and the result would be an array where the shape depends on the shapes of `a` and `b`.

The equation
$$\operatorname{dot}(a, b)[i, j, k, m]=\sum(a[i, j,:] \times b[k,:, m])$$

describes this general case.

>Example: Generalized Sum Product with N-D and M-D Arrays
```py
import numpy as np

A = np.random.rand(2, 3, 4)
B = np.random.rand(2, 4, 3)

result = np.dot(A, B)
print("Generalized sum product of A and B:\n", result)
```



