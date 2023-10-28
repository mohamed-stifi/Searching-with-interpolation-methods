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
    axs[0].set_title("La valeur de f à chaque étape de méthode Secant ")
    axs[1].set_title("La valeur de ~f' à chaque étape de méthode Secant ")

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
a = 0.2
b = 3
X = np.linspace(0.1, 4 ,200)
Y1 = f(X)
Y2 = df(X)
#--------------------------| Secant Method |---------------------------------
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
    return xv, y, y1 , iter_

#--------------------------- | resulta | -------------------------------
xv, y1, y2 , iter_ = Secant_Method(f, df, a, b, num_iter_max = 1000, eps = 1e-8)

x1 ,x2 = xv, xv
# ---------------------------------------------------------------
A_plot(x1 , y1, x2 , y2) 
