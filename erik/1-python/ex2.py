#Create a program that prints the sum of all the values in the list:

'''
a = [1, 2, 5, 10, 255, 3]
sum = 0
count = 0

while count < len(a):
    sum = sum+a[count]
    # print a
    count +=1

print sum
'''


#  Better method

a = [1, 2, 5, 10, 255, 3]
sum = 0

for val in a:
    sum += val
print sum
