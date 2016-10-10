
def selectSort(arr):
    for i in range(len(arr)):
        min = i
        temp = arr[i]
        for j in range( i+1, len(arr)):
            if(arr[j]<arr[min]):
                min = j
        arr[i] = arr[min]
        arr[min]=temp
    return arr

# print(selectSort([54,26,93,17,77,31,44,55,20]))
