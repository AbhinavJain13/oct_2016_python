import random
def sample(x):
    arr=[]
    for y in range (0,100):
        arr.append(random.randint(1,10000))
    return arr

arr=sample(100)
arr2=[]
for n in range(0,len(arr)):
    mini=arr[n]
    maxi=arr[n]
    count=0
    for i in arr:
        if mini<i:
            mini=arr[n]
            arr[n]=arr[count]
            arr[count]=mini
        count+=1

print arr
