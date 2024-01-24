N = int(input('Enter the number you want to check: '))
if N < 0:
    print('Invalid Number !!!')
for i in range(2, N):
    if N % i == 0:
        print('Entered number is not prime')
        break
    else:
        print('Entered number is prime')
        break