def insertionSort(arr):
    for i in range(0, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j = j-1
        print arr
    return arr

a= [10,9,8,7,6,1,2,3,4,5]
b = insertionSort(a)
print b
