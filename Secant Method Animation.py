import numpy as np
from numdifftools import Derivative as Df
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------------------------
f = lambda x: 0.65 - 0.75 / (1 + x**2) - 0.65 * x * np.arctan(1/x)
df = Df(f)
d2f = Df(df)

# Initial values
a = 0.2
b = 3
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
#--------------------------| Quasi Newton Method |---------------------------------
def Secant_Method(f, df, a, b, num_iter_max = 1000, eps = 1e-8):
    dfx = df(a)
    x = a 
    xv, y, y1 = [x],[f(x)],[dfx]
    iter_ = 0
    while np.abs(dfx) > eps and num_iter_max > iter_ :
        df1 = df(a)
        df2 = df(b)
        x = a - (df1*(b- a))/(df2 - df1)
        dfx = df(x)
        xv.append(x)
        y.append(f(x))
        y1.append(dfx)
        if dfx >= 0 :
            b = x
            df2 = dfx
        else :
            a = x
            df1 = dfx
        iter_ += 1
    return xv, y, y1 
# Perform the Newton-Raphson method and get the values
xv, y1, y2 = Secant_Method(f, df, a, b, num_iter_max = 1000, eps = 1e-8)

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
