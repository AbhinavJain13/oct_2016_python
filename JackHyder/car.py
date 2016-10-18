class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = 0
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def displayall(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax

car1=Car(10005, "25mph", "Almost entirely empty, but not quite", "1mpg")
car2=Car(2, "0.25mph", "Full", "2mpg")
car3=Car(600, "2mph", "Hard to tell", "3mpg")
car4=Car(238749823779, "25mph", "Almost entirely empty, but not quite", "4mpg")
car5=Car(6, "255mph", "Always empty", "5mpg")
car6=Car(666, "25555mph", "Never empty", "9000mpg")

car6.displayall()
