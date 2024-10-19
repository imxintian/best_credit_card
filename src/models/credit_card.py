from dataclasses import dataclass
from datetime import date

@dataclass
class CreditCard:
    name: str
    bill_day: int
    repay_day: int
    credit_limit: float
    balance: float = 0.0

    def is_valid(self) -> bool:
        return 1 <= self.bill_day <= 31 and 1 <= self.repay_day <= 31 and self.credit_limit > 0

    def available_credit(self) -> float:
        return max(0, self.credit_limit - self.balance)

    def update_balance(self, amount: float) -> None:
        self.balance += amount
        self.balance = max(0, min(self.balance, self.credit_limit))