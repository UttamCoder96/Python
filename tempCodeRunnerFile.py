class Animal:
    def cat1(self):
        print('parent')
class Dog(Animal):
    def cat1(self):
        super().cat1()  #super function
        print('child')
obj1 = Dog()
obj1.cat1()