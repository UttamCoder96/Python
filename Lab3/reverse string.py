try:
    def reverse(na):
        name1 = na[::-1]
        print(name1)
    name = input('Enter your name: ')
    reverse(name)
except Exception as e:
    print('Error found!')