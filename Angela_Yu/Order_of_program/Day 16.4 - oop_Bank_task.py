class BankAccount:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance
        
    def deposit(self, amount):
        self.balance + amount
        print(f"the deposit amount is: ${amount}")
        
    def withdraw(self, amount):
        self.balance - amount
        print(f"the withdraw amount is: ${amount}")
        
    def display_balance(self):
        balance = self.balance
        print(f"Your current balance is: {balance}")
        
# Create two BankAccount objects here and perform the operations above

bankacc = BankAccount(11223344,"Ajay",1000)
bankacc.display_balance()
bankacc.deposit(1000)
bankacc.withdraw(500)
bankacc.deposit(2000)
bankacc.withdraw(1000)
bankacc.display_balance()