
# with both a deposit() and a withdraw() function 
class BankAccount: 
	def __init__(self): 
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine") 

	def deposit(self): 
		amount=float(input("Enter amount to be Deposited: ")) 
		self.balance += amount 
		print("\n Amount Deposited:",amount) 

	def withdraw(self): 
		amount = float(input("Enter amount to be Withdrawn: ")) 
		if self.balance>=amount: 
			self.balance-=amount 
			print("\n You Withdrew:", amount) 
		else: 
			print("\n Insufficient balance ") 

	def display(self): 
		print("\n Net Available Balance=",self.balance) 


#Define a child class min balance

class MinimumBalanceAccount(BankAccount):
    def __init__(self,minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance
    def withdraw(self,amount):
        if self.balance - amount < self.minimum_balance:
            print("Sorry, minimum balance is low ")
        else:
            BankAccount.withdraw(self.amount)

# creating an object of class 
s = BankAccount() 

# Calling functions with that class object 
s.deposit() 
s.withdraw() 
s.display() 

