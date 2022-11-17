# Write a script inverseconvert1.py that performs the “inverse process” of
# convert1.py (or convert2.py). For example, if we first apply convert1.py to
# the specific test file .convert_infile1 in src/py/intro, which looks like
# some comment line
# 1.5
#   tmp-measurements tmp-model1 tmp-model2
#       0.0 0.1 1.0
#       0.1 0.1 0.188
#       0.2 0.2 0.25
# we get three two-column files tmp-measurements.dat, tmp-model1.dat, and tmp-model2.dat. 
# Running
# python inverseconvert1.py outfile 1.5 \
#       tmp-measurements.dat tmp-model1.dat tmp-model2.dat
# should in this case create a file outfile, almost identical to .convert_infile1;
# only the first line should differ (inverseconvert1.py can write anything on
# the first line). For simplicity, we give the time step parameter explicitly as a
# command-line argument (it could also be found from the data in the files).
# Hint: When parsing the command-line arguments, one needs to extract the
# name model1 from a filename model1.dat stored in a string (say) s. This can be done by s[:-4]


# Note: da sistemare, la spaziatura e il formato finale non sono corretti 

#!/usr/bin/env python

import sys, math, string

usage = 'Usage: %s outfile dt tmp-measurements.dat tmp-model1.dat tmp-model2.dat' % sys.argv[0]

inputfile = []
ifile = []

try:
    outfilename = sys.argv[1]
    dt = sys.argv[2]
    for nfiles in range(0, 3): 
        inputfile.append(sys.argv[nfiles+3])
except (IndexError):
    sys.stderr.write(usage); sys.exit(1)

nfiles += 1
dt = float(dt)

row = {}

for i in range(0, nfiles):
    ifile = open(inputfile[i], 'r'); lines = ifile.readlines(); ifile.close()
    row[i] = []
    for line in lines:
        pair = line.split()
        value = pair[1]
        row[i].append(value)

ofile = open(outfilename, 'w') ; ofile.write('some comment line\n%g\n  ' % dt)
ofile.write('   %s %s  %s\n' % (inputfile[0][:-4], inputfile[1][:-4], inputfile[2][:-4]))
for i in range(0, nfiles):
    ofile.write('       %s  %s  %s\n' % (row[i][0], row[i][1], row[i][2]))
ofile.close()