class Car(object):
    def __init__(self, price, speed, mileage, fuel = "Full"):
        self.price = price
        self.speed = str(speed) + " mph"
        self.fuel = fuel
        self.mileage = str(mileage) +  " mpg"
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print "Price:",self.price
        print "Speed:",self.speed
        print "Fuel:",self.fuel
        print "Mileage:",self.mileage
        print "Tax:",self.tax
        print ""

test = Car(2000,35,15)
test1 = Car(2000,5,105,"Not Full")
test3 = Car(2000,15,95,"Kind of Full")
test4 = Car(2000,25,25)
test5 = Car(2000,45,25,"Empty")
test6 = Car(20000000,35,15,"Empty")
