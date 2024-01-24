try:
    def detect(n1):
        num = 56
        m = 67
        sum = n1 + num
    detect(5)
    print(f'Number of local varible: {detect.__code__.co_nlocals}')
except Exception as e:
    print(chr(2))
