#It restrict access to certain attributes and methods to prevent modification
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        if amount > 50 and amount<=50000000:
            self.__balance+=amount
    def get_balance(self):
        return self.__balance
account=BankAccount(500000)
account.deposit(600000)
print("Balance", account.get_balance())