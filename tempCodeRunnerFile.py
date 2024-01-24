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
obj1.show()