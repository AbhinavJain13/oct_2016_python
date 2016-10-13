class Animal(object):
    def __init__ (self, name, health=100):
        self.name = name
        self.health = health
    def walk(self):
        self.health-=1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print (str(self.name)+" "+str(self.health))
        return self
animal=Animal("animal")
animal.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health=150
    def pet(self):
        self.health+=5
        return self
dog=Dog("Dog")
dog.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health=170
    def fly(self):
        self.health-=10
        return self
    def displayHealth(self):
        print("this is dragon!")
        super(Dragon, self).displayHealth()
        return self
dragon=Dragon("Dragon")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
