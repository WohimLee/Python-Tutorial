&emsp;
# np.cumsum


>计算 CDF
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