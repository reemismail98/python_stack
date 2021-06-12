from BankAccount import BankAccount 
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def deposit(self, amount):
    	self.account.deposit(amount)
    def make_withdrawal(self, amount):
    	return self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()
        print(f"{self.name} balance is:{self.balance}")
    def transfer_money(self,other_user,amount):
        if self.withdrawal(amount):
            other_user.deposit(amount)
            return True
        return False     

user1=User("ree","reem@gmail.com,10000")  
azzam=("azzam",1958)
azzam.make_withdrawal(1000)
azzam.display_user_balance()
user1.make_withdrawal(1000)
user1.display_user_balance()
user1.transfer_money(ali,11000)      
