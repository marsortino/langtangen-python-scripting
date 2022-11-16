# The following code contains five errors. Find them!

# #!/usr/bin/ env python
# import sys, random
# def compute(n):
# i = 0; s = 0
# while i <= n:
# s += random.random()
# i += 1
# return s/n
# n = sys.argv[1]
# print ’average of %d random numbers is %g" % (n, compute(n))

#!/usr/bin/env python       # error: there was a space before env
import sys, random

n = int(sys.argv[1]) # error: line position, cast missing 

def compute(n):
    i = 0; s =0
    while i <= n:
        s += random.random()
        i += 1 # error: indentation
    return s/n

print("average of %d random numbers is %g" % (n, compute(n))) # error: wrong use of '"
