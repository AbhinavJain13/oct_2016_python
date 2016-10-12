# Create a class called Animal with the following attributes: name, and health.
# Give the animal following three methods: walk, run, and displayHealth.
# Give a new animal a health of 100 when it gets created.
# When a walk() method is invoked, have the health decrease by 1.
# When a run() method is involved, have the health decrease by 5.
# When a displayHealth() method is invoked, display on screen the name of the Animal and the health.
#
# Create an instance of the animal called 'animal' and have this animal walk three times, run twice, and have it display its health.
#
# Now, create another class called Dog that inherits everything that the Animal does and has,
# but 1) have the default health be 150 and
# 2) add a new method called pet, which when invoked, increase the health by 5.

# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
#
# Now, create another class called Dragon that also inherits everything from Animal,
# but 1) have the default health be 170 and
# 2) add a new method called fly, which when invoked, decreased the health by 10.

#Have the Dragon walk() three times, run() twice, fly() twice, and have it displayHealth(). When the Dragon's displayHealth function is called, have it say 'this is a dragon!' before it displays the default information (by calling the parent's displayHealth function).
#
# Now for the first instance of the animal (instance called 'animal'), try calling fly() or pet() and make sure this doesn't work.

class Animal(object):
    def __init__(self,name=None):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -=5
        return self
    def displayHealth(self):
        print 'Name: ',self.name,'\n','Health: ',self.health
        return self

class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
        self.name = name
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health =  170
    def fly(self):
        self.health -= 5
        return self

pig = Animal('Pig')
# walk three times, run twice, and have it display its health
pig.walk().walk().walk().run().run().displayHealth()

doggie = Dog('Lassie')
# walk() three times, run() twice, pet() once, and have it displayHealth
doggie.walk().walk().walk().run().run().pet().displayHealth()

bigdragon = Dragon('Blow Hard')
bigdragon.walk().walk().walk().run().run().fly().displayHealth()
# walk() three times, run() twice, fly() twice, and have it displayHealth()
