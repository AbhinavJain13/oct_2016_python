from random import randint
mylst=[]
for r in range(100):
    mylst.append(randint(0,10000))

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst
print (bubble_sort(mylst))
