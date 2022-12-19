# Define a matrix and a vector, e.g.,
#   A = array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
#   b = array([-3, -2, -1])
# Use the NumPy manual to find a function that computes the standard matrix vector product A times b (i.e., the vector whose i-th component is 
# \sum^2_j=0 { A[i,j]*b[j]) }.


#!/usr/bin/env python 

from numpy import *

A = array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
b = array([-3, -2, -1])

c = matmul(A, b)
print(c)
