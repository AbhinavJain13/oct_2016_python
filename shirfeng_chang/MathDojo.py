Part I
class MathDojo(object):
    def __init__(self):
        self.result = 0

    def add(self,x, y=0):
        self.result+=(x+y)
        return self

    def subtract(self,x, y=0):
        self.result-=(x+y)
        return self

print MathDojo().add(2).add(2,5).subtract(3,2).result

Part III
class MathDojo(object):
    def __init__(self):
        self.result = 0
        self.store = 0

    def loop(self,x):
        for index in x:
            if type(index) is int or type(index) is float:
                self.store+=index
            else:
                self.loop(index)
        return self

    def add(self,x):
        self.loop(x)
        self.result+=self.store
        self.store = 0
        return self

    def subtract(self,x):
        self.loop(x)
        self.result-=self.store
        self.store = 0
        return self

print MathDojo().add(([1],3,4)).add(([3, 5, 7, 8], [2, 4.3, 1.25])).subtract((2, [2,3], [1.1, 2.3])).result
