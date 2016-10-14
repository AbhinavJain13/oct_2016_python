class Car(object):
    def __init__(self, price, speed, fuel, miles):
      self.price = price
      self.speed = speed
      self.fuel = fuel
      self.miles = miles
      if (self.price>10000):
          self.tax=0.15
      else:
          self.tax=0.12
      def display_all(self):
        print ("Price: "+str(self.price)+", Speed: "+str(self.speed)+", Fuel: "+str(self.fuel)+", Mileage: "+str(self.miles)+", Tax: "+str(self.tax))
      display_all(self)

car1=Car(2000, "35mph", "Full", "15mpg")
car1=Car(2000, "5mph", " Not Full", "105mpg")
car1=Car(2000, "15mph", "Kind of Full", "95mpg")
car1=Car(2000, "25mph", "Full", "25mpg")
car1=Car(2000, "45mph", "Empty", "25mpg")
car1=Car(20000000, "35mph", "Empty", "15mpg")
