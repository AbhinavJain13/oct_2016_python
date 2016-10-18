from random import randint
mylst=[]
for r in range(100):
    mylst.append(randint(0,10000))

def insertion_sort(lst):
    for i in range(1,len(lst)):
        # v=i-1
        while i-1>=0:
            if lst[i]<lst[i-1]:
                lst[i],lst[i-1]=lst[i-1],lst[i]
                i-=1
            else:
                break
    return lst
print (insertion_sort(mylst))
