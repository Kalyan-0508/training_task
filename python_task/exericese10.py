
class BankAccount:

    def __init__(self, balance=0):
        self.__balance = balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance! Cannot withdraw.")

    def check_balance(self):
        print("Current Balance:", self.__balance)
acc = BankAccount(1000)

acc.deposit(1000)
acc.withdraw(200)
acc.withdraw(2000)  
acc.check_balance()
