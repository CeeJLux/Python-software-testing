from datetime import date
print("Bank Related Project")

class Account:
    def __init__(self, name, account_num, account_bal):
        self.name = name
        self.account_num = account_num
        self.account_bal = account_bal

    def show_menu(self):
        print(f"{self.name}, Welcome to your Dashboard \n Available Balance = {self.account_bal}\n Date: {date.today()}")
        return "Done"

    @property
    def get_balance(self):
           print(f"Available Balance = {self.account_bal}")


emmanuel = Account("Emmanuel Joseph", "00000000000", "1,000,000")
print(emmanuel.show_menu())
print(emmanuel.get_balance)
