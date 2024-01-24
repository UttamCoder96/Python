import pdb
pdb.set_trace()
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
name = 'Uttam'
print('good morning sir!!\n')
a=int(input('Enter first number:\n'))
b=int(input('Enter second number: '))
print(f'Enterd number are:\nFirst number: {a}\nSecond number: {b}')
#Arithmetic operator
print(f'Sum of your input number is: {a+b}')
print(f'Substraction of input number is: {a-b}')
print(f'Multiplication of input number is: {a*b}')
print(f'Division: {a//b}')
print(f'Exponential: {a**b}')
print(f'Modulus: {a%b}')
a += 1
b -= 1
c *= 2
d /= 2
e %= 2
f **= 2
print(f'{a}\n{b}\n{c}\n{d}\n{e}\n{f}')
#Logical operator
print(a==b)
print(b!=c)
print(a<=b)
print(d>=e)
#or & and operator
if a!=b and a==c:
    print('WOW!!!SO BEAUTIFUL!!')
elif b!=e or d>e :
    print('ABCDEFG')
if 'T' in name:
    print('Found')
else:
    print('404 error\nAlpha. Not Found !!!')
#not operator
if not name:
    print('That is empty')
else:
    print('That is not empty')
#Changing constants value
name='Uttam'
name='Mukhiya'
print(name)
#Multiple assignment
X,Y,Z=1,2,3
Y,Z=1,2
print(X,Y,Z)

