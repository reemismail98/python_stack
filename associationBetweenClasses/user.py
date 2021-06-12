from Bankaccount import BankAccount
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def deposit(self, amount):
    	self.account.deposit(amount)
    def make_withdrawal(self, amount):
    	self.account.withdraw(amount)
    def display_user_balance(self):
        print(f"username: {self.name}")
        self.account.display_account_info()
    def transfer_money(self,other_user,amount):
        self.make_withdrawal(amount)
        other_user.deposit(amount)    

user1=User("reem","reem@gmail.com")  
azzam=("azzam","1958@gmail.com")
user1.deposit(1000)
user1.make_withdrawal(500)
user1.display_user_balance()
     

