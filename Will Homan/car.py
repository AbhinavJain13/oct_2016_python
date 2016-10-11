class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if(price <= 10000):
            self.tax = .12
        else: self.tax = .15
        self.display_all()
    def display_all(self):
        print('Price: ',self.price)
        print('Speed: ',self.speed)
        print('Fuel: ',self.fuel)
        print('Mileage: ',self.mileage)
        print('Tax: ',self.tax)


car1 = Car(2000, '35mph', 'Full', '15mpg')
car2 = Car(200000, '35mph', 'Empty', '15mpg')
