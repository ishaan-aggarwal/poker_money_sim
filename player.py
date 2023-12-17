from decimal import Decimal, getcontext

# set precision to 2 decimal places
getcontext().prec = 3

class Player:

    def __init__(self, name: str, amount: Decimal):
        self.name = name
        self.amount = amount
        self.pot_contribution = Decimal('0.00')

    def deposit_money(self, amount: Decimal) -> None:
        self.amount += amount

    def withdraw_money(self, amount: Decimal) -> None:
        if amount < 0:
            raise ValueError("Amount must be positive")
        elif amount > self.amount:
            raise ValueError("Insufficient funds")
        else:
            self.amount -= amount

