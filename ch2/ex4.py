# We consider an extension of the Scientific Hello World
# script hw.py. The script is now supposed to read an arbitrary
# number of command-line arguments and write the natural logarithm of each
# number to the screen.
#
# Implement four types of loops over the command-line entries:
# - a for r in sys.argv[1:] loop
# - a for loop with an integer counter i running over the relevant indices in sys.argv (using range function)
# - a while loop with an integer counter running over the relevant indices in sys.argv
# - an "infinite" while 1: loop with an integer counter and a try-except block where whe break out of the loop when sys.argv[i] is an illegal operation

#!/usr/bin/env python

import math
import sys

def ln_r(r):
    if r > 0:
        a = math.log(r)
        print("ln(%g) = %g" % (r, a))
    else:
        print("ln(%g) is illegal." % (r))


# # first loop
# # for r in sys.argv[1:]:

# #     r = float(r)
# #     ln_r(r)

# # # second loop
# lenght = len(sys.argv)
# for i in range(1, lenght):
#     r = float(sys.argv[i])
#     ln_r(r)

# # # third loop
# lenght = len(sys.argv)
# lenght -= 1 
# i = 1
# while i <= lenght:
#     r = float(sys.argv[i])
#     ln_r(r)
#     i += 1

# # four loop
i = 1
while 1:
    try:
        r = float(sys.argv[i])
        ln_r(r)
        i += 1
    except:
        print("Finished!"); sys.exit(1)  # Probabilmente sys.exit(1) è inutile

# # Bonus Loop
# print([math.log(float(sys.argv[x])) if (float(sys.argv[x])>0) else "Error" for x in range(1 , len(sys.argv))])
    