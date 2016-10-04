print ("Starting the pkrogram...")
from random import randint
heads=0
tails=0
for i in range(1, 5000):
    if randint(1,2)==1:
        heads+=1
        print ("Attempt # ",i," : Throwing a coin... Its a head! ... Got ",heads," head(s) so far and ",tails," so far")
    else:
        tails+=1
        print ("Attempt # ",i," : Throwing a coin... Its a tail! ... Got ",heads," head(s) so far and ",tails," so far")
