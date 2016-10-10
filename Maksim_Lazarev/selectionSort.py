from random import randint
mylst=[]
for r in range(100):
    mylst.append(randint(0,10000))

def selection_sort(lst):
    for i in range(len(lst)):
        for v in range (i+1, len(lst)):
            if lst[v]<lst[i]:
                lst[v],lst[i]=lst[i],lst[v]
    return lst
print (selection_sort(mylst))
