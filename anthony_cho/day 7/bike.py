class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print("Riding")
        self.miles += 10
        return self
    def reverse(self):
        print("Reversing")
        self.miles -= 5
        return self


ruckus = Bike(130, "10mph")
shadow = Bike(600, "20mph")
trek = Bike(300, "15mpg")

ruckus.ride().reverse().displayInfo()
