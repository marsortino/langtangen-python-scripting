# You pay 1 unit of money and are allowed to throw four dice. 
# If the sum of the eyes on the dice is less than 9,
# you win 10 units of money, otherwise you loose your investment. 
# Should you play this game?
# Hint: Use the simulation method from Exercise 2.9.

#!/usr/bin/env python
import random, sys

try:
    money = int(sys.argv[1])
except:
    sys.stderr.write("Usage:" + sys.argv[0] + "money"); sys.exit(1)

p = 0
n = float(money)
while money > 0:
    sum = 0
    for i in range(0,4):
       a = random.randint(1, 6)
       sum = sum + a
    if sum < 9: p += 1
    money -= 1
#     if sum < 9:
#         p += 10
#     else:
#         p -= 1
#         if p == 0: print("Soldi finiti."); sys.exit(1)

print(p/n) # final result is 0.05, so on average we lose 0.5 unit of money per game