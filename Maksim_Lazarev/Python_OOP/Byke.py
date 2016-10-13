class Bike(object):
    def __init__(self, price, max_speed, miles=0):
      self.price = price
      self.max_speed = max_speed
      self.miles = miles
    def displayInfo(self):
        print ("Price: "+str(self.price)+", Max Speed: "+str(self.max_speed)+", Miles: "+str(self.miles))
    def ride(self):
        print ("Riding")
        self.miles+=10
    def reverse(self):
        print ("Reversing")
        if (self.miles>=5):
            self.miles-=5
        else:
            self.miles=0

bike1=Bike(200, "25mph")
bike2=Bike(200, "25mph")
bike3=Bike(200, "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
