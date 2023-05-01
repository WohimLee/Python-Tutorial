

import numpy as np
import matplotlib.pyplot as plt


x = np.array(["Test-1", "Test-2", "Test-3", "C-TEST"])
y = np.array([12, 22, 6, 18])

plt.barh(x, y,  color = ["#4CAF50","red","hotpink","#556B2F"], height=0.5)
plt.savefig("./imgs/bar2.png")