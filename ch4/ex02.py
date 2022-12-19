# Extract the 2 × 2 matrix in the lower right corner of the matrix A in
# Exercise 4.1 as a slice. Add this slice to another 2 × 2 matrix, multiply the
# result by a 2 × 2 matrix, and insert this final result in the upper left corner
# of the original matrix A. Control the result by hand calculations.

#!/usr/bin/env python

from numpy import *

A = array([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
print(A)

slicedA = A.copy()
slicedA = slicedA[1:,1:]
id2 = eye(2)
slicedA = (slicedA+id2)*id2

A[:2,:2] = slicedA
print(A)