x = [2,3,1,4]
def SelectionSort(a):
    for i in range (len(a)):
		minIndex = i
		for j in range (i+1, len(a)):
			if a[j] < a[minIndex]:
				minIndex = j
		if minIndex != i:
			a[i], a[minIndex] = a[minIndex], a[i]
    print a

SelectionSort(x)
