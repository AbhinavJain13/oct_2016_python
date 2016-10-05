import random
from datetime import datetime

start_time = datetime.now()

arr = []
for count in range(1, 101):
    arr.append(random.randint(1,10000))


def insertion(x):
    for i in range(1, len(x)):
        j = i
        while j > 0 and x[j] < x[j - 1]:
            x[j], x[j-1] = x[j-1], x[j]
            j=j-1
    return x

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

print insertion(arr)
