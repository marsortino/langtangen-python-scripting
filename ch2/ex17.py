# Read the excel_data.csv file
# and print out the row list to see how the data are represented in Python.
# Then extract the data in the columns in separate lists, subtract the model1
# and measurements data to form a new list, say errors. We want to write a
# new file in the CSV format containing the x and errors data in the first two
# columns of a spreadsheet

# The text suggested to use 'csv' as module which is quite archaic. A more modern approach would be to use 'pandas'.

#!/usr/bin/env python
import csv

# read csv

f_csv_old = open('excel_data.csv', 'r') 
reader = csv.reader(f_csv_old, delimiter=',') 

i = 0
x = []
errors = []

for row in reader:
    i += 1
    if i >= 7:
        x_value = float(row[0])
        model1 = float(row[1])
        measurements = float(row[4])
        model1_measurements = model1 - measurements

        x.append(x_value)
        errors.append(model1_measurements)

# write new csv with x and errors in the first two columns

rows = []
for i in range(len(x)):
    rows.append([x[i], errors[i]])

f_csv_new = open('excel_data_new.csv', 'w', newline = '') 
writer = csv.writer(f_csv_new)
writer.writerows(rows)

f_csv_old.close(); f_csv_new.close()
