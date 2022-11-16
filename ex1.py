# Write a script that prints a uniformly distributed random number between −1 and 1. 
# The number should be written with four decimals as implied by the %.4f format


#!/usr/bin/env python
import random

a = random.uniform(-1 , 1)
print("A casual number between -1 and 1 is: %.4f" % (a))