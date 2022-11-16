# Extend the script from Exercise 2.1 such that you draw n random uniformly distributed numbers, 
# where n is given on the command line, and compute the average of these numbers

#!/usr/bin/env python

import random, sys

try:
    nsample = int(sys.argv[1])
except:
    print("Usage:", sys.argv[0], "nsample"); sys.exit(1)

a = 0
i = 0

while i <= nsample:
    a += random.uniform(-1, 1)
    i += 1

print("Average of %d random numbers between -1 and 1 is: %g" % (nsample, a/nsample))
