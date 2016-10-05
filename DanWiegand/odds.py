def oddEven():
    for count in range(1, 2001):
        if(count % 2 == 0):
            print "Number is {}. This is an Even Number".format(count)
        else:
            print "Number is {}. This is an Odd Number".format(count)
print oddEven()
