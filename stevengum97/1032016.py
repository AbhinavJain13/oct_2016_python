import random
import string
# don't worry too much about what these two functions are doing, but feel free to discuss them with your team - but you won't be asked to implement anything like them for a while!
def randomString(val):
    letters = string.letters
    return "".join(random.choice(letters) for i in range(val))
def makeRandom():
    return [random.randint(5,45) if random.randint(0,1) else randomString(random.randint(2,7)) for y in range(10) ]

#print makeRandom()

# Assignment: Your team should write a function that takes the results from makeRandom, and then if the element in the list starts with a capital letter print a tuple with the capital letter, and the then word's length.  If the value is a number, print that many @ symbols.  If the element is a string that starts with a lowercase letter, print the string, reversed!
['IwWpAx', 4, 2, 'TYCm', 'mJmtAYm', 'xKpnPcD', 'Gc', 'MKc', 'epub', 'ABxe']
# given the string above your function should output:
"""
(I,7)
@@@@
@@
(T,4)
mYAtmJM
DcPnpKx
(G,2)
(M,3)
bupe
(A,4)
"""



r_list = makeRandom()
print(r_list)

def random_list(arr):
    for i in range(0,len(arr)):
        if type(arr[i]) is str:
            if arr[i][0].isupper() == True:
                print arr[i][0], len(arr[i])
            else:
                print arr[i][::-1]
        elif type(arr[i]) is int:
            print arr[i]*"@"

random_list(r_list)
