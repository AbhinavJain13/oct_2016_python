def print_odd():
    for count in range(1, 101):
    if count % 2 !=0:
        print count
def print_mult():
    for count in range(5, 1000005):
    if count % 5 ==0:
        print count
def printsum():
    for count in range([]):
        if count % 5 ==0:
        print count
def printavg():
    a = [1, 2, 5 ,10, 255, 3]
    b = sum(a)
    c = len(a)
    avg = float(b/c)
    print avg
def oddneven():
    for count in range(1,2001):
        if count % 2 ==0:
            print "This is an even number"
        elif count % 2 !=0:
            print "This is an odd number"
def multiples(x):
    return x * 5
 multiples([2,4,10,16])

def grade(num):
    print "Scores and Grades"
    for x in range(num):
        score = input("Enter score: ")
        if score > 100 or score < 0:
            print "Please enter score between 0 and 100"
        else:
            if score <= 59:
                grade = "F"
            elif score >= 60 and score <= 69:
                grade = "D"
            elif score >= 70 and score <= 79:
                grade = "C"
            elif score >= 80 and score <= 89:
                grade = "B"
            elif score >= 90:
                grade = "A"
            print "Score:", str(score) + "; Your grade is ",grade
    print "End of program. Bye!"

x = [4,6,1,3,5,7,25]
    def draw_stars(arr):
       for i in range (len(arr)):
           arr[i] *= "*"
           print arr[i]
    draw_stars(x)
