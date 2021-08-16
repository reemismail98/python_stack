class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate=int_rate
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self  
    def display_account_info(self):
        print(f"YOUR BALANCE IS {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
# account1=BankAccount(0.01,2000).deposit(400).deposit(300).deposit(300).withdraw(100).yield_interest().display_account_info()
# account2=BankAccount(0.01,4000).deposit(500).deposit(600).withdraw(100).withdraw(200).withdraw(90).withdraw(150).yield_interest().display_account_info()



