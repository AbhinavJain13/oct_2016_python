class MathDojo(object):
    def __init__(self=0):
        self = 0
    def add(self, num1, *restOfNums):
        self = num1
        for num in restOfNums:
            self += num
        return self


MathDojo().add(1).result
