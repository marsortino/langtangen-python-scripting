# Suppose we have a script that performs numerous efficiency tests. The
# output from the script contains lots of information, but our purpose now is
# to extract information about the CPU time of each test and sort these CPU
# times. The output from the tests takes the following form
    # ...
    # f95 -c -O0 versions/main_wIO.f F77WAVE.f
    # f95 -o app -static main_wIO.o F77WAVE.o -lf2c
    # app < input > tmp.out
    # CPU-time: 255.97 f95 -O0 formatted I/O
    # f95 -c -O1 versions/main_wIO.f F77WAVE.f
    # f95 -o app -static main_wIO.o F77WAVE.o -lf2c
    # app < input > tmp.out
    # CPU-time: 252.47 f95 -O1 formatted I/O
    # f95 -c -O2 versions/main_wIO.f F77WAVE.f
    # f95 -o app -static main_wIO.o F77WAVE.o -lf2c
    # app < input > tmp.out
    # CPU-time: 252.40 f95 -O2 formatted I/O
    # ...
# First we need to extract the lines starting with CPU-time. Then we need
# to sort the extracted lines with respect to the CPU time, which is the
# number appearing in the second column. Write a script to accomplish this
# task. A suitable testfile with output from an efficiency test can be found in
# src/misc/efficiency.test.
# Hint: Find all lines with CPU time results by using a string comparison of
# the first 7 characters to detect the keyword CPU-time. Then write a tailored
# sort function for sorting two lines (extract the CPU time from the second
# column in both lines and compare the CPU times as floating-point numbers).

#!/usr/bin/env python

import sys

EfficiencyFile = open('efficiency.test', 'r'); output = EfficiencyFile.readlines(); EfficiencyFile.close()
ListaTempi = []

# # Metodo 1
# for lines in output:
#     if lines[0:8] == 'CPU-time':
#         ListaTempi.append(float(lines[9:16]))

# ListaTempi.sort()
# print(ListaTempi)

# Metodo 2
for lines in output:
    if lines[0:8] == 'CPU-time':
        terms = lines.split()
        ListaTempi.append(float(terms[1]))

ListaTempi.sort()
print(ListaTempi)