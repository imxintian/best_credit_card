import datetime
from typing import List, Dict


class CreditCard:
    def __init__(self, name: str, bill_day: int, repay_day: int, credit: float):
        self.name = name
        self.bill_day = bill_day
        self.repay_day = repay_day
        self.credit = credit
        self.balance = 0


def calculate_best_card(cards: List[CreditCard], date: datetime.date) -> CreditCard:
    best_card = None
    max_cycle = 0

    for card in cards:
        cycle = calculate_cycle(card, date)
        if cycle > max_cycle and card.balance < card.credit:
            max_cycle = cycle
            best_card = card

    return best_card


def calculate_cycle(card: CreditCard, date: datetime.date) -> int:
    next_bill_date = get_next_bill_date(card, date)
    days_to_bill = (next_bill_date - date).days
    days_to_repay = calculate_days_to_repay(card, next_bill_date)
    return days_to_bill + days_to_repay


def get_next_bill_date(card: CreditCard, date: datetime.date) -> datetime.date:
    if date.day <= card.bill_day:
        return date.replace(day=card.bill_day)
    next_month = date.replace(day=1) + datetime.timedelta(days=32)
    return next_month.replace(day=card.bill_day)


def calculate_days_to_repay(card: CreditCard, bill_date: datetime.date) -> int:
    repay_date = bill_date.replace(day=card.repay_day)
    if repay_date < bill_date:
        repay_date = repay_date.replace(month=repay_date.month % 12 + 1)
    return (repay_date - bill_date).days


def main():
    cards = [
        CreditCard("Card A", 5, 15, 10000),
        CreditCard("Card B", 26, 14, 15000),
    ]

    today = datetime.date.today()
    best_card = calculate_best_card(cards, today)

    print(f"On {today}, the best card to use is: {best_card.name}")


if __name__ == "__main__":
    main()