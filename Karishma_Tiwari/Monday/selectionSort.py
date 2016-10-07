def selectionSort(arr):

    for i in range(0,len(arr)):
        min =i;
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min = j;
        arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [50,32,2,77,25]
result = selectionSort(arr)
print result
