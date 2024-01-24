#function overriding
class Animal:
    def cat(self):
        print('parent')
class Dog(Animal):
    def cat1(self):
        print('child')
obj1 = Dog()
obj1.cat1()
print("----------------")
#super function
class Animal:
    def cat(self):
        print('parent')
class Dog(Animal):
    def cat1(self):
        super().cat()  #super function
        print('child')
obj1 = Dog()
obj1.cat1()
print("----------------")
#
class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(self.name)
class Hari(Person):
    def show1(self):
        print('child class')
h = Hari('Ram')
h.show()
#
class College:
    def __init__(self, name, locaton, phone):
        self.name = name
        self.location = locaton
        self.phone = phone
class Computer(College):
    def __init__(self, sem, total_subject, name, locaton, phone):
        self.sem = sem
        self.total_subject = total_subject
        super().__init__(name, locaton, phone)
    def show(self):
        print(self.sem, self.total_subject, self.name, self.phone, self.location)
obj1 = Computer(4, 6, 'Uttam', 'Sitapaila', 'XXXXXXXX')
obj1.show()
#
class College:
    def __init__(self, name, locaton, phone):
        self.name = name
        self.location = locaton
        self.phone = phone
class Computer(College):
    def __init__(self, sem, total_subject, name, locaton, phone):
        self.sem = sem
        self.total_subject = total_subject
        super().__init__(name, locaton, phone)
    def show(self):
        print(self.sem, self.total_subject, self.name, self.location, self.phone)
obj1 = Computer(4, 6, 'Uttam', 'Sitapaila', 'XXXXXXXX')
print(hasattr(obj1, 'name'))
print(getattr(obj1, 'location'))
setattr(obj1, 'name', 'Mukhiya')
#delattr(obj1, 'phone')
obj1.show() #got error because in line 17 we already deleted the attribute 'phone'
