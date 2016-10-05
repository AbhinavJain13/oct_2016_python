from random import randint
import datetime

#Create Array of 100 numbers from 0 to 10000.  Output display.
array = []
for i in range(100):
    array.append(randint(0,10000))

print array

def insertion(x):
    start = datetime.datetime.now()
    for i in range(1,len(x)):
        swap = x[i]
        tmp = i
        while swap < x[tmp-1] and tmp > 0:
            x[i] = x[i-1]
            tmp-=1
        x[tmp] = swap
    end = datetime.datetime.now()
    print x
    print end - start
insertion(array)
