#!/usr/bin/env python
import sys, math, string
usage = 'Usage: %s infile' % sys.argv[0]

try:
    infilename = sys.argv[1]
except:
    print(usage); sys.exit(1)

# loads file into a list of lines
f = open(infilename, 'r'); lines = f.readlines(); f.close()

# the second line contains the increment in t
dt = float(lines[1])

# the third line contains the name of the time series:
ynames = lines[2].split()

# store y data in a dictionary of lists of floats
y = {}              # declare empty dictionary
for name in ynames:
    y[name] = []    # empty list (of y values of a time series)

# load data form the rest of the lines:
for line in lines[3:]:
    yvalues = [float(x) for x in line.split()]
    if len(yvalues) == 0: continue # skip blank lines
    i = 0 # counter for yvalues
    for name in ynames:
        y[name].append(yvalues[i]); i += 1
    # a nicer syntax of the above loop is:
    # for name, yvalue in zip(ynames, yvalues):
    #   y[name].append(yvalue)

    for name in y:   # run through all keys in y
        ofile = open(name + '.dat', 'w')
        for k in range(len(y[name])):
            ofile.write('%12g %12.5e\n' % (k*dt, y[name][k]))
        ofile.close