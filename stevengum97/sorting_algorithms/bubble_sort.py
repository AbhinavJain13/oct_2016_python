import datetime
t = datetime.time(1,2,3)

def bubble_sort(arr):
    print "This is the arr before sorting: "
    print arr
    i = 0
    start = datetime.datetime.now()
    for i in range(len(arr)):
        for i in range(len(arr)):
            if i <= len(arr)-2:
                if arr[i+1] < arr[i]:
                    temp = arr[i]
                    arr[i] = arr[i+1]
                    arr[i+1] = temp
    print arr
    end = datetime.datetime.now()
    #print "Start:  ", start
    #print "End:   ", end
    print  "Time to sort:  ", end - start

a = [1,2,3,8,5,9,6,10,7]

bubble_sort(a)

#created using https://www.random.org/integer-sets/
b = [3162, 8301, 2220, 8455, 6446, 1199, 1788, 7527, 3284, 1326, 3223, 5909, 2822, 2853, 2679, 2044, 108, 4975, 6283, 4782, 4739, 8588, 3989, 7460, 8003, 9673, 8817, 2252, 3406, 834, 8475, 1988, 4868, 6839, 3850, 1783, 6022, 8063, 5809, 610, 4557, 7559, 6201, 3592, 3312, 4934, 5226, 5418, 9695, 6797, 1956, 2811, 750, 9313, 6320, 4686, 2384, 627, 5449, 9794, 5562, 7824, 7165, 1308, 7236, 5640, 9417, 1073, 9046, 2975, 1301, 8696, 3281, 9389, 6440, 6075, 7475, 6101, 2511, 9074, 9850, 1512, 6566, 4744, 7870, 9877, 1570, 4834, 6383, 8502, 7315, 3301, 6158, 6964, 2623, 7480, 6877, 316, 436, 2584]

bubble_sort(b)
