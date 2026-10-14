class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.__account_number = account_number #Privated Attribute 
        self.__account_holder = account_holder  #Privated Attribute
        self.__balance = balance  #Privated Attribute

    def deposit(self, amount=0.0): #Manages deposits into BankAccount objects
        if amount > 0:
            self.__balance += amount #Stored amount increased by deposit amount
            print(f"Deposited: {amount:.2f}. New balance: {self.__balance:.2f}")
        else: #If deposit amount is not a positive number
            print("Deposit amount must not be negative.")

    def withdraw(self, amount=0.0): #Manages withdrawals from BankAccount objects
        if 0 < amount <= self.__balance:
            self.__balance -= amount #Stored amount reduced by withdrawal amount
            print(f"Withdrew: {amount:.2f}. New balance: {self.__balance:.2f}")
        else: #If withdrawal amount exceeds current balance or is not a positive number
            print("Invalid withdrawal amount.")

    def get_balance(self): #Displays current balance of BankAccount objects
        return self.__balance

    def get_account_info(self): #Displays information about the BankAccount object
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: {self.__balance:.2f}")
        
# Example Object

acc1 = BankAccount("123456789", "John Doe", 1000.0)
acc1.get_account_info()
acc1.deposit(-0.25)
acc1.withdraw(1000.5)
