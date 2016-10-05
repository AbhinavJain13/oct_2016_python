def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swap = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = swap
        print arr
    return arr

a = [10,9,8,7,6,1,2,3,4,5]
b = bubbleSort(a)
print b
