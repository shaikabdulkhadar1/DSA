class Bank:
    def __init__(self, accNumber, balance):
        self.accNumber = accNumber
        self.balance = balance
    
    def debit(self, amount):
        self.balance -= amount
        print('$',amount,'was debitted')
    
    def credit(self, amount):
        self.balance += amount
        print('$',amount,'was creditted')

    def getBalance(self):
        return self.balance

b1 = Bank(123456, 2500)
print('Account No:', b1.accNumber, '- Balance:', b1.getBalance())
b1.debit(1000)
print('Account No:', b1.accNumber, '- Balance:', b1.getBalance())
b1.credit(500)
print('Account No:', b1.accNumber, '- Balance:', b1.getBalance())
