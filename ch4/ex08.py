# Exercise 4.8. Implement Exercise 2.9 using NumPy arrays.
#
# Solve the same problem as in Exercise 2.9, but use Numerical Python
# and a vectorized algorithm. That is, generate a (long) random vector e of
# 2n uniform integer numbers ranging from 1 to 6, find the entries that are
# 6 by using where(e == 6, 1, 0), reshape the vector to a two-dimensional
# 2 × n array, add the two rows of this array to a new array e2, count how
# many of the elements in e2 that are greater than zero (these are the events
# where at least one die shows a 6) by sum(where(e2 > 0, 1, 0)). Estimate the
# probability from this count. Insert CPU-time measurements in the scripts
# (see Chapter 4.1.4 or 8.10.1) and compare the plain Python loop and the
# standard random module with the vectorized version utilizing random, where,
# and sum from numpy

#!/usr/bin/env python

from numpy import *

import sys, timeit


try:
    n = int(sys.argv[1])
except (IndexError):
     sys.stderr.write("Usage:" + sys.argv[0] + "n"); sys.exit(1)

random.seed(26)

# Exercise 2.9 code:

# import sys, math, random

# try:
#     n = int(sys.argv[1])
# except (IndexError):
#     sys.stderr.write("Usage:" + sys.argv[0] + "n"); sys.exit(1)

p = 0
test = 0
t0 = timeit.default_timer()
for i in range(0, n):
    a = random.randint(1, 7)
    b = random.randint(1, 7)
    
    if a == 6 or b == 6: p += 1
t1 = timeit.default_timer()
if p == 0:
    print("Non è uscito nessun 6!")
else:
    print(p/float(n))

# Exercise 4.8 code:

def roll(n_rolls):
    return random.randint(1, 7, 2*n_rolls)

t2 = timeit.default_timer()
e = roll(n)
e2 = where(e == 6, 1.0, 0.0).reshape(2, n)
p = sum(where(e2 > 0, 1, 0))
t3 = timeit.default_timer()

if p == 0:
    print("Non è uscito nessun 6!")
else:
    print(p/float(n))

print('Time needed for the loop is:', t1-t0)
print('Time needed for the vectorialized function is:', t3-t2)