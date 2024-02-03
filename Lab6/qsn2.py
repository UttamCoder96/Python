class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, grade, name, age ):
        self.grade = grade
        self.name = name
        self.age = age
        super().__init__(name, age)
    def show_details(self):
        print(f'''
              Name = {self.name}
              age = {self.age}
              grade = {self.grade}''')
class Teacher(Person):
    def __init__(self, subject, name, age):
        self.subject = subject
        self.name = name
        self.age = age
        super().__init__(name, age)
    def show_details(self):
        print(f'''
              name = {self.name}
              age = {self.age}
              subject = {self.subject}''')
obj1 = Student('A','uttam', 20)
obj2 = Teacher('Python', 'Anish', 29)
obj1.show_details()
obj2.show_details()