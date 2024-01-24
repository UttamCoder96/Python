try:
    '''def operation(lis):
        ma = 0
        mi = lis[1]
        for i in lis:
            if i > ma:
                ma = i
            if i < mi:
                mi = i
        print(f'Maximum value = {ma}')
        print(f'Minimum value = {mi}')'''
    '''def operation(lis):
        even = []
        odd = []
        for i in lis:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        even.sort()
        odd.sort()
        print(f'even number sorted list= {even}')
        print(f'odd number sorted list= {odd}')'''
    '''def operation(num):
        is_prime = True
        for i in range(2,num):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            print('Entered number is prime')
        else:
            print('Entered number is not prime')'''
#class 9
    '''def operation(*args):
        sum = 0
        for i in args:
            sum += i
        multi = 1
        for i in args:
            multi *= i
        return sum, multi'''
#class 10
    from class10 import opera
    def operation(x, y):
        sum = x + y
        print(f'Sum = {sum}')
    opera(10, 20)
except ValueError as v:
    print('value error !!!')