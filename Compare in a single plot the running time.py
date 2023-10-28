from LAB1 import search_with_fixe_step,search_with_accelerat_step,\
                  exhaustive_Search, dichotomous_Search,\
                  interval_Halving,Fibonacci,\
                  golden_Section
from main import Newton_Rapson_method,Quasi_Newton_Method,\
                Secant_Method
import time 
import numpy as np
from numdifftools import Derivative as Df
import matplotlib.pyplot as plt
# -----------------------------------------------------------------
f = lambda x : 0.65 - 0.75/(1 + x**2) - 0.65*x*np.arctan(1/x)
df = Df(f)
d2f = Df(df)
x0 = 0.2
a = 0.2
b = 3
delta = 1e-3
X = np.linspace(0.1, 4 ,200)
Y = f(X)
# -------------------------------------------------------------------
methods = ['Search method with fixed step size',
    'Search method with accelerated step size','Exhaustive search method',
    'Dichotomous search method','Interval halving method',
    'Fibonacci method','Golden section method',
    'Newton-Rapson method', 'Quasi Newton Method', 'Secant Method']
time_of_methods = []
#--------------------------------------------------------------------
t1 = time.time()
search_with_fixe_step(f, x_init = 0.01 ,step = 0.00005)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
search_with_accelerat_step(f, x_init = 0.01, step = 0.00005)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
exhaustive_Search(f, 0.01, 2.0, 10000)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
dichotomous_Search(f,0.01, 2.0 , 0.001, eps = 1e-9, max_iter = 10000)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
interval_Halving(f,0.01, 2.0 , eps = 1e-9, max_iter = 10000)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
Fibonacci(f, 0.01, 2.0, 50)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
golden_Section(f, x_l= 0.01, x_u = 2.0, eps = 1e-5)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
Newton_Rapson_method( df, d2f, x0,num_iter_max= 1000, eps = 1e-9)
t2 = time.time()
time_of_methods.append(t2-t1)
#--------------------------------------------------------------------
t1 = time.time()
Quasi_Newton_Method(f, x0, delta,num_iter_max = 1000, eps = 1e-8)
t2 = time.time()
time_of_methods.append(t2-t1)
# -------------------------------------------------------------------
t1 = time.time()
Secant_Method(df, a, b, num_iter_max = 1000, eps = 1e-8)
t2 = time.time()
time_of_methods.append(t2-t1)
# -------------------------------------------------------------------
fig, ax = plt.subplots()
y = np.arange(len(time_of_methods))
ax.barh(y ,time_of_methods, align='center')
ax.set_yticks(y, labels=methods)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('running time')
ax.set_title('the running time for each method')
plt.show()