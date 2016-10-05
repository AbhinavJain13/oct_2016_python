def grades():
    for num in range(1, 10):
        score = input('What is your score: ')
        grade = getGrade(int(score))
        print("Score: {}; Your grade is {}".format(score, grade))



def getGrade(score):
    if score >= 90:
        return "A"
    elif score < 90 and score >= 80:
        return "B"
    elif score < 80 and score >= 70:
        return "C"
    else:
        return "D"

grades()
