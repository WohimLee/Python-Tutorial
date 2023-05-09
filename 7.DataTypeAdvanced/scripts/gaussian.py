

import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, 200)

def gaussianPDF(x, mean=0, std=1):
    term1 = 1 / (std*np.sqrt(2*np.pi))
    term2 = np.exp(-1/(2*std**2)*(x - mean)**2)
    return term1*term2


def logisticPDF(x, mu=0, gamma=1):
    term1 = np.exp(-(x-mu)/gamma)
    term2 = gamma*(1+term1)**2
    return term1 / term2


def CDF(pdf):
    # Normalize the PDF so that it integrates to 1
    norm_const = np.trapz(pdf)
    pdf_normalized = pdf / norm_const

    # Sort the normalized PDF in ascending order
    pdf_sorted = np.sort(pdf_normalized)

    # Calculate the cumulative sum of the sorted PDF
    cdf = np.cumsum(pdf_sorted)

    # # Insert a zero at the beginning of the CDF
    # cdf = np.insert(cdf, 0, 0)

    return cdf

fig, axes = plt.subplots(1, 2, figsize=(10, 5))


ax1 = axes[0]
ax1.set(title='Gaussian PDF')
ax1.spines[['left', 'bottom']].set_position('zero')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)

y1 = gaussianPDF(x)
ax1.plot(x, y1)

ax2 = axes[1]
ax2.set(title='Gaussian CDF')
ax2.spines[['left', 'bottom']].set_position('zero')
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

y2 = CDF(y1)
ax2.plot(x, y2)

fig.suptitle('Gaussian Distribution')
fig.tight_layout()


plt.show()
# fig.savefig('../imgs/gaussian.png')



