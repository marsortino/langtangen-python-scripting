# Write a function myjoin that concatenates a list of strings to a single
# string, with a specified delimiter between the list elements. That is
# is supposed to be an implementation of string object’s join function (or
# string.join) in terms of basic string operations.

#!/usr/bin/env python

def myjoin(delimiter, *arg):
    # UnitedString = [str + delimiter for str in arg]
    UnitedString = ''
    for str in arg:
        UnitedString += ' '+ str + delimiter
    UnitedString = UnitedString[1:-1]
    return UnitedString

test = myjoin(" ", "ciao", "si", "prova", "bla")
print(test)