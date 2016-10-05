def sel_sort(arr):
    for i in range(0,len(arr)-1):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        (arr[i],arr[min])=(arr[min],arr[i])
        print arr
    return arr
arr=[2,1,3,7,2,4,1,4]
res=sel_sort(arr)
print res
