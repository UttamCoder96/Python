class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def show_details(self):
        print(f'Name = {self.name}')
        print(f'age = {self.age}')
        print(f'grade = {self.grade}')
obj = Student('Uttam Mukhiya', 20, 'A')
obj.show_details()


