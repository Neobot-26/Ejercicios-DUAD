class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit_money(self,amount_money):
        if amount_money <= 0:
            raise ValueError("The amount must be greater than zero")
        self.balance += amount_money
        
    def withdraw_money(self,amount_money):
        if amount_money <= 0:
            raise ValueError("The amount must be greater than zero")
        if amount_money > self.balance:
            raise ValueError("Insufficient Funds in Bank account")
        self.balance -= amount_money

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, min_balance=0):
        super().__init__(balance)
        self.min_balance = min_balance

    def withdraw_money(self, amount_money):
        if amount_money <= 0:
            raise ValueError("The amount must be greater than zero")
        
        if self.balance - amount_money < self.min_balance:
            raise ValueError("Unable to go lower than minimun balance defined")
        self.balance -= amount_money
        
#Main
account1 = SavingsAccount(balance=1000, min_balance=200)
account1.deposit_money(500)
print(account1.balance)
account1.withdraw_money(1000)
print(account1.balance)
account1.withdraw_money(400)
print(account1.balance)
