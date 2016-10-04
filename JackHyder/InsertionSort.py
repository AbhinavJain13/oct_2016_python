x = [2,3,1,4,5,9,7]
def InsertionSort(a):
    for b in range(1,len(a)):
        c=b
        while c>0 and a[c]<a[c-1]:
            a[c], a[c-1]=a[c-1], a[c]
            c=c-1
    print a

InsertionSort(x)
