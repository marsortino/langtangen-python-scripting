# Create a script that in a loop from 1 to n draws two uniform random
# numbers between 1 and 6 and counts how many times p a 6 shows up. Write
# out the estimated probability p/float(n) together with the exact result 11/36.
# Run the script a few times with different n values (preferably read from the
# command line) and determine from the experiments how large n must be to
# get the first three decimals (0.306) of the probability correct.
# Use the random module to draw random uniformly distributed integers in
# a specified interval.

#!/usr/bin/env python
import sys, math, random

try:
    n = int(sys.argv[1])
except (IndexError):
    sys.stderr.write("Usage:" + sys.argv[0] + "n"); sys.exit(1)

p = 0
test = 0
for i in range(0, n):
    #a = random.randrange(1,7)
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    
    if a == 6 or b == 6: p += 1

if p == 0:
    print("Non è uscito nessun 6!")
else:
    print(p/float(n))