# Extend the datatrans1.py script such that you can read a file with an
# arbitrary number of columns of real numbers. Find the average of the numbers
# on each line and write to a new file the original columns plus a final column
# with the averages. All numbers in the output file should have the format
# 12.6f.

#!/usr/bin/env python
import sys, math, numpy

try:
    infilename = sys.argv[1]; outfilename = sys.argv[2]
except (IndexError):
    sys.stderr.write("Usage:" + sys.argv[0] + "infilename outfilename")

ifile = open( infilename, 'r')
ofile = open(outfilename, 'w')

x = []

for line in ifile:
    columns = line.split()
    lenght = len(columns)
    avg = 0
    for i in range(0, lenght):
        columns[i] = float(columns[i])
        avg = avg + columns[i]
        ofile.write("%12.6f" % columns[i]) 
    avg = avg / (i+1)
    ofile.write("%12.6f\n" % (avg))    
    print(avg)

ifile.close(); ofile.close()