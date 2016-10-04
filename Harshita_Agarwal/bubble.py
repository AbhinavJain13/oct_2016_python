def bub_sort(arr):
    for i in range(1,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,1,3,7,2,4,1,4]
res=bub_sort(arr)
print(res)
