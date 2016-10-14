def bubbleSort(alist):
    for item in range(len(alist)-1, 0, -1):
        for i in range(item):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        print(alist)

alist = [30,21,33,45,92,3,48,91,56]
bubbleSort(alist)
