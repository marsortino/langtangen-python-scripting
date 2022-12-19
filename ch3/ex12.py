# Computer work often involves a lot of temporary files, i.e., files that you
# need for a while, but that can be cleaned up after some days. If you let the
# name of all such temporary files contain the stem tmp, you can now and then
# run a clean-up script that removes the files. Write a script that takes the
# name of a directory tree as command-line argument and then removes all
# files (in this tree) whose names contain the string tmp.
# Hint: Use os.path.walk to traverse the directory tree (see Chapter 3.4.7)
# and look up Chapter 3.2.8 to see how one can test if a string contains the
# substring tmp. Avoid giving the script a name containing tmp as the script
# may then remove itself! Also remember to test the script thoroughly, with
# the physical removal statement replaced by some output message, before you
# try it on a directory tree.

#!/usr/bin/env python

import sys, os

try:
    dir_name = sys.argv[1]
except (IndexError):
    sys.stderr.write("Usage: ", sys.argv[0], 'directoryname')

