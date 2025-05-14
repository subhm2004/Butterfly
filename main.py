import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import cm

# Equation r(θ)
def r(theta):
    return np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) - np.sin(theta / 12)**5

# θ values
theta = np.linspace(0, 24 * np.pi, 2000)

# r(θ) → Cartesian coordinates
r_vals = r(theta)
x_vals = r_vals * np.cos(theta)
y_vals = r_vals * np.sin(theta)

# ---- Apply a 90° counter-clockwise rotation ONCE ----
angle_rad = np.radians(90)
x_rot = x_vals * np.cos(angle_rad) - y_vals * np.sin(angle_rad)
y_rot = x_vals * np.sin(angle_rad) + y_vals * np.cos(angle_rad)

# Plot setup
fig, ax = plt.subplots(figsize=(7, 7))
ax.set_facecolor("black")
fig.patch.set_facecolor("black")
ax.axis("off")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Line object
line, = ax.plot([], [], lw=2)

# Color map settings
colormap = cm.get_cmap("hsv")
num_colors = 24  # Change color every full π (approx 260-270 points here)
points_per_loop = len(theta) // num_colors  # ~83 for 2000 points and 24 loops

# Animation function
def get_animation():
    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        end = i + 1
        x = x_rot[:end]
        y = y_rot[:end]

        # Determine loop and color
        loop_index = (i // points_per_loop) % num_colors
        color_value = loop_index / num_colors
        line.set_color(colormap(color_value))

        line.set_data(x, y)
        return line,

    ani = FuncAnimation(
        fig, animate, init_func=init,
        frames=len(x_rot),
        interval=15, blit=True, repeat=True
    )

    plt.show()

# Entry point
if __name__ == "__main__":
    get_animation()
