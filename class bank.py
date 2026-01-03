class Bank: 
def   init  (self): 
self.no = int(input("Enter account number: ")) 
self.name = input("Enter account holder name: ") 
self.type = input("Enter account type(Savings/Current): ") 
self.balance = int(input("Enter balance amount:")) 
print("Account created successfully!") 
 
def deposit(self): 
amount = int(input("Enter amount to be deposit: ")) 
if (amount % 100 == 0): 
self.balance = self.balance + amount 
print("Amount deposited!") 
else: 
print("Enter multiples of 100") 
 
 
def withdraw(self): 
withdraw_amount = int(input("Enter amount to withdraw: ")) 
if withdraw_amount > self.balance: 
print("Insufficient balance!") 
elif withdraw_amount % 100 != 0: 
print("Can only withdraw multiples of 100") 
else: 
self.balance = self.balance - withdraw_amount 
print("Amount withdrawn successfully!") 
def display(self): 
print("Account Number :", self.no) 
print("Account Holder Name :", self.name) 
print("Account Type:", self.type) 
print("Available Balance:", self.balance) 
 
while (True): 
print("1.Account Creation","2.Deposit","3.Withdraw ","4.Display ") 
 
 
choice = int(input("Enter your choice: ")) 
if choice == 1: 
a = Bank() 
elif choice == 2: 
a.deposit() 
elif choice == 3: 
a.withdraw() 
elif choice == 4: 
a.display() 
else: 
print("Invalid choice! Please try again.")