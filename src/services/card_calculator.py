from datetime import date, timedelta
from typing import List, Tuple
from src.models.credit_card import CreditCard
from src.utils.date_utils import get_next_bill_date, calculate_days_to_repay


def calculate_best_card(cards: List[CreditCard], target_date: date = date.today()) -> CreditCard:
    """计算给定日期最适合使用的信用卡"""
    best_card = None
    max_cycle = 0

    for card in cards:
        if card.available_credit() <= 0:
            continue

        cycle = calculate_cycle(card, target_date)
        if cycle > max_cycle:
            max_cycle = cycle
            best_card = card

    return best_card


def calculate_cycle(card: CreditCard, target_date: date) -> int:
    """计算指定信用卡在给定日期的账单周期长度"""
    next_bill_date = get_next_bill_date(card.bill_day, target_date)
    days_to_bill = (next_bill_date - target_date).days
    days_to_repay = calculate_days_to_repay(card.repay_day, next_bill_date)
    return days_to_bill + days_to_repay


def get_current_billing_cycle(card: CreditCard, target_date: date = date.today()) -> Tuple[date, date, date]:
    """
    计算信用卡当前或最近的账单周期和还款日

    :param card: 信用卡对象
    :param target_date: 目标日期，默认为今天
    :return: 元组 (周期开始日, 周期结束日, 还款日)
    """
    last_bill_date = get_next_bill_date(card.bill_day, target_date - timedelta(days=32))
    next_bill_date = get_next_bill_date(card.bill_day, target_date)

    if last_bill_date <= target_date < next_bill_date:
        # 目标日期在当前账单周期内
        cycle_start = last_bill_date
        cycle_end = next_bill_date - timedelta(days=1)
    else:
        # 目标日期不在当前账单周期内，使用下一个周期
        cycle_start = next_bill_date
        cycle_end = get_next_bill_date(card.bill_day, next_bill_date) - timedelta(days=1)

    repay_date = cycle_end.replace(day=card.repay_day)
    if repay_date < cycle_end:
        repay_date = repay_date.replace(month=repay_date.month % 12 + 1)

    return cycle_start, cycle_end, repay_date