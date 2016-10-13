def map(list, func):
    myArr=[]
    for item in list:
        myArr.append(func(item))
    return myArr
print (map([1,2,3,4,5], lambda x: x*2))
