from modules import GenePool
class Dog(animal):
    def __init__(self):
        self.health = 150
    def pet(self):
        self.health+=5

class Dragon(animal):
    def __init__(self):
        print "Did someone order, a fire breathing dragon?"
        self.health = 170

    def fly(self):
        self.health -=10
