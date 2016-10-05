
'''
1-prints all the odd numbers from 1 to 1000.
Use the for loop and don't use array to do this exercise.


2-prints all the multiples of 5 from 5 to 1,000,000.
'''
#1
for x in range(1,1000,2):
    print "loop - ",x

#2
for x in range(5,1000,5):
    if x%5==0:
        print "loop - ",x
