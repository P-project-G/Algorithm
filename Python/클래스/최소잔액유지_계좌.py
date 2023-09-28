class BankAcocount:
    def __init__(self,balance=0,name='none'):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def get_info(self):
        print('이름:', self.name)
        print('잔고:', self.balance)


class MinimumBalanceACcount(BankAcocount):
    def __init__(self,minimum_balance=0, name='none'):
        self.minimum_balance = minimum_balance
        BankAcocount.__init__(self,0,name)

    def withdraw(self,amount):
        if self.balance-amount < self.minimum_balance:
            print("최소 잔액을 유지해야 합니다.")
        else:
            self.balance -= amount
        return self.balance


a=MinimumBalanceACcount(500,'Kim')
a.deposit(1000)
print(a.balance)
a.withdraw(1500)
print(a.balance)
a.deposit(1000)
a.withdraw(1500)
print(a.balance)