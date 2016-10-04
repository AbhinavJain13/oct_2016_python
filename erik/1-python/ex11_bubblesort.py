
import datetime
import time

data = [9,8,2,7,4,3,6,1];
def bubbleicious(ary):
    #set start time
    startTime = time.time()
    aLength =  len(ary)
    runTimes = aLength -1
    count = 0 # track how many times we have a no swap in a row
    i = 0
    x = 0
    temp = 0
    #while i in range(0,runTimes) and count != runTimes:
    while x in range(0,runTimes):
        while i in range(0,runTimes) and count != runTimes:
            print "i",i
            print "ary[i]",ary[i]
            if ary[i] > ary[i+1]:
                print ary[i],ary[i+1]
                #do the swap
                temp = ary[i+1]
                ary[i+1] = ary[i]
                ary[i] = temp
                count = 0 # reset the tracking counter
                i = i+1
                print ary
            else:
                count +=1 # increment count for each NO swap
                i+=1
        i=0
        x+=1
    # set endtime
    endTime = time.time()
    print "time elapsed: ",endTime-startTime
    return ary
print (bubbleicious(data))
