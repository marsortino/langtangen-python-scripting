#!/usr/bin/env python
import math
import sys

r = float(sys.argv[1])
s = math.sin(r)
#print("Hello, World! sin(" + str(r) + ")=" + str(s))
print("Hello, World! sin(%(r)g)=%(s)12.5e" % vars())