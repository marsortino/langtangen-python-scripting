# Consider the following initialization of a string, two integers, and a floating-point variable:
# name = ’myfile.tmp’; i = 47; s1 = 1.2; s2 = -1.987;
# Write the string in a field of width 15 characters, and adjusted to the left;
# write the i variable in a field of width 5 characters, and adjusted to the
# right; write s1 as compactly as possible in scientific notation; and write s2 in
# decimal notation in a field of minimum width

#!/usr/bin/env python

name = 'myfile.tmp'; i = 47; s1 = 1.2; s2 = -1.987;

print("%-15s" % (name))
print("%5d" % (i))
print("%.1e" % (s1))
print("%4.3f" % (s2))