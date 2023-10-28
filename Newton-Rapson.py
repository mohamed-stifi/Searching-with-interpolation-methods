import numpy as np
from numdifftools import Derivative as Df
import matplotlib.pyplot as plt

#--------------------------| global variable |---------------------------------
def A_plot(x1 , y1, x2, y2):
    t = 0.5
    fig, axs = plt.subplots(1, 2)
    axs[0].plot(X, Y1)

    axs[1].plot(X, Y2, label= "$f'$")
    
    
    # Set the x-axis and y-axis labels for each subplot.
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('f')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel("f'")

    # Add titles to the subplots.
    axs[0].set_title("La valeur de f à chaque étape de méthode Newton-Rapson")
    axs[1].set_title("La valeur de f' à chaque étape de méthode Newton-Rapson")

    # Plot the data on the subplots.
    for x , y in zip(x1, y1) : 
        axs[0].scatter([x], [y],  c= 'y')
        plt.pause(t)
    for x , y in zip(x2, y2) : 
        axs[1].scatter([x], [y], c= 'y')
        plt.pause(t)
    

    # Display the plot.
    plt.show()

# --------------------------------------------------------------------------
f = lambda x : 0.65 - 0.75/(1 + x**2) - 0.65*x*np.arctan(1/x)
df = Df(f)
d2f = Df(df)
x0 =  0.2

X = np.linspace(0.1, 4 ,200)
Y1 = f(X)
Y2 = df(X)
#--------------------------| Newton-Rapson method |---------------------------------
def Newton_Rapson_method( f,df , d2f, x0,num_iter_max= 1000, eps = 1e-9) :
    f1  = df(x0)
    xv, y, y1 = [x0],[f(x0)],[f1]
    iter_ = 0
    while np.abs(f1) > eps and num_iter_max > iter_ :
        f2 = d2f(x0)
        if f2 != 0 :
            x0 -= f1/f2
            f1  = df(x0)
            xv.append(x0)
            y.append(f(x0))
            y1.append(f1)
            iter_ += 1
        else :
            x0 -= f1/eps
            f1  = df(x0)
            xv.append(x0)
            y.append(f(x0))
            y1.append(f1)
            iter_ += 1

    return xv, y, y1 , iter_
#--------------------------- | resulta | -------------------------------
xv, y1, y2 , iter_ = Newton_Rapson_method( f, df, d2f, x0,num_iter_max= 1000, eps = 1e-9)

x1 ,x2 = xv, xv
# ---------------------------------------------------------------
A_plot(x1 , y1, x2 , y2) 
