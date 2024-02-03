try:
    age = int(input('Enter your age: '))
    if age < 16:
        raise Exception('you should 16+ for this!')
    print('Code for 16+')
except Exception as eee:
    print(eee)