#Function
try:
    def num(N):
        N = N + N
        return N
    n = int(input('Enter any number: '))
    re = num(n)
    print(re)
#upper and lower case conversion
    def name(N):
        N = N.lower()
        return N
    n = (input('Enter any number: '))
    re = name(n)
    print(re)
#fuction call from anoter file i.e 'temp.py'
    from temp2 import operation
    n = int(input('Enter 1st number: '))
    n2 = int(input('Enter 2nd number: '))
    opt = input('Enter the operator you want: ')
    operation(n,n2,opt)
    num = int(input('Enter any integer:'))
    operation(num)
except ValueError as v:
    print('value error !!!')
