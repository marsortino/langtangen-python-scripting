# Perl’s join function can join an arbitrary composition of strings and lists
# of strings. The purpose of this exercise is to write a similar function in Python

#!/usr/bin/env python

def myjoin2(delimiter, *arg):
    UnitedString = ""
    for elem in arg:
        if isinstance(elem, str):
            UnitedString += elem + delimiter
            # print("Ho trovato una stringa. " + UnitedString)
        elif isinstance(elem, list):
            UnitedString = UnitedString + delimiter.join(elem) + delimiter
            # print("Ho trovato una lista " + UnitedString)
        elif isinstance(elem, tuple):
            UnitedString = UnitedString + delimiter.join(elem) + delimiter
            # print("Ho trovato una tupla. " + UnitedString)
        else:
            print("Non ho trovato niente")
    print(UnitedString)
    return UnitedString[:-1]

list1 = ['s1', 's2', 's3']
tuple1 = ('s4', 's5')
ex1 = myjoin2(',', 't1', 't2', list1, tuple1, 't3', 't4')
print(ex1)