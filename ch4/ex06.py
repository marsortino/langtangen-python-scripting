# Exercise 4.6. Vectorize a formula containing an if condition
# Consider the following function f(x):
# f(x) = n/(n+1) * \align{
#                         0.5^{1+1/n} - (0.5 - x)^{1+1/n}, 0 <= x <= 0.5
#                         0.5^{1+1/n} - (x-0.5)^{1+1/n}, 0.5 < x <= 1
#                         }
# Here, n is a real number, typically 0 < n ≤ 1. (The formula describes the
# velocity of a pressure-driven power-law fluid in a channel.) Make a vectorized
# Python function for evaluating f(x) at a set of m equally spaced x values
# between 0 and 1 (i.e., no loop over the x values should appear). 

#!/usr/bin/env python

import numpy as np

def func(x, n):
    x1 = n/(n+1)*0.5**(1+1/n) - (0.5 - x)**(1+1/n) # RuntimeWarning when he starts calculating for x > 0.5
    x2 = n/(n+1)*0.5**(1+1/n) - (x - 0.5)**(1+1/n) # RuntimeWarning when he starts calculating for x < 0.5
    return np.where(x > 0.5, x2 , x1)

x = np.linspace(0, 1, 30)
n = 10

velocity = func(x,n)
print(velocity)