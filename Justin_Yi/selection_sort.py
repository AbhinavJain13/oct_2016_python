def selectionSort(sort):
    for num in range(0, len(sort)-1,1):
        minimum = 0
        for i in range(num):
            if sort[i] > sort[minimum]:
                minimum = i
        temp = sort[num]
        sort[num] = sort[minimum]
        sort[minimum] = temp
        print sort


sort = [1,4,0,2,3,6]
selectionSort(sort)
