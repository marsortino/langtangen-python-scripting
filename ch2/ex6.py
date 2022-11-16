# Modify the datatrans1.py script such that it reads a stream of (x, y) pairs
# from the command line and writes the modified pairs (x, f(y)) to a file. The
# usage of the new script, here called datatrans1b.py, should be like this:
# python datatrans1b.py tmp.out 1.1 3 2.6 8.3 7 -0.1675
# resulting in an output file tmp.out:
# 1.1 1.20983e+01
# 2.6 9.78918e+00
# 7 0.00000e+00
# Hint: Run through the sys.argv array in a for loop and use the range function
# with appropriate start index and increment.

#!/usr/bin/env python

import sys
import math
import numpy


def myfunc(y):
    if y >= 0.0:
        return y**5.0*math.exp(-y)
    else:
        return 0.0
        
lenght = len(sys.argv)

try:
    lenght > 2 and (lenght % 2) == 0
except:
    print("Usage:", sys.argv[0], "outfile x1value y1value x2value y2value ..."); sys.exit(1)

outfilename = sys.argv[1]
ofile = open(outfilename, 'w')

i = 2
for i in range(2, lenght, 2):
    x = float(sys.argv[i])
    fy = myfunc(float(sys.argv[i+1]))
    
    ofile.write("%g %12.5e\n" % (x, fy))
