class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        print "New Car!!"
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12

    def display_all(self):
        print "price: ", str(self.price)
        print "speed: ", str(self.speed)
        print "fuel: ", str(self.fuel)
        print "mileage: ", str(self.mileage)
        print "tax: ", str(self.tax)
        return self

car1 = Car(20000, 150, 'Full', 15000)
car2 = Car(7000, 100, 'Empty', 50000)
car3 = Car(50000, 200, 'Full', 0)
car4 = Car(15000, 170, 'Almost Full', 10000)
car5 = Car(100000, 250, 'Full', 0)
car6 = Car(5000, 80, 'Empty', 70000)


car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
