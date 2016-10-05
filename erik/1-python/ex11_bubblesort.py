#import datetime
import time
import random
from random import randint

def bubbleicious():
    # generate data // test data = [9,8,2,7,4,3,6,1]
    def generateData():
        ary = []
        i=0
        while i in range(0,100):
            ary.append(randint(0, 10000))
            i+=1
        return ary
    # init
    ary = generateData()
    aLength =  len(ary)
    runTimes = aLength -1
    count = 0 # track how many times we have a 'no swap' in a row
    i = 0
    x = 0
    temp = 0
    # with all set ups complete, start the clock...
    startTime = time.time()
    while x in range(0,runTimes):
        while i in range(0,runTimes) and count != runTimes:
            if ary[i] > ary[i+1]:
                #do the swap
                temp = ary[i+1]
                ary[i+1] = ary[i]
                ary[i] = temp
                count = 0 # reset the tracking counter
                i = i+1
            else:
                count +=1 # increment count for each NO swap
                i+=1
        i=0
        x+=1
    # we have an answer, stop the clock.
    endTime = time.time()
    print "time elapsed: ",endTime-startTime," seconds!"
    return ary

print bubbleicious()
