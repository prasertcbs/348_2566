# %%
import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and subplot
fig, ax = plt.subplots()

# Create a list of points for the curve of the heart
t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
points = np.array([x, y]).T

# Plot the curve of the heart
plt.plot(x, y, color='r', linewidth=2)

# Fill in the heart with the color red
plt.fill(x, y, color='r', alpha=0.5)

# Display the plot
plt.axis('equal')
plt.show()

# %%
