#function
from temp2 import operation
try:
    n1 = int(input('Enter any number: '))
    n2 = int(input('Enter another number: '))
    _,result = operation(n1,n2)
    print(result)
except ValueError as v:
    print('value error!')
