# Write a code segment that removes all elements larger than 2 in the list
# [3,4,2,1], but use a while loop and an index that is correctly updated in
# each pass in the loop.
# The same problem appears also with other list modification functions,
# such as del, e.g.,
#   list = [3,4,2,1]
#   for item in list:
#       del list[0]
# Explain why the list is not empty (print list and item inside the loop if you
# are uncertain). Construct a new loop where del list[0] successfully deletes
# all list items, one by one

#!/usr/bin/env python

lista = [3,4,2,1]

i = 0
while i < len(lista):
    if lista[i] > 2:
        lista.remove(lista[i])
        i -= 1
    i += 1
print(lista)

lista2 = [3,4,2,1]

for item in lista2[:]:
    del lista2[0]
    print(lista2)