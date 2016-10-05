def inse_sort(arr):
    for i in range(0,len(arr)-1):
        for j in range(i+1,0,-1):
            if arr[j-1] > arr[j]:
                (arr[j-1],arr[j])=(arr[j],arr[j-1])
    return arr
arr=[2,1,3,7,2,4,1,4]
res=inse_sort(arr)
print res
