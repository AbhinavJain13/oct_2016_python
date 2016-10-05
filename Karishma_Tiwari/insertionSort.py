
#using while loop
def insertionSort(arr):
    for i in range(0,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]= arr[j], arr[j-1]
            j-=1
    return arr



# using for loop
def insertionSort(arr):
    for i in range(0, len(arr)):
        for j in range (i, 0, -1):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j]= arr[j], arr[j-1]
            else:
                 break
    return arr

result = insertionSort([2,1,9,8,13,10,5])
print result
