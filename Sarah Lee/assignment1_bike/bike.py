class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        print "New Bike!!!"
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayinfo(self):
        print "price: ", self.price
        print "max_speed: ", self.max_speed
        print "miles: ", self.miles
        return self

    def ride(self):
        self.max_speed += 10
        print "Riding!", self.max_speed
        return self

    def reverse(self):
        self.miles -= 5
        print "Reversing!", self.miles
        return self
        if self.miles < 0:
            print "Impossible--negative miles"

bike1 = Bike(200, 30, 10)
bike2 = Bike(150, 25, 20)
bike3 = Bike(250, 35, 40)

bike1.ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
