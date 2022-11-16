#!/usr/bin/env python
import sys, math

try:
    infilename = sys.argv[1]; outfilename = sys.argv[2]
except:
    print("Usage:", sys.argv[0], "infile outfile"); sys.exit(1)

ifile = open( infilename, 'r') # open file for reading
ofile = open(outfilename, 'w') # open file for writing

def myfunc(y):
    if y >= 0.0:
        return y**5*math.exp(-y)
    else:
        return 0.0

lines = ifile.readlines()

x = []; y = [] # start with empty lists
for line in lines:
    xval, yval = line.split()
    x.append(float(xval)); y.append(float(yval))

for i in range(0, len(x), 1):
    fy = myfunc(y[i]) # transform y value
    ofile.write('%g %12.5e\n' %(x[i], fy))

ifile.close(); ofile.close()