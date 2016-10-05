def grade():
    print "Scores and Grades"
    for i in range(0, 10):
        scores = input('Enter your grade:')
        if scores >= 60 and scores <= 69:
            print "Score", scores, "Your grade is a D"
        elif scores >= 70 and scores <= 79:
            print "Score", scores, "Your grade is a C"
        elif scores >= 80 and scores <= 89:
            print "Score", scores, "Your grade is a B"
        elif scores >= 90 and scores <= 100:
            print "Score", scores, "Your grade is a A"
        else:
            print "You failed"
    print "End of the program. Bye!"

grade()
