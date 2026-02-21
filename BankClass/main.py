from BankAccount import BankAccount
from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount
checking1 = CheckingAccount("Fong", 10000, 1, 11, 400)
checking2 = CheckingAccount("Dank", 20000, 1, 12, 1000)
savings1 = SavingsAccount("Fong", 3, 13, 7000, .04)
savings2 = SavingsAccount("Dank", 4, 14, 8000, .06)
#Transfer 500 to savings
checking1.transfer(500,savings1)
#exceeds transfer limit
print(checking1.balance)
#transfer 400 instead
checking1.transfer(400,savings1)
#successful
print(checking1.balance)
print(savings1.balance)
#withdraw from checking1
checking1.withdraw(500)
#sucessful withdrawal
print(checking1.balance)
#add interest to savings2
print(savings2.balance)
savings2.add_interest()
print(savings2.balance)