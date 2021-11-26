class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

brandon_schumacher = User("Brandon Schumacher", "brandon@gmail.com")
fred_smith = User("Fred Smith", "fred@gmail.com")
jill_doe = User("Jill Doe", "jill@gmail.com")

brandon_schumacher.make_deposit(1000).make_deposit(500).make_deposit(700).make_withdrawal(500).transfer_money(jill_doe, 100).display_user_balance()
fred_smith.make_deposit(500).make_deposit(800).make_withdrawal(300).make_withdrawal(200).display_user_balance()
jill_doe.make_deposit(2500).make_withdrawal(500).make_withdrawal(200).make_withdrawal(400).display_user_balance()