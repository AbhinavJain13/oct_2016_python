class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()

    def display_all(self):
        print("Price: ", self.price)
        print("Speed: ", self.speed)
        print("Fuel: ", self.fuel)
        print("Mileage: ", self.mileage)
        print("Tax: ", self.tax)
        return self


honda = Car(1000, "30mph", "Full", "15mpg")
toyota = Car(1500, "30mph", "Full", "15mpg")
lexus = Car(15000, "60pmh", "Full", "15mpg")
audi = Car(20000, "70mph", "Full", "15mpg")
bmw = Car(16000, "65mph", "Full", "15mpg")
lincoln = Car(8000, "60mph", "Full", "15mpg")
