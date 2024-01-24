#Default argument
try:
    def ope(l, b , h = 2):
        area = l * b
        volum = l * b * h
        print(f'Area = {area}')
        print(f'Volume = {volum}')
    a = int(input('Enter the length: '))
    c = int(input('Enter the breadth: '))
    ope(a,c)
#Pass by object reference
    def ope(x, y):
        y = 20
        x.append(96)
        print(f'inside function = {y}') 
    n = [10]
    n2 = 19
    ope(n.copy(), n2)
    print(f'outside function = {n}')
#In dictionary
    def ope(x,y):
        x[2] = 'Mukhiya'
        print(f'Outside function: {x}') 
    n = {1:'Uttam'}
    n2 = 19
    ope(n, n2)
    print(f'outside function: {n}')
# use of "main"def opera(a, b):
    def opera(a, b):
        multi = a * b
        print(f'Multiplication = {multi}')
    def name(str):
        print(str)
    name('Uttam')
    if __name__ == '__main__':
        opera(9, 10)
except Exception as e:
    print('Error Found !!')
    print(chr(2))
