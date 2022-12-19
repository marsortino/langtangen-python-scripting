# Write a function findprograms taking a list of program names
# as input and returning a dictionary with the program names as keys and the
# programs’ complete paths on the current computer system as values. Search
# the directories in the PATH environment variable as indicated in Exericise 3.6.
# Allow a list of additional directories to search in as an optional argument to
# the function. Programs that are not found should have the value None in the
# returned dictionary.
# Here is an illustrative example of using findprograms to test for the existence of some utilities used in this book:
#   programs = {
#       ’gnuplot’ : ’plotting program’,
#       3.2. Variables of Different Types 109
#       ’gs’ : ’ghostscript, ps/pdf converter and previewer’,
#       ’f2py’ : ’generator for Python interfaces to Fortran’,
#       ’swig’ : ’generator for Python interfaces to C/C++’,
#       ’convert’ : ’image conversion, part of the ImageMagick package’,
#        }
#   installed = findprograms(programs.keys())
#   for program in installed:
#       if installed[program]:
#           print ’You have %s (%s)’ % (program, programs[program])
#       else:
#           print ’*** Program’, program, ’was not found’
#           print ’ .....(%s)’ % programs[program]

#!/usr/bin/env python

import os

def findprograms(*arg):
    path_programs = {}
    for keys in arg[0]:
        print('provo a cercare ', keys)
        if keys in os.environ:
            path_programs[keys] = os.environ.get(str(keys))
            print("ho trovato qualcosa")
        else:
            path_programs[keys] = None  # non funziona
    return path_programs


programs = {
    'python': 'programming',
    'gnuplot': 'plotting program',
    'gs' : 'ghostscript, ps/pdf converter and previewer',
    'f2py' : 'generator for Python interfaces to Fortran',
    'swig' : 'generator for Python interfaces to C/C++',
    'convert' : 'image conversion, part of the ImageMagick package',
    }
programs_keys = list(programs.keys())
installed = findprograms(programs_keys)
for program in installed:
    if installed[program]:
        print('You have %s (%s)' % (program, programs[program]))
    else:
        print('*** Program', program, 'was not found')
        print(' .....(%s)' % programs[program])
