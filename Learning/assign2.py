class BankAccount:
    def __init__(self,amount):
        self.amount = amount
    def chk_balance(self):
        print(f"Your current balance is: ", self.amount)
    def deposit(self):
        return 
    
p1 = BankAccount(700000)
p1.chk_balance()
