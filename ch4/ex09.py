# Exercise 4.9. Implement Exercise 2.10 using NumPy arrays.
# Solve the same problem as in Exercise 2.10, but use Numerical Python
# and a vectorized algorithm. Generate a random vector of 4n uniform integer
# numbers ranging from 1 to 6, reshape this vector into an array with four
# rows and n columns, representing the outcome of n throws with four dice,
# sum the eyes and estimate the probability. Insert CPU-time measurements
# in the scripts (see Chapter 4.1.4 or 8.10.1) and compare the plain Python
# solution in Exercise 2.10 with the version utilizing NumPy functionality.
# Hint: You may use the numpy functions random.randint, sum, and < (read
# about them in the NumPy reference manual, and notice especially that sum
# can sum the rows or the columns in a two-dimensional array).

from numpy import *

import sys, timeit

try:
    n = int(sys.argv[1])
except (IndexError):
    sys.stderr.write("Usage:" + sys.argv[0] + "number")

def roll(n_rolls):
    return random.randint(1, 7, 4*n_rolls)

random.seed(5)

t0 = timeit.default_timer()
e = roll(n).reshape(4, n)
results = e.sum(axis = 0)
p = where(results > 9, 1, 0)
p = sum(p)/float(n)
t1 = timeit.default_timer()
print(p)

# Exercise 2.10 code:
t2 = timeit.default_timer()
p = 0
for i in range(0,n):
    sum = 0
    for i in range(0,4):
       a = random.randint(1, 6)
       sum = sum + a
    if sum < 9: p += 1
t3 = timeit.default_timer()
print(1-p/float(n))


# Comparison
print('Time needed for the NumPy code:', t1-t0)
print('Time needed for the for code is:', t3-t2)