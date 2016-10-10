def insertionSort(alist):

   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [3,4,5,6,8,5,3,5,3,5,6,4,3,2,4,87,54,23,12,4365,76453,3232,5445,2332]
insertionSort(alist)
print(alist)
