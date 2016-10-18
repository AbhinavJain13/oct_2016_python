class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price < 10000:
            self.tax = 0.12
        else:
            self.tax = 0.15
        self.display_all()
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed, "mph"
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage, "mpg"
        print "Tax", self.tax

Car(2000, 200, "full", 200)
