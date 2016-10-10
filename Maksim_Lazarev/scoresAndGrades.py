def grade(num):
    if 60<num<69:
        return "D"
    elif 70<num<79:
        return "C"
    elif 80<num<89:
        return "B"
    else:
        return "A"

print ("Scores and Grades")
from random import randint
for i in range(1, 10):
    num=randint(60,100)
    print ("Score:", num, "Your Grade is ", grade(num), sep='')
print ("End of the program. Bye!")
