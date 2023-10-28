import numpy as np
from numdifftools import Derivative as Df
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------------------------
f = lambda x: 0.65 - 0.75 / (1 + x**2) - 0.65 * x * np.arctan(1/x)
df = Df(f)
d2f = Df(df)

# Initial values
x0 = 0.2
X = np.linspace(0.1, 4, 200)
Y1 = f(X)
Y2 = df(X)

# Create the figure and subplots
fig, axs = plt.subplots(1, 2)
# Set the x-axis and y-axis labels for each subplot.
axs[0].set_title("f")
axs[1].set_title("f'")
axs[0].set_xlabel('X')
axs[0].set_ylabel('f')
axs[1].set_xlabel('X')
axs[1].set_ylabel("f'")
# Initialize empty scatter plots for animation

axs[0].plot(X,Y1, c='b')
axs[1].plot(X,Y2, c='b')
sc1 = axs[0].scatter([], [], c='y')
sc2 = axs[1].scatter([], [], c='y')

# Function to perform the Newton-Raphson method
def Newton_Rapson_method(f, df, d2f, x0, num_iter_max=1000, eps=1e-9):
    xv, y1, y2 = [x0], [f(x0)], [df(x0)]
    iter_ = 0
    while abs(y2[-1]) > eps and num_iter_max > iter_:
        f2 = d2f(xv[-1])
        if f2 != 0:
            xv.append(xv[-1] - y2[-1] / f2)
            y1.append(f(xv[-1]))
            y2.append(df(xv[-1]))
            iter_ += 1
        else:
            xv.append(xv[-1] - y2[-1] / eps)
            y1.append(f(xv[-1]))
            y2.append(df(xv[-1]))
            iter_ += 1
    return xv, y1, y2

# Perform the Newton-Raphson method and get the values
xv, y1, y2 = Newton_Rapson_method(f, df, d2f, x0, num_iter_max=1000, eps=1e-9)

# Animation update function
def update(frame):
    x1, y1_, x2, y2_ = xv[:frame], y1[:frame], xv[:frame], y2[:frame]
    sc1.set_offsets(np.c_[x1, y1_])
    sc2.set_offsets(np.c_[x2, y2_])
    return sc1, sc2

# Create the animation
ani = FuncAnimation(fig, update, frames=len(xv), blit=True, interval=300)

# Display the plot
plt.show()
