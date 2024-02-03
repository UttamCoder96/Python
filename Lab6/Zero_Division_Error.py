try:
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    result = n1 // n2
    print(result)
except ZeroDivisionError as e:
    print("Error! Cannot divide by zero")