class animal:
    def sum(self,a,b):
        self.a = a
        self.b = b
        print(self.a + self.b)
    def value(self):
        self.sum(2,3)
obj1 = animal()
obj1.value()
#Magical 
class animal:
    def __init__(self, age, name):
        self.name = name
        self.age = age
        #print(name)
    def __str__(self):
        return f'{self.age}Uttam'
obj1 = animal(20, 'Uttam')
print(obj1)
#
class details:
    def __init__(self, name):
        self.name = name
obj1 = details('Uttam')
print(obj1.name)
obj1.name = 'Pragyan'
print(obj1.name)
#
class details:
    def __init__(self, name):
        self.name = name
obj1 = details('Uttam')
#print(obj1.name)
def change1(obj1):
    print(obj1.name)
    obj1.name = 'Pragyan'
    print(obj1.name)
change1(obj1)