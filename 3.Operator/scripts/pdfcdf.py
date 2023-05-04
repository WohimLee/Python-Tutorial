import numpy as np
import matplotlib.pyplot as plt

# Define the x range and create the Gaussian and logistic PDFs
x = np.linspace(-5, 5, 500)
gaussian_pdf = np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi)
logistic_pdf = np.exp(-x) / (1 + np.exp(-x)) ** 2

# Normalize the PDFs so that the area under the curve is 1
gaussian_pdf_norm = gaussian_pdf / np.trapz(gaussian_pdf, x)
logistic_pdf_norm = logistic_pdf / np.trapz(logistic_pdf, x)

# Calculate the CDFs
gaussian_cdf = np.cumsum(gaussian_pdf_norm) * (x[1] - x[0])
logistic_cdf = np.cumsum(logistic_pdf_norm) * (x[1] - x[0])

# Plot the PDFs and CDFs
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Gaussian PDF
axs[0, 0].plot(x, gaussian_pdf_norm)
axs[0, 0].set_title('Gaussian PDF')

# Gaussian CDF
axs[1, 0].plot(x, gaussian_cdf)
axs[1, 0].set_title('Gaussian CDF')

# Logistic PDF
axs[0, 1].plot(x, logistic_pdf_norm)
axs[0, 1].set_title('Logistic PDF')

# Logistic CDF
axs[1, 1].plot(x, logistic_cdf)
axs[1, 1].set_title('Logistic CDF')

plt.show()
