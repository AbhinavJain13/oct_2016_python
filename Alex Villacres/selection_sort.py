import random
from datetime import datetime


start_time = datetime.now()

arr = []
for count in range(1, 101):
    arr.append(random.randint(1,10000))

def selection(x):
    for i in range(0, len(x) - 1):
        mini = i
        for j in range(i, len(x)):
            if x[j] < x[mini]:
                mini = j
        if mini != i:
            x[i], x[mini] = x[mini], x[i]
    print x
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

selection(arr)
