&emsp;
# np.sum



&emsp;
# np.cumsum
numpy.cumsum(a, axis=None, dtype=None, out=None)[source]
- Return the cumulative sum of the elements along a given axis.
- Parameters:
    - a: array_like
      - Input array
    - axis: int, optional
        - Axis along which the cumulative sum is computed. The default (None) is to compute the cumsum over the flattened array.
    - dtype: dtype, optional
        - Type of the returned array and of the accumulator in which the elements are summed. If dtype is not specified, it defaults to the dtype of a, unless a has an integer dtype with a precision less than that of the default platform integer. In that case, the default platform integer is used.
    - out: ndarray, optional
        - Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output but the type will be cast if necessary. See Output type determination for more details.
- Returns:
    - cumsum_along_axisndarray.
        - A new array holding the result is returned unless out is specified, in which case a reference to out is returned. The result has the same size as a, and the same shape as a if axis is not None or a is a 1-d array.

&emsp;
>示例 1
```py
import numpy as np

var = np.array([[1,2,3], [4,5,6]])
print(var)

res1 = np.cumsum(var)
print("res1: ", res1)

# specifies type of output value(s)
res2 = np.cumsum(var, dtype=float)     
print("res2: ", res2)

# 0 维度方向的累加
res3 = np.cumsum(var, axis=0)      
print("res3: ", res3)

# 1 维度方向累加
res4 = np.cumsum(var, axis=1)      
print("res4: ", res4)
```

&emsp;
>示例2: 计算 CDF
- Gaussian PDF
    $$p(x) = \frac{1}{\sigma \sqrt{2 \pi}} \cdot exp\Big({-\frac{1}{2\sigma^2}\cdot(x-\mu)^2}\Big)$$
```py
import numpy as np

# Define the x range and create the Gaussian and logistic PDFs
x = np.linspace(-5, 5, 500)
gaussian_pdf = np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)

# Normalize the PDFs so that the area under the curve is 1
gaussian_pdf_norm = gaussian_pdf / np.trapz(gaussian_pdf, x)

# Calculate the CDFs
gaussian_cdf = np.cumsum(gaussian_pdf_norm) * (x[1] - x[0])
```

&emsp;
# np.cumprod
numpy.cumprod(a, axis=None, dtype=None, out=None)[source]
- Return the cumulative product of elements along a given axis.

- Parameters:
    - a: array_like
        - Input array.
    - axis: int, optional
        - Axis along which the cumulative product is computed. By default the input is flattened.
    - dtype: dtype, optional
        - Type of the returned array, as well as of the accumulator in which the elements are multiplied. If dtype is not specified, it defaults to the dtype of a, unless a has an integer dtype with a precision less than that of the default platform integer. In that case, the default platform integer is used instead.
    - out: ndarray, optional
        - Alternative output array in which to place the result. It must have the same shape and buffer length as the expected output but the type of the resulting values will be cast if necessary.
- Returns:
    - cumprod: ndarray
        - A new array holding the result is returned unless out is specified, in which case a reference to out is returned.


