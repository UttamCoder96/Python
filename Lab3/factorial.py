try:
    def fact(n):
        fact = 1
        if n == 1:
            print(f'factorial= {fact}')
        else:
            for i in range(1,n+1):
                fact *= i
            print(f'factorial = {fact}')
    num = int(input('Enter any positive integer: '))
    if num < 0:
        print('Number must be positive !')
    else:
        fact(num)
except Exception as e:
    print('Error Found !')