# Private attribute i.e. 'self.__name'
class person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def print1(self):
        print(self.__name)
        print(self.age)
obj1 = person('Uttam', 20)
# obj1.__name = 'Mukhiya'
obj1.age = 21
# print(obj1.__name)
print(obj1.age)
#Name Mangling/ accessing Private attributes outside class
print(obj1._person__name)
#
class person:
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    def set_name(self, name):
        self.__name = name
        print(self.__name)
obj1 = person('Uttam', 20)
print(obj1._person__name)
obj1.set_name('Unknown')