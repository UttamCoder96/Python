import math
r = int(input('Enter the radius of circle: '))
if r <= 0:
    print('Radius can not be negative !')
else:
    area = math.pi * r **2
    print(round(area, 2))
    perimeter = 2 * math.pi * r
    print(round(perimeter, 2))