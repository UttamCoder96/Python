def count(name):
    upper = 0
    lower = 0
    for i in name:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print(f'Upper case number: {upper}')
    print(f'lower case number: {lower}')
name = input('Enter any sentence: ')
#name.replace(' ', '')
#print(name)
count(name)