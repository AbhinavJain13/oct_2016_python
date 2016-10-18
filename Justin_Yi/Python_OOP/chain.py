class Bike(object):
    def __init__(self, price, max_speed,miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "Price:", self.price, "Max Speed:", self.max_speed, "Miles:", self.miles
    def ride(self):
        self.miles += 10
        print "Riding", self.miles
        return self
    def reverse(self):
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print "Reversing", self.miles
        return self

bike1 = Bike(10,10,30)
bike1.reverse().reverse().ride().displayinfo()
