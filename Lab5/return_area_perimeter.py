class Square:
    def area(self, length):
        self.length = length
        return length ** 2
    def perimeter(self):
        return 4 * self.length
l = int(input('Enter the length of square: '))
obj = Square()
print(f'Area = {obj.area(l)}')
print(f'Perimeter = {obj.perimeter()}')