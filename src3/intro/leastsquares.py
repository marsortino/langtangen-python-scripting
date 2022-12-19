# Scitools is not available for python3. As such, matplotlib has been used.

import sys
try:
    n = int(sys.argv[1])    # no of data points
except:
    n = 20

# from scitools.all import * # import numpy and much of scitools
# however scitools is not available for python3+
# numpy and matplotlib are then used.
from numpy import *
import matplotlib.pyplot as plt

# compute data points in x and y arrays:
# x in (0, 1) and y = -2*x+3+eps, where eps is normally
# distributed with mean zero and st.dev. 0.25.
random.seed(20)
x = linspace(0.0, 1.0, n)
noise = random.normal(0, 0.25, n)
a_exact = -2.0; b_exact = 3.0
y_line = a_exact*x + b_exact
y = y_line + noise

# create least squares system:
A = array([x, zeros(n)+1])
A = A.transpose()
result = linalg.lstsq(A, y)
# result is a 4-tuple, the solution (a, b) is the 1st entry:
a, b = result[0]

# plot:
# original plot code
# plot(x, y, ’o’,
#      x, y_line, ’r’,
#      x, a*x + b, ’b’,
#      legend=(’data points’, ’original line’, ’fitted line’),
#      title=’y = %g*x + %g: fit to y = %g*x + %s + normal noise’ % \
#             (a, b, a_exact, b_exact),
#      hardcopy=’tmp.ps’)

# plot done with matplotlib:
plt.plot(x, y, 'o',
         x, y_line, 'r',
         x, a*x+b, 'b',
         )
plt.axis([0, 1, 1, 3.5])
plt.legend(['data point', 'original line', 'fitted line'])
plt.title('y = %g*x + %g: fit to y = %g*x + %s + normal noise' % \
             (a, b, a_exact, b_exact))
#plt.show()
plt.savefig('tmp.png')