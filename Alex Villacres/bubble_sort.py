import random

arr = []
for count in range(1, 101):
    arr.append(random.randint(1,10000))

def bubble(my_list):
    for i in range(len(my_list)):
        for i in range(len(my_list)-1):
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
            print my_list
        print 'break'
    print "Final Answer", my_list

bubble(arr)
