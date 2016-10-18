class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

bike1= Bike(200, "25mph", 0)
bike2= Bike(300, "50mph", 0)
bike3= Bike(1000, "4000mph", 0)

bike1.ride().ride().ride().reverse().displayInfo()

bike1.ride().ride().reverse().reverse().displayInfo()

bike3.reverse().reverse().reverse().displayInfo()
