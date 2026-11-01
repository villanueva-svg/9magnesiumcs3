class BankAccount:
    def __init__(self, account_number="", account_holder="", balance=0.0):
        self.__account_number = account_number #Privated Attribute
        self.__account_holder = account_holder #Privated Attribute
        self.__balance = balance #Privated Attribute

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance must be a positive number.")

    def display_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder}")
        print(f"Account Balance: ${self.__balance:.2f}")

acc1 = BankAccount("123456789", "John Doe", 1000.0)
acc1.display_info()
acc1.set_balance = 1500.0
acc1.display_info()
acc1.set_balance = -500.0 #Trigger invalidation message