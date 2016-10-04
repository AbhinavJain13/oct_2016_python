import datetime
from datetime import timedelta
import random



def rannumber():

    values=[]

    for count in range (1,101):
        values.append(random.randint(1,10000));
    return values
values= rannumber()



def bubble_sort(list):
    start= datetime.datetime.now()

    for index in range(1,len(list)):
        for index in range(1,len(list)):
            if list[index]<list[index-1]:
                temp=list[index-1]
                list[index-1]=list[index]
                list[index]=temp
    print list
    end = datetime.datetime.now()
    print "It took",(end.microsecond-start.microsecond), "microseconds!"

bubble_sort(values)
