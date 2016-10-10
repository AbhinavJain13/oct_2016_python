import random
A = random.sample(xrange(10000),100)

def bubblesort(A):
    for i in range(len(A)):
        for k in range( len(A) - 1, i, -1):
            if (A[k] < A[k - 1]):
                temp = A[k]
                A[k] = A[k-1]
                A[k-1] = temp
    print A

bubblesort(A)


# import random
# print random.sample(xrange(10000),100)
