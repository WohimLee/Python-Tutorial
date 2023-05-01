import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

def sigmoid(x:np.ndarray):
    output = 1 / (1 + np.exp(-x))
    return output

y = sigmoid(x)

xlim = x.min(), x.max()
ylim = y.min(), y.max()

plt.title('sigmoid')
plt.xlabel('x')
# plt.xlim(xlim)
plt.ylabel('y')
# plt.ylim(ylim)
plt.plot(x, y, 'r-', label='sigmoid')
plt.legend()
plt.grid()
plt.savefig('./imgs/sigmoid.png', dpi=150)

# plt.show()