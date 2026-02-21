from BankAccount import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, name, account_no, routing_no, balance, interest_rate):
        super().__init__(name, balance, account_no, routing_no)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
