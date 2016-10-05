import random
def sample(x):
    arr=[]
    for y in range (0,100):
        arr.append(random.randint(1,100))
    return arr

def bubbleSort(arr):
    for i in range (0,100):
        print "Run #",i
        if arr==sorted(arr):
            print arr
            return arr
        count=0
        breaks=len(arr)
        for element in arr:
            if count==breaks-1:
                break
            if element>arr[count+1]:
                temp=element
                arr[count]=arr[count+1]
                arr[count+1]=temp

            count=count+1

bubbleSort(sample(100))
