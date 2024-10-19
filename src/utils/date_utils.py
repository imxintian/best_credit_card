from datetime import date, timedelta


def get_next_bill_date(bill_day: int, target_date: date = date.today()) -> date:
    """
    Calculate the next bill date given the bill day and a target date.

    :param bill_day: Day of the month when the bill is generated
    :param target_date: The date to calculate from (default is today)
    :return: The next bill date
    """
    if target_date.day <= bill_day:
        return target_date.replace(day=bill_day)
    next_month = target_date.replace(day=1) + timedelta(days=32)
    return next_month.replace(day=bill_day)


def calculate_days_to_repay(repay_day: int, bill_date: date) -> int:
    """
    Calculate the number of days between the bill date and the repayment date.

    :param repay_day: Day of the month when the payment is due
    :param bill_date: The date when the bill is generated
    :return: Number of days between bill date and repayment date
    """
    repay_date = bill_date.replace(day=repay_day)
    if repay_date < bill_date:
        repay_date = repay_date.replace(month=repay_date.month % 12 + 1)
    return (repay_date - bill_date).days