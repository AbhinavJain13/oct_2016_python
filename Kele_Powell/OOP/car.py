class Car(object):
    def __init__(self, price,speed,fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if price>0:
            if price>10000:
                self.tax=0.15
            else:
                self.tax=0.12
        else:
            print "You cant have a free car!"
        self.displayAll()

    def displayAll (self):
        print "\nPrice: $"+ str(self.price), "\nSpeed: "+ str(self.speed)+"mph" "\nFuel: "+ self.fuel,"\nMileage: " +str(self.mileage)+" miles" "\nTax: "+ str(self.tax)+"%"





Honda= Car(1000,90,"full",35000)
Toyota= Car(32000,110,"full",0)
ferd= Car(5000,60,"half full",63456)
chevy= Car(20000,78,"3/4 full", 2000)
datson= Car(7200,40,"almost empty",35)
hyunda= Car(100,0,"empty",1000000)
