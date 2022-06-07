class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = float(int_rate)
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.int_rate > 0:
            self.balance += self.balance*self.int_rate
        return self


account_1 = BankAccount(0.2, 3600)
account_2 = BankAccount(0.3, 4300)

account_1.deposit(340).deposit(1500).deposit(600).withdraw(
    500).yield_interest().display_account_info()
account_2.deposit(750).deposit(600).withdraw(300).withdraw(50).withdraw(
    100).withdraw(800).yield_interest().display_account_info()
