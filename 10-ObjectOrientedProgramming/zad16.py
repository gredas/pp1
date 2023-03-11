import random
class Account():
    def __init__(self):
        self.balance = 0
        self.number = str(random.randint(10000000000000000000000000,100000000000000000000000000))
    def deposit(self,PLN):
        self.balance += PLN
    def withdraw(self,PLN):
        if self.balance<PLN:
            print('Not enough money')
        else:
            self.balance -= PLN
    def status(self):
        print(f'Bank Account No: {self.number[0:2]} {self.number[2:6]} {self.number[6:10]} {self.number[10:14]} {self.number[14:18]} {self.number[18:22]} {self.number[22:26]}')
        print(f'Balance: PLN {self.balance}')
acc = Account()
acc.status()
acc.deposit(25.30)
acc.status()
acc.withdraw(31.70)
acc.status()
acc.withdraw(14)
acc.status()
