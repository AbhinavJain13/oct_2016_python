# Create a class called  Car.
# In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage.
# If the price is greater than 10,000, set the tax to be 15%.
# Otherwise, set the tax to be 12%.
#
# Create six different instances of the class Car.
# In the class have a method called display_all() that returns all the information about the car as a string.
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

class Car(object):
    def __init__(self,price=None,speed=None,fuel=None,mileage=None):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = self.calcTax()
        self.display_all()

    def calcTax(self):
        if self.price > 10000:
            return 0.15
        else:
             return 0.12
    def display_all(self):
        print 'Price: ',self.price,'\n','Speed: ',self.speed,'\n','Fuel: ',self.fuel,'\n','Mileage: ',self.mileage,'\n','Tax: ',self.tax,'\n\n'

mustang = Car(9000,225,'unleaded only', 125000)
jeep = Car(125000,50,'premium leaded only', 125000)
porsche = Car(100000,300,'premium leaded only',11000)
