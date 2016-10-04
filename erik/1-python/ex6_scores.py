'''
Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A
'''

def grades():
    i=0
    while i in range(0,10):
        print "Enter a grade: "
        grade = int(raw_input())
        # print type(grade)
        if grade >=90 and grade<=100:
            print "Grade A"
        elif grade >=80 and grade<=89:
            print "Grade B"
        elif grade >=70 and grade<=79:
            print "Grade C"
        elif grade >=60 and grade<=69:
            print "Grade D"
        else:
            print "You flunked!"
        i += 1
    print 'end of the program'
grades()
