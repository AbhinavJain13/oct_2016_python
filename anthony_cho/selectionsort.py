def selection_sort(arr):
    currIndex, minIndex = 0, 0
    while currIndex < len(arr):
        for num in range(currIndex, len(arr)):
            if arr[num] < arr[minIndex]:
                minIndex = num
        arr[currIndex], arr[minIndex] = arr[minIndex], arr[currIndex]
        currIndex += 1
        minIndex = currIndex
    print arr

selection_sort([72, 42, 50, 88, 85, 5, 51, 44, 87, 22, 15, 41, 89, 21, 39, 1, 94, 79, 9, 35, 4, 80, 69, 90, 48, 66, 13, 82, 26, 64, 16, 12, 40, 67, 33, 96, 58, 53, 77, 8, 75, 68, 61, 93, 84, 7, 81, 74, 97, 11, 47, 62, 54, 2, 63, 18, 38, 99, 19, 36, 45, 6, 24, 25, 55, 73, 49, 10, 23, 60, 29, 37, 86, 71, 52, 31, 98, 91, 3, 95, 83, 100, 17, 43, 57, 59, 46, 56, 27, 76, 32, 70, 14, 28, 78, 30, 92, 65, 20, 34])
