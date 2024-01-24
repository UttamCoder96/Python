#Inheritance

# i.single
class Animal:
    def show(self):
        self.name = input('Enter the name of your cat: ')

class cat(Animal):
    def disp(self):
        print(f"Your cat {self.name} is cute {chr(3)}")
obj1 = cat()
obj1.show()
obj1.disp()
# ii.Multiple 
class Animal:
    def get(self):
        self.name = input('Enter the name of your cat: ')
class Tom:
    def type(self):
        self.breed = input('Enter your cat breed: ')

class cat(Animal, Tom):
    def disp(self):
        print(f"Your cat {self.name} is cute {chr(3)}")
        print(f'Your cat breed {self.breed} is so nice')
obj1 = cat()
obj1.get()
obj1.type()
obj1.disp()
# iii.Multi-level
class Animal:
    def get(self):
        self.name = input('Enter the name of your cat: ')

class cat(Animal):
    def type1(self):
        self.breed = input('Enter your cat breed: ')
    
class Tom(cat):
    def disp(self):
        print(f"Your {self.breed} breed cat {self.name} is cute {chr(3)}")

obj1 = Tom()
obj1.get()
obj1.type1()
obj1.disp()