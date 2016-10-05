import random
def sample(x):
    arr=[]
    for y in range (0,100):
        arr.append(random.randint(1,10000))
    return arr

arr=sample(100)

for i in range (1,len(arr)):
    x=arr[i]
    j=i-1
    while j >= 0 and arr[j] > x:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=x

print arr
