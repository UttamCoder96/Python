try:
    def operation(n):
        di = {n:n**2 for n in range(1,n+1)}
        print(di)
    inp = int(input('Enter any number: '))
    operation(inp)
except Exception as e:
    print('Error Found!')
