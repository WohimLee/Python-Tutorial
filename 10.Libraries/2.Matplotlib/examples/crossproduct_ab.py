import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define vectors a and b
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Calculate the cross product of a and b
result = np.cross(a, b)

# Calculate the magnitude of the cross product
magnitude = np.linalg.norm(result)

# Calculate the signed area of the parallelogram
signed_area = magnitude * np.sign(np.dot(result, result))

# Define the origin point
origin = np.array([0, 0, 0])

# Create the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
ax.quiver(*origin, *a, color='r', label='a', arrow_length_ratio=0.1)
ax.quiver(*origin, *b, color='b', label='b', arrow_length_ratio=0.1)
ax.quiver(*origin, *result, color='g', label='a x b', arrow_length_ratio=0.1)


# Plot the parallelogram
parallelogram = np.array([origin, a, a + b, b])
parallelogram_poly = Poly3DCollection([parallelogram], alpha=0.3)
parallelogram_poly.set_facecolor('blue')
ax.add_collection3d(parallelogram_poly)

# Set the axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('|a x b| Visualization')

# Set the plot limits
max_val = max(np.max(np.abs(a)), np.max(np.abs(b)))
ax.set_xlim([-max_val, max_val])
ax.set_ylim([-max_val, max_val])
ax.set_zlim([-max_val, max_val])

# Add a legend
ax.legend()

# Add the signed area as text
ax.text(0, 0, max_val, f'Signed Area: {signed_area}', ha='center', va='center')

# Show the plot
plt.show()
