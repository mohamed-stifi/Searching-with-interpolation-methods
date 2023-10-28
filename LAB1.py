import math
import time
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
def search_with_fixe_step(f, x_init = 0 ,step = 0.05):
    f1 = f(x_init)
    f2 = f(x_init+step)
    if f2 < f1 :
        x_init = x_init + step
        while True :
            f1 = f2
            f2 = f(x_init+step)
            if f2 < f1 :
                x_init = x_init + step
            else :
                return (x_init - step, x_init+ step)
    elif f1 < f2 :
        x_init = x_init - step
        while True :
            f1 = f(x_init)
            f2 = f(x_init-step)
            if f1 > f2 :
                x_init = x_init - step
            else :
                return ( x_init - step, x_init + step)
    else :
        return (x_init - step,x_init + step)
    
# ---------------------------------------------------------------------
def search_with_accelerat_step(f, x_init = 0, step = 0.001):
    f1 = f(x_init)
    f2 = f(x_init+step)
    if f2 < f1 :
        x_init = x_init + step
        while True :
            f1 = f2
            f2 = f(x_init+step)
            if f2 < f1 :
                x_init = x_init + step
                step = 2*step
            else :
                return (x_init - step/2 , x_init + step)
    elif f1 < f2 :
        x_init = x_init - step
        while True :
            f1 = f(x_init)
            f2 = f(x_init-step)
            if f1 > f2:
                x_init = x_init - step
                step = 2*step
            else :
                return ( x_init-step, x_init + step/2)
    else :
        return (x_init - step,x_init + step)
# ---------------------------------------------------------------------
def exhaustive_Search(fun, a, b, n):
    delta = (b-a)/n
    x1 = a
    x2 = x1 + delta
    x3 = x2 + delta
    fx1 = fun(x1)
    fx2 = fun(x2)
    fx3 = fun(x3)
    iter_ = 0
    while fx1>=fx2 and  fx2>=fx3 :
        x1 = x2
        x2 = x3
        x3 = x3 + delta
        fx1 = fx2
        fx2 = fx3
        fx3 = fun(x3)
        iter_ = iter_ + 1 
    return x1, x2, iter_
# ---------------------------------------------------------------------
def dichotomous_Search(f,x_l, x_u , delta, eps = 1e-4, max_iter = 1000):
    iter_ = 0
    l = x_u - x_l
    while l > eps and iter_ < max_iter :
        l = x_u - x_l
        xc = (x_u + x_l)/2
        x1 = xc - delta/2
        x2 = xc + delta/2
        fx1 = f(x1)
        fx2 = f(x2)
        if fx1 < fx2 :
            x_u = x2
        elif fx1 > fx2 :
            x_l = x1
        else :
            x_u = x2
            x_l = x1
        iter_ = iter_ + 1
    return x_l, x_u, iter_, l
# ---------------------------------------------------------------------
def interval_Halving(f,x_l, x_u, eps = 1e-4, max_iter = 1000):
    iter_ = 0
    l = x_u - x_l
    while l > eps and iter_ < max_iter :
        l = x_u - x_l
        x0 = (x_u + x_l)/2
        x1 = x0 - l/4
        x2 = x0 + l/4
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        if fx1 <fx0 < fx2 :
            x_u = x0
        elif fx1 > fx0> fx2 :
            x_l = x0
        elif fx0 < fx1 and fx0 < fx2 :
            x_u = x2
            x_l = x1
        iter_ = iter_ + 1
    return x_l, x_u, iter_, l
# ---------------------------------------------------------------------
def fib(n):
    f0 = 1
    f1 = 1
    f =0
    for i in range(2, n+1):
        f = f0 + f1
        f0 = f1
        f1 = f
    return f1
def Fibonacci(f, x_l, x_u, n):
    l = x_u - x_l
    x1 = x_l + (fib(n-2)/ fib(n))*l
    x2 = x_l + (fib(n-1)/ fib(n))*l
    while n>1 :
        n = n - 1
        f1 = f(x1)
        f2 = f(x2)
        if f1 < f2 :
            x_u = x2
            l = x_u - x_l
            x2 = x1
            x1 = x_l + (fib(n-2)/ fib(n))*l
            f2 = f1
            f1 = f(x1)
        elif f1 > f2 :
            x_l = x1
            l = x_u - x_l
            x1 = x2
            f1 = f2
            x2 = x_l + (fib(n-1)/ fib(n))*l
            f2 = f(x2)
    return x_l , x_u , l
# ---------------------------------------------------------------------
def golden_Section(f, x_l, x_u, eps):
    phi = 2/( 1 + math.sqrt(5) ) 
    l = x_u - x_l
    x1 = x_l + (phi**2)*l
    x2 = x_l + phi*l
    f1 = f(x1)
    f2 = f(x2)
    while l > eps :
        if f1 < f2 :
            x_u = x2
            l = x_u - x_l
            x2 = x1
            x1 = x_l + (phi**2)*l
            f2 = f1
            f1 = f(x1)
        elif f1 > f2 :
            x_l = x1
            l = x_u - x_l
            x1 = x2
            f1 = f2
            x2 = x_l + phi*l
            f2 = f(x2)
    return x_l , x_u , l
# ---------------------------------------------------------------------

# ---------------------------------------------------------------------

# ---------------------------------------------------------------------