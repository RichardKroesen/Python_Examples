# Brief: Encapsulation is the concept of controlled data access. 
# Adding "__" after self.ATTRIBUTE makes the variable member private in Python.

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount("1234567890", 1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())
