class animal(object):
    def __init__(self):
        print "Animal Created"
        self.health = 100
        self.name= "Atuck"

    def walk(self):
        if self.health > 2:
           self.health -=1
        if self.health <= 0:
           print "Oh No, looks like {} has died".format(self.name)
           return self

        print "Currently Walking,  {}".format(self.name)
        return self

    def run(self):
        if self.health > 6:
           self.health -=5
        if self.health <= 0:
           print "{}'s health is too low, please buy a musubi to revive {}'s health'".format(self.name, self.name)
           return self

        print "Currently running, {}".format(self.name)
        return self

    def displayHealth(self):
        print "{}'s Health: {}.".format(self.name, self.health)
        return self

    def musubi(self):
        self.health +=25
        print " +25  {} 's Health {}".format(self.name, self.health)
        return self
