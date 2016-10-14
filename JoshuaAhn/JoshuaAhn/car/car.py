class Car(object):
     def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
           self.tax = 0.15 * self.price
        else:
           self.tax = 0.12 * self.price

     def displayInfo(self):

         print 'Price: {}, Speed: {}, Fuel: {}, Mileage: {}, Tax: {}'.format(self.price, self.speed, self.fuel, self.mileage, self.tax)

car1 = Car(2000, '35mph', 'Full', '15mpg')
car2 = Car(2000, '5mph', 'Not Full' , '105mpg')
car3 = Car(2000, '45mph', 'Empty', '25mpg')
car4 = Car(2000, '15mph', 'Kind of Full', '95mpg')
car5 = Car(2000, '25mph', 'Full', '25mpg')
car6 = Car(200000, '35mph', 'Empty', '15mpg')

car1.displayInfo()
car2.displayInfo()
car3.displayInfo()
car4.displayInfo()
car5.displayInfo()
car6.displayInfo()
