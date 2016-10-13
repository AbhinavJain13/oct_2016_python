# class MathDojo(object):
#     def __init__(self):
#         self.result=0
#     def add(self, arg1):
#         self.result+=arg1
#         return self
#     def substract(self, arg1):
#         self.result-=arg1
#         return self
# print (MathDojo().add(2).add(8).substract(3).result)

# md=Mathdojo() <-- THIS IS WHAT IS CALLED A NEW INSTANCE ???
# HOW CAT THE NEW INSTANCE DO THE FOLLOWING TASK:
# MathDojo().add(2).add(2, 5).subtract(3, 2).result ???

class MathDojo(object):
    def __init__(self):
        self.result=0
    def add(self, arg1, arg2=0):
        self.result+=(arg1+arg2)
        return self
    def substract(self, arg1, arg2=0):
        self.result-=(arg1+arg2)
        return self
print (MathDojo().add(2).add(2,5).substract(3,2).result)
