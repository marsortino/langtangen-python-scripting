# Write a function taking a program name as argument and returning true
# if the program is found in one of the directories in the PATH environment
# variable and false otherwise. This function is useful for determining whether
# a specific program is available or not. Hint: Read Chapter 3.2.5.

#!/usr/bin/env python

import sys, os

def isthere(program_name):
    if program_name in os.environ:
        print("The program is available.")
        return
    else: print("The program is not available."); return


try:
    program = sys.argv[1]
    isthere(program)
except (IndexError):
    print("Usage: %s program_name" % (sys.argv[0]))

