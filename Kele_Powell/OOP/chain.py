class bike(object):
    def __init__ (self, max_speed, price):
        print "Bought a new bike!"
        self.price=price
        self.max_speed=max_speed
        self.miles=0
    def DisplayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
    def ride(self):
        self.miles+=10
        print "riding"
        print "Rode for 10 miles"
        return self
    def reverse(self):
        if self.miles>5:
            self.miles-=5
            print "Reversing"
            print "Reversed 5 miles"
        else:
            print "You dont have enough miles to reverse"
        return self

schwinn=bike("56mph","$500")
schwinn.ride().ride().ride().reverse().DisplayInfo()



Kona=bike("80mph","over $9000")
Kona.ride().ride().reverse().reverse().DisplayInfo()


Huffy=bike('20mph','$200')
Huffy.reverse().reverse().reverse().reverse().DisplayInfo()
