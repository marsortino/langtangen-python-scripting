# Consider the following script:
#   from numpy import linspace
#   x = linspace(0, 1, 3)
#   # y = 2*x + 1:
#   y = x; y *= 2; y += 1
#   # z = 4*x - 4:
#   z = x; z *= 4; z -= 4
#   print x, y, z
# Explain why x, y, and z have the same values. How can the script be changed
# such that y and z get the intended values?

#!/usr/bin/env python

from numpy import linspace

x = linspace(0, 1, 3)
# y = 2*x + 1
y = x; y *= 2; y +=1
# z = 4*x -4
z = x; z *= 4; z -= 4
print(x, y, z)

# # Explain why x, y, and z have the same values.
# Because y and z point to the same array x. Thus in reality we are changing x. A fix would be:

x = linspace(0, 1, 3)
y = x.copy(); y *= 2; y +=1
z = x.copy(); z *= 4; z -= 4
print(x, y, z)