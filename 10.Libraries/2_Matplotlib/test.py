import numpy as np
import matplotlib.pyplot as plt

x = np.array(["Test-1","Test-2","Test-3","Test-4"])
y = np.array([12, 22, 6, 18])

plt.barh(x, y, height = 0.1, color = ["#4CAF50","red","hotpink","#556B2F"])

plt.savefig("./test.jpg", dpi=300)