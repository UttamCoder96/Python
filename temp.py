from class17_temp2 import take
import class17_temp as operation
def main():
    x, y = take()
    while True:
        print('''
              1. Additon
              2. Multipolicaton
              3. Division
              4. Subtraction
              5. Exit''')
        operator = input('Operation you want: ')
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
        