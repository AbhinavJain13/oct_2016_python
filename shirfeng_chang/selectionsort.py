from random import randint
import datetime

#Create Array of 100 numbers from 0 to 10000.  Output display.
array = []
for i in range(100):
    array.append(randint(0,10000))

print array

def selection(x):
    start = datetime.datetime.now()
    #outIndex loop to end
    for outIndex in range(len(x)):
        low = outIndex
        #Finding min
        for inIndex in range(outIndex,len(x)):
            if x[inIndex] < x[low]:
                low = inIndex

        temp = x[low]
        x[low] = x[outIndex]
        x[outIndex] = temp
    end = datetime.datetime.now()
    print x
    print end - start
selection(array)
