from random import randint
import datetime

#Create Array of 100 numbers from 0 to 10000.  Output display.
array = []
for i in range(100):
    array.append(randint(0,10000))

print array

#Sort function
def bubble(x):
    start = datetime.datetime.now()
    for i in range(len(x)):
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                temp = x[i]
                x[i] = x[i+1]
                x[i+1] = temp
    end = datetime.datetime.now()
    print x
    print end - start

bubble(array)
