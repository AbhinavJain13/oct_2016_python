class Animal(object):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print self.name
        print self.health
        return self
    def animal(self):
        self.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def pet(self):
        self.health+=5
        return self
    def petapet(self):
        self.walk().walk().walk().run().run().pet().displayHealth()
dog = Dog("Dog",150)
dog.petapet()

class Dragon(Animal):
    def fly(self):
        self.health-=10
        return self
    def msg(self):
        print "this is a dragon!"
        return self
    def flyapet(self):
        self.walk().walk().walk().run().run().fly().fly().msg().displayHealth()
dragon = Dragon("Dragon",170)
dragon.flyapet()
