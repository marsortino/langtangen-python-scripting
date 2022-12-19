# The function
#   def initial_condition(x):
#       return 3.0
# does not work properly when x is a NumPy array. In that case the function
# should return a NumPy array with the same shape as x and with all entries
# equal to 3.0. Perform the necessary modifications such that the function works
# for both scalar types and NumPy arrays

#!/usr/bin/env python

from numpy import *

def initial_condition(x):
  if isinstance(x, ndarray):
      r = zeros(x.size, float) + 3
  else:
      r = 3
  return r 

# def initial_condition(x):
#     x1 = zeros(x.size, float) + 3
#     x2 = 3
#     return where(isinstance(x, ndarray), x1 , x2)

x = array([1, 2, 3, 5, 0])
constant_function = initial_condition(x)
print(constant_function)