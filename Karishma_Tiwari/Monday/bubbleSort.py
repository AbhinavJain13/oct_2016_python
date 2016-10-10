def bubbleSort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            if arr[j]>arr[j+1]:
                (arr[j], arr[j+1])= (arr[j+1], arr[j])


    return arr

arr = [6,5,3,1,8,7,2,4]
result = bubbleSort(arr)
print result
