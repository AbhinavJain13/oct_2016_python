import random
from random import randint
#print randint(0,1)
#i if i < x else x
sumhead = 0
sumtail = 0
for i in range (0,5000):
    if (randint(0,1) == 1): sumhead = sumhead + 1
    else: sumtail = sumtail + 1
    print "Heads: ",sumhead," Tails: ",sumtail
print "TOTALS! Heads: ",sumhead," Tails: ",sumtail
