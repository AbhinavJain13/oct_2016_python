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
        if self.miles >=5:
            print 'Going in reverse is scaaaaarrrrrry!'
            self.miles -= 5
            return self
        else:
            print 'You can never go back!'
            return self

pee_wees_bike = Bike(10000,225)
eriks_bike = Bike(2500,25)
maxs_bike = Bike(2575,55)

pee_wees_bike.ride().ride().ride().reverse().displayInfo()

eriks_bike.ride().ride().reverse().reverse().displayInfo()

# Bikes are not allowed to go backwards
maxs_bike.ride().reverse().reverse().reverse().displayInfo()


# Have the first instance ride three times, reverse once and have it displayInfo().
# Have the second instance ride twice, reverse twice and have it displayInfo().
# Have the third instance reverse three times and displayInfo().
