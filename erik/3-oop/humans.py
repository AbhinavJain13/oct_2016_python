class Human(object):
    def __init__(self,clan=None):
        print "New human created."
        self.clan =  clan
        self.health = 100
        self.strength = 3
        self.intelligence = 3
        self.stealth = 3

    def taunt(self):
        print "you want some of this?!"

erik =  Human('Ninja')
# erik.taunt()
print erik.clan
