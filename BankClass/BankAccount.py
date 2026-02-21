class BankAccount:

    bank_title = "Bank of Dank Memes"

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.min_balance = 10.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance <= self.min_balance or (self.balance - amount <= self.min_balance):
            print(amount, "will reduce your balance to below the minimum balance.  You cannot withdraw until your balance remains greater than ", self.min_balance)
            return
        self.balance -= amount

    def print_customer_information(self):
        print(BankAccount.bank_title, ":")
        print("Customer Name: ", self.name)
        print("Customer Balance: ", self.balance)
        print("Customer Minimum Balance: ", self.min_balance)

