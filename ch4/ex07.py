# Exercise 4.7. Slicing of two-dimensional arrays.
# Consider the following recursive relation (arising when generalizing the
# one-dimensional diffusion equation scheme in Chapter 4.2.2 to two dimensions)
# u_{i,j}^{l+1} = \beta (u^l_{i-1, j} + u^l_{i+1, j} + u^l_{i, j-1} + u^l_{i1, j+1}) + (1 - 4\beta)u^l_{i,j}
# Write a straight Python loop implementing this recursion. Then replace the
# loop by a vectorized expression based on slices

#!/usr/bin/env python

import numpy as np
import timeit

def ddiff(u, beta):
    n = len(u[0]) - 1
    u_new = u.copy()
    for i, j in zip(range(1, n), range(1, n)):
        u_new[i-1,j-1] = beta*(u[i-1, j] + u[i+1, j] + u[i, j-1] + u[i, j+1]) + (1 - 4*beta)*u[i, j]
    return u_new

def vddiff(u, beta):
    n = len(u[0]) - 1
    u[1:n, 1:n] = beta*(u[0:n-1, 1:n] + u[2:n+1, 1:n] + u[1:n, 0:n-1] + u[1:n, 2:n+1]) + (1 - 4*beta)*u[1:n, 1:n]
    return u

#u = np.array([[1, 2, 5, 7, 9, 11], [2, 4, 5, 13, 21, 22]]) # array bidimensionale = matrice

# let's make a 9x9 matrix
u = np.linspace(1, 100, 81).reshape(9,9)
beta = 0.2

# a different approach to create a bidimensional array using linspace and newaxis is shown in 4.3.5 i.e.:
x = np.linspace(1, 9, 9)
y = np.linspace(1, 9, 9)
xv = x[:, np.newaxis] ; yv = y[np.newaxis, :]
print(xv + yv)


t0 = timeit.default_timer()
res = ddiff(u, beta)
t1 = timeit.default_timer()
vres = vddiff(u, beta)
t2 = timeit.default_timer()
print(res-vres)
print('Time needed for ddiff =', t1 - t0)
print('Time needed for vdiff =', t2 - t1 ) # è più lento il v diff. Chiedere perché