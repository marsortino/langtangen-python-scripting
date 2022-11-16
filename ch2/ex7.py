# Consider the datatrans1.py script with a typo (sys.arg) in the try block:

# try:
#     infilename = sys.arg[1]; outfilename = sys.argv[2]
# except:
#     print "Usage:",sys.argv[0], "infile outfile"; sys.exit(1)

# Run this script and observe that whatever you write as filenames, the script
# aborts with the usage message. The reason is that we test for any exception in
# the except block. We should rather test for specific exceptions, i.e., the type
# of errors that we want to recover from in the try block. In the present case we
# are worried about too few command-line arguments. Read about exceptions
# in Chapter 8.8 and figure out how the except block is to be modified. Run
# the modified script and observe the impact of the typo.
# Extend the script with an appropriate try-except block around the first
# open statement. You should test for a specific exception caused by a non existing input file.
# Finally, it is a good habit to write error messages to standard error
# (sys.stderr) and not standard output (where the print statements go). Make
# the corresponding modifications of the print statements.

#!/usr/bin/env python
import math
import sys

try:
    infilename = sys.argv[1]; outfilename = sys.argv[2]
except (IndexError):
    sys.stderr.write("Usage:" + sys.argv[0] + " infile outfile"); sys.exit(1)
ifile = open( infilename, 'r')  # open file for reading
ofile = open(outfilename, 'w')  # open file for writing

def myfunc(y) :
    if y >= 0.0:
        return y**5*math.exp(-y)
    else:
        return 0.0
    #return (y**5*math.exp(-y) if y >= 0 else 0.0)

# read ifile line by line and write out transformed values:
for line in ifile:
    pair = line.split()
    x = float(pair[0]); y = float(pair[1])
    fy = myfunc(y) # transform y value
    ofile.write('%g %12.5e\n' % (x,fy))
ifile.close(); ofile.close()