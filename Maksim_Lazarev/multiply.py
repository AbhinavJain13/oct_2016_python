def multiply(a,b):
    c=[]
    for i in a:
        c.insert(i, i*b)
    return c
a=[2,4,10,16]
print (multiply(a, 5))
