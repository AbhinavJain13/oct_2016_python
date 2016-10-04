def insertSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]
        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr
# print(insertSort([10,7,3,1,9,7,4,3]))
