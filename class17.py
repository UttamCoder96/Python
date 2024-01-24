#Exception handling
from class17_temp import Add
result = Add(2, 3)
print(result)
#raise
age = int(input('Enter your age: '))
try:
    if age < 18:
        raise Exception('Xoti Bacchi Ho Kyaaa??!!! ')
    print('You are adult now !')
except Exception as e:
    print(e)


import class17_temp as operation
from class17_temp2 import inputs
def main():
    x, y = inputs()
    while True:
        print('''
              1. Additon
              2. Multipolicaton
              3. Division
              4. Subtraction
              5. Exit''')
        operator = int(input('Operation you want: '))
        if operator == '1':
            print(operation.Add(x, y))
        elif operator == '2':
            print(operation.Mul(x, y))
        elif operator == '3':
            print(operation.Div(x, y))
        elif operator == '4':
            print(operation.Sub(x, y))
        elif operator == '5':
            break
main()
        