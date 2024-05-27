class account:
    def _init_(self,account_number,balance,account_type):
    self.account_number= account_number 
    self.balance=balance
    self.account_type= account_type

def deposite(self,amount):
    self.balance+=amount

def withdraw(self,amount):
    if self.balance>=amount:
        self.balance-=amount
    else:
        print("insufficient funds")


def delete_account(self):
    Print ("account deleted successfully")

#Creating an instance of the account class
new_account=Account("210942679",1000,"personal")