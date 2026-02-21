from BankAccount import BankAccount

bankaccount1 = BankAccount("Fong", 20000)
bankaccount2 = BankAccount("Dank", 20)

bankaccount1.print_customer_information()

bankaccount1.deposit(100)

bankaccount1.print_customer_information()

bankaccount1.withdraw(20090)

bankaccount1.withdraw(2000)

bankaccount1.print_customer_information()

bankaccount2.print_customer_information()