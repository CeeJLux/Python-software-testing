from datetime import date
print("Bank Related Project")

class Account:
    def __init__(self, name, account_num, account_bal):
        self.name = name
        self.account_num = account_num
        self.account_bal = account_bal

    def show_menu(self):
        print(f"{self.name}, Welcome to your Dashboard \n Available Balance = {self.account_bal}\n Date: {date.today()}\n")
        return "Done"

    @property
    def get_balance(self):
        print(f"Available Balance = {self.account_bal} \n")
        return "Done"

    def deposit(self, amount):
        self.account_bal += amount
        print(f"Deposit Successful \n Current Balance = {self.account_bal} \n")
        return "Done"


emmanuel = Account("Emmanuel Joseph", "00000000000", 1000000)

print(emmanuel.deposit(3000))
