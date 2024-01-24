#OOPS- Object Oriented Programming
 #Class
    #Syntax: class_name of class:
                #methode & attribute of class
#obj = class_name()
#obj.function_name(argumnets)
class Uttam:
    def show_details(self, name):
        print(f'Good Afternoon! {name} {chr(3)}')
obj1 = Uttam()
obj2 = Uttam()
n = input('Enter your name: ')
obj1.show_details(n)
obj2.show_details('Mukhiya')
#Constructor
    #Syntax:
             #class class_name:
                #def __init__(self, parameter1, parametern)
#obj = class_name(argumnets)
class Uttam:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print(self.name)
        print(self.age)
obj1 = Uttam('Uttam',20)
obj2 = Uttam('Sumi',23)
obj2.name = 'Meena'
obj2.show_details()
#normal operaton
class operation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        print(f'Sum is {self.num1 + self.num2}')
    def sub(self):
        print(f'Subtaction is {self.num1 - self.num2}')
    def mul(self):
        print(f'Multiplication is {self.num1 * self.num2}')
num1 = int(input('Enter 1st number: '))
num = int(input('Enter 2nd number: '))
obj1 = operation(num1, num)
while True:
    op = input("Enter the operator your want:(Opearator should be '+', '-', '*') ")
    if op == '+':
        obj1.sum()
    elif op == '-':
        obj1.sub()
    elif op == '*':
        obj1.mul()
    elif op == '%':
        break
    else:
        print(f'Invalid Operator!!{chr(2)}')