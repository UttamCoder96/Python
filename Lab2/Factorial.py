try:
    N = int(input('Enter any integer: '))
    fact = 1
    if N < 0:
        print('Number must be positive integer !')
    else:
        for i in range(1, N+1):
           fact *= i
        print(f'Factorial: {fact}') 
except ValueError as v:
    print('Value error !!!')
except NameError as n:
    print('Name error !!!')
except TypeError as t:
    print('Type error !!!')
except IndexError as i:
    print('Index error !!!')