class BankAccount:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amounnt):
        if amounnt > 0:
            self.__balance += amounnt
        
    def get_balance(self):
        return self.__balance

ac = BankAccount()
ac.deposit(500) 
print(ac.get_balance())

#This is th example of an Encapsulation method.
