#!/usr/bin/env python
import math
import sys

try:
    infilename = sys.argv[1] ; outfilename = sys.argv[2]
except:
    print("Usage:", sys.argv[0], "infilename outfilename"); sys.exit(1)

x = []; y = []

from numpy import * 
x = array(x); y = array(y) # convert lists to efficient arrays

import scitools.filetable
f = open(infilename, 'r')
x, y = scitools.filetable.read_columns(f)
f.close()

x = 10*x
y = 2*y + 0.1*sin(x)
    
f = open(outfilename, 'w')
scitools.filetable.write_columns(f, x, y)
f.close()
