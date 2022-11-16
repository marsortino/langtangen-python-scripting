# Modify the datatrans1.py script such that it reads its numbers 
# from standard input, sys.stdin, and writes the results to standard output, sys.stdout.
# You can work with sys.stdin and sys.stdout as the ordinary file objects you
# already have in datatrans1.py, except that you do not need to open and close them.
#

#!/usr/bin/env python
import math, sys

def myfunc(y):
    if y >= 0.0:
        return y**5.0*math.exp(-y)
    else:
        return 0.0

for lines in sys.stdin:

    try:
        pair = lines.split()
        x = float(pair[0]) ; y = float(pair[1])
    except:
        print("Error! Give me: x y"); sys.exit(1)
    
    
    fy = myfunc(y)
    sys.stdout.write("x = %g y = %g e f(y) = %g\n"% (x, y, fy))