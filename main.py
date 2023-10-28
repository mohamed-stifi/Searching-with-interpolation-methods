import numpy as np
from numdifftools import Derivative as Df
import matplotlib.pyplot as plt
from time import time

#--------------------------| global variable |---------------------------------
f = lambda x : 0.65 - 0.75/(1 + x**2) - 0.65*x*np.arctan(1/x)
df = Df(f)
d2f = Df(df)
x0 = 0.2
a = 0.2
b = 3
delta = 1e-3
X = np.linspace(0.1, 4 ,200)
Y = f(X)
#--------------------------| plot the function |---------------------------------
plt.plot(X, Y, label = "$f(x) = 0.65 - 0.75/(1+x^2) -0.65xtan^{-1}(1/x)$")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#--------------------------| Newton-Rapson method |---------------------------------
def Newton_Rapson_method( df , d2f, x0,num_iter_max= 1000, eps = 1e-9) :
    """
    parametrs:
        df :
        d2f :
        x0 :
        eps :
    return :
        x0 :
        iter_ :
    """
    f1  = df(x0)
    iter_ = 0
    while np.abs(f1) > eps and num_iter_max > iter_ :
        f2 = d2f(x0)
        if f2 != 0 :
            x0 -= f1/f2
            f1  = df(x0)
            iter_ += 1
        else :
            x0 -= f1/eps
            f1  = df(x0)
            iter_ += 1

    return x0 , iter_

#---------------------------|Quasi Newton Method |--------------------------------
def Quasi_Newton_Method(f, x0, delta,num_iter_max = 1000, eps = 1e-8):
    """
    parametrs:
        f : 
        x0 :
        delta :
        num_iter_max :
        eps :
    return :
        x0 :
        iter_ :
    """
    f1 = f(x0 + delta)
    f2 = f(x0 - delta)
    delta_2 = 2*delta
    df = (f1 - f2)/delta_2
    iter_ = 0
    while np.abs(df) > eps and num_iter_max > iter_ :
        x0 -= (delta*(f1 - f2))/(2*(f1 - 2*f(x0) + f2))
        f1 = f(x0 + delta)
        f2 = f(x0 - delta)
        df = (f1 - f2)/delta_2
        iter_ += 1
    return x0 , iter_

#---------------------------| Secant Method |--------------------------------
def Secant_Method(df, a, b, num_iter_max = 1000, eps = 1e-8):
    """
    parametrs:
        df : 
        a :
        b :
        num_iter_max :
        eps :
    return :
        x0 :
        iter_ :
    """
    dfx = df(a)
    x = a 
    iter_ = 0
    while np.abs(dfx) > eps and num_iter_max > iter_ :
        df1 = df(a)
        df2 = df(b)
        x = a - (df1*(b- a))/(df2 - df1)
        dfx = df(x)
        if dfx >= 0 :
            b = x
            df2 = dfx
        else :
            a = x
            df1 = dfx
        iter_ += 1
    return x , iter_

#----------------------------| time complixity |-------------------------------
methods = ['Newton-Rapson method', 'Quasi Newton Method', 'Secant Method']
times = []
x_optm = []
optm_iter = []
t1 = time()
N_x , N_iter_ = Newton_Rapson_method( df, d2f, x0,num_iter_max= 1000, eps = 1e-9)
t2 = time()
times.append(t2-t1)
x_optm.append(N_x)
optm_iter.append(N_iter_)
# -------------
t1 = time()
Q_x , Q_iter_ = Quasi_Newton_Method(f, x0, delta,num_iter_max = 1000, eps = 1e-8)
t2 = time()
times.append(t2-t1)
x_optm.append(Q_x)
optm_iter.append(Q_iter_)
# --------------
t1 = time()
S_x , S_iter_ = Secant_Method(df, a, b, num_iter_max = 1000, eps = 1e-8)
t2 = time()
times.append(t2-t1)
x_optm.append(S_x)
optm_iter.append(S_iter_)

# ---------------------------------------------------------------
print('times : ', times)
fig, ax = plt.subplots()
y = np.arange(len(times))
ax.barh(y ,times, align='center')
ax.set_yticks(y, labels=methods)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('running time')
ax.set_title('the running time for each method')

plt.show()

#------------------
print('x optimal : ',x_optm)
plt.scatter(methods,x_optm)
plt.ylabel('x optimal')
plt.title('resulta of the methods')
plt.show()
## --------------
print('number of iterition : ',optm_iter)
plt.bar(methods,optm_iter)
plt.ylabel('number of iter')
plt.title('number of itertion for get the resulta of the methods')
plt.show()