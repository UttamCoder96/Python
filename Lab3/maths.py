def permutation(a, b):
    fact4 = 1
    fact1 = 1
    for i in range(1, a+1):# n!
        fact1 *= i
    for i in range(1, b+1):# (n-r)!
        fact4 *= i
    #print(fact4)
    per = fact1 // fact4
    print(f'Permutaion is {per}')
    return fact4 # (n-r)!
def combination(x, y):
    fact2 = 1
    fact3 = 1
    result1 = permutation(x, x - y)
    #print(result1)
    for i in range(1, x+1):# n!
        fact2 *= i
    #print(fact2)
    for i in range(1, y+1):# r!
        fact3 *= i
    #print(fact3)
    result2 = fact2 // (fact3 * result1)
    print(f'Combination is {result2}')
r = int(input('Enter the value of r: '))
num = int(input('Enter any positive integer: '))
combination(num,r)


    

    