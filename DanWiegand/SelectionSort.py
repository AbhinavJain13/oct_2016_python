a = [12,5,3,8,2,7,345,6,3]
def selectSort(a):
    for i in range (0, len(a)-1):
        minI = i
        for j in range (i+1, len(a)):
            if a[j] < a[minI]:
                minI = j
                a[i], a[minI] = a[minI], a[i]

selectSort(a)
print a
