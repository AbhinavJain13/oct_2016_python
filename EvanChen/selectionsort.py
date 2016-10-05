def selectionSort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j]<arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
        print arr
    return arr


a= [10,9,8,7,6,1,2,3,4,5]
b = selectionSort(a)
print b
