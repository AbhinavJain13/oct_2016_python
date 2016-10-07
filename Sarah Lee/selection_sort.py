
# def selectionsort(A):
#     for i in range(len(A)-1, 0, -1):
#         max_found = 0
#         for k in range(0, len(A)-1, +1):
#             if (A[k] > (A[max_found])):
#                 max_found = k
#             A[i], A[max_found] = A[max_found], A[i]
#     print A
# selectionsort([3,2,1,9,4])
#



def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

def selectionsort( aList ):
  for i in range( len( aList ) ):
    least = i
    for k in range( i + 1 , len( aList ) ):
      if aList[k] < aList[least]:
        least = k
    swap( aList, least, i )

    print aList

selectionsort([1,5,8,2,4])
