def bubblesort(x):
    for sorter in range(len(x)-1,0,-1):
        for num in range(sorter):
            if x[num]>x[num+1]:
                temp = x[num]
                x[num] = x[num+1]
                x[num+1] = temp

x = [2,5,4,5,3,5,6,4,3,23,43,54,63,34,54,65,76,89,32,3,4,1,1,3,4]
bubblesort(x)
print(x)
