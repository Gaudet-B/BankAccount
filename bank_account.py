class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f'Interest rate: {self.int_rate}, Balance: {self.balance}')
        return self
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
    # @classmethod
    # def print_all_accounts_info(cls):
    #     for val in cls:
    #         print(val)

account1 = BankAccount(0.015, 1000)
account2 = BankAccount(0.019, 5000)

account1.deposit(1000).deposit(1000).deposit(1000).withdraw(1500).yield_interest().display_account_info()
account2.deposit(2500).deposit(2500).withdraw(500).withdraw(500).withdraw(500).withdraw(500).yield_interest().display_account_info()

# BankAccount.print_all_accounts_info()