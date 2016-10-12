class Bike(object):
    def __init__(self,price=None,max_speed=None):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price,self.max_speed,self.miles
        return self

    def ride(self):
        print 'Riding! Wheeeeeee!'
        self.miles += 10
        return self

    def reverse(self):
        print 'Going in reverse is scaaaaarrrrrry!'
        if self.miles >=5:
            self.miles -= 5
            return self
        else:
            print 'Back where you started, bro!'
            return self


pee_wees_bike = Bike(10000,225)
eriks_bike = Bike(2500,25)
maxs_bike = Bike(2575,55)

# print pee_wees_bike
# print eriks_bike
# print maxs_bike

pee_wees_bike.ride()
pee_wees_bike.ride()
pee_wees_bike.ride()
pee_wees_bike.reverse()
pee_wees_bike.displayInfo()

eriks_bike.ride()
eriks_bike.ride()
eriks_bike.reverse()
eriks_bike.reverse()
eriks_bike.displayInfo()

# this instance cannot go backwards
maxs_bike.reverse()
maxs_bike.reverse()
maxs_bike.reverse()
maxs_bike.displayInfo()




# Have the first instance ride three times, reverse once and have it displayInfo().
# Have the second instance ride twice, reverse twice and have it displayInfo().
# Have the third instance reverse three times and displayInfo().
