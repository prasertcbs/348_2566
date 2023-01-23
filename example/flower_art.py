# %%
import matplotlib.pyplot as plt
import numpy as np

# Set up the figure and subplot
fig, ax = plt.subplots()

# Set the number of petals and the radius of the circles
num_petals = 5
circle_radius = 0.5

# Create the petals as circles
for i in range(num_petals):
    angle = i * 2 * np.pi / num_petals
    x = circle_radius * np.cos(angle)
    y = circle_radius * np.sin(angle)
    ax.add_patch(plt.Circle((x, y), radius=0.5, color='r'))

# Create the center of the flower as a yellow circle
ax.add_patch(plt.Circle((0, 0), radius=0.2, color='y'))

# Display the plot
plt.axis('equal')
plt.show()

# %%
