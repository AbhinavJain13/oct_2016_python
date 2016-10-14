import random
class bike(object):
    def __init__(self, speed, price):
        print "Succesfully immported a new bike"
        self.price= price
        self.max_speed= speed
        self.miles= 0

    def displayinfo(self):
        print 'Speed: {}, Price: {}, Milage:{}'.format(self.max_speed, self.price, self.miles)


    def ride(self):
        print "Riding"
        self.miles = self.miles +10
        return self


    def reverse(self):
        print "Reversing"
        self.miles = self.miles -5
        return self

# instance 1
bike1 = bike(200, 300)
bike1.ride().ride().ride().reverse().displayinfo()

# instance 2
bike1.ride().ride().reverse().reverse().displayinfo()
#instance 3
bike1.reverse().reverse().reverse().displayinfo()
