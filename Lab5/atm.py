class Atm:
    def __init__(self, name, age, acc, money):
        self.name = name
        self.age = age
        self.acc = acc
        self.money = money
        self.extra()

    def check_balance(self):
        print(f'Your balance is {self.money}')
        self.extra()

    def deposit(self):
        new_balance = int(input('Enter amount: '))
        self.money += new_balance
        print(f'Your new balance is {self.money}')
        self.extra()

    def withdraw(self):
        withd = int(input('How much cash you want to withdraw? '))
        if withd <= 0:
            print('Amount should be grater than 0 !')
            exit
        elif withd < self.money:
            self.money -= withd
            print(f'Your remaining balance is {self.money}')
        else:
            print('Insufficient Balance !!!')
        self.extra()

    def user_details(self):
        print(f'Name = {self.name}')
        print(f'age = {self.age}')
        print(f'account type = {self.acc}')
        print(f'Balance = {self.money}')
        self.extra()
    def extra(self):
        print(f'''
              1.Check balance
              2.deposite
              3.withdrawl
              4.user details
              5.exit''')
        choose = int(input('Enter your choice: '))
        if choose == 1:
            self.check_balance()
        if choose == 2:
            self.deposit()
        if choose == 3:
            self.withdraw()
        if choose == 4:
            self.user_details()
        if choose == 5:
            exit
obj1 = Atm('Uttam', 20, 'Saving', 100000)