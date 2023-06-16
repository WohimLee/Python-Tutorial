

import numpy as np
import matplotlib.pyplot as plt


u = [2, 3, 1]
v = [0, 5, 4]
q = [7, -8, 10]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 10])

start = [0, 0, 0]
ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2])
ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2])
ax.quiver(start[0], start[1], start[2], q[0], q[1], q[2], color='r', arrow_length_ratio=0.1)


plt.show()