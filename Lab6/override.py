class Vehicle:
    def drive(self):
        print('From class Vehicle')
class Car(Vehicle):
    def drive(self):
        super().drive()
        print('From class Car')

class Bicycle(Vehicle):
    def drive(self):
        print('From class Drive')

obj1 = Bicycle()
obj2 = Car()
obj1.drive()
obj2.drive()

