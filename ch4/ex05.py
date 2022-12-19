# The integral of a function f(x) from x = a to x = b can be calculated
# numerically by the Trapezoidal rule
# \int{f(x)}_a^b = h/2 f(a) + h/2 f(b) + h \sum^{n-1}_{i=1} f(a+ih);    h = (b-a)/n
# Implement this approximation in a Python function containing a straightforward loop.
# The code will run slowly compared to a vectorized version. Make the
# vectorized version and introduce timings to measure the gain of vectorization.
# Use the function
# f1(x)=1+2x
# as test functions for the integration

#!/usr/bin/env python

from numpy import *
import timeit

def func(x):
    return 1+2*x

def trapz(a, b, n):
    x = linspace(a, b , n)
    h = (b-a)/(n-1)
    sum = 0
    for i in range(1, len(x)-1):
        sum += func(a+i*h)
    return h*sum + h/2*func(a)+h/2*func(b)

def vtrapz(a, b, n):
    x = linspace(a, b, n)
    h = (b-a)/(n-1)
    f = func(x)
    return h/2*(f[0]+f[-1]) + h*f[1:-1].sum()

a = 1; b = 100; n = 10000

t0 = timeit.default_timer()
F = trapz(a, b, n) 
t1 = timeit.default_timer()
vF = vtrapz(a, b, n)
t2 = timeit.default_timer()
print(F)
print(vF)

print('time needed for trapz is:', t1-t0)
print('time needed for vtrapz is:', t2-t1)