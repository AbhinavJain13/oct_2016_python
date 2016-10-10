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
            print "Score:", str(score) + "; Your grade is",grade
    print "End of program. Bye!"
