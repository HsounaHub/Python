class BankAccount:
    # don't forget to add some default values for these parameters!
    all_instances=[]
    def __init__(self, int_rate=1, balance=0): 
        self.int_rate=int_rate/100
        self.balance=balance
        BankAccount.all_instances.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if self.balance-amount>0:
            self.balance-=amount
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        self.balance+=self.int_rate*self.balance
        return self
    @classmethod
    def All_Bank_Info(cls):
        for item in cls.all_instances:
            print(item)

account1=BankAccount(3,500)
account2=BankAccount(2,400)

account1.deposit(100).deposit(200).deposit(100).withdraw(300).yield_interest().display_account_info()
account2.deposit(200).deposit(100).withdraw(100).withdraw(200).withdraw(100).withdraw(300).yield_interest().display_account_info()