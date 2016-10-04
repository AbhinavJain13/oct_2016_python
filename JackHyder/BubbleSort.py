x = [1,3,4,2]
def BubbleSort(a):
    for b in range(len(a)):
        for c in range(b+1, len(a)):
            if a[b]>a[c]:
                a[c], a[b] = a[b], a[c]
    print a

BubbleSort(x)
