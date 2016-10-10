import random

def rannumber():
    values=[]
    for count in range (1,101):
        values.append(random.randint(1,10000));
    return values
values= rannumber()

def insertion(values):
    for index in range(0,len(values)):
        for index2 in range(index,0,-1):
            if values[index2]<values[index2-1]:
                values[index2],values[index2-1]=values[index2-1],values[index2]
    return values
insertion(values)
