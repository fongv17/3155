from BankAccount import BankAccount

class CheckingAccount(BankAccount):

    def __init__(self, name, balance, account_no, routing_no, transfer_limit):
        super().__init__(name, balance, account_no, routing_no)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, other_account):
        if amount > self.balance or (amount > self.transfer_limit):
            print("Insufficient funds or amount exceeds your transfer limit of",self.transfer_limit)
        else:
            self.balance -= amount
            other_account.balance += amount