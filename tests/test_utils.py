import pytest
from datetime import date
from src.utils.date_utils import get_next_bill_date, calculate_days_to_repay


def test_get_next_bill_date():
    # Test when target date is before bill day
    assert get_next_bill_date(15, date(2023, 5, 10)) == date(2023, 5, 15)

    # Test when target date is after bill day
    assert get_next_bill_date(15, date(2023, 5, 20)) == date(2023, 6, 15)

    # Test when target date is on bill day
    assert get_next_bill_date(15, date(2023, 5, 15)) == date(2023, 5, 15)


def test_calculate_days_to_repay():
    # Test when repay day is in the same month
    assert calculate_days_to_repay(20, date(2023, 5, 15)) == 5

    # Test when repay day is in the next month
    assert calculate_days_to_repay(5, date(2023, 5, 25)) == 11

    # Test when bill date and repay date are the same
    assert calculate_days_to_repay(15, date(2023, 5, 15)) == 0

# You can add more test cases here
from datetime import date
from src.utils.date_utils import calculate_days_to_repay
def test_calculate_days_to_repay():
    # 测试当还款日在当月
    assert calculate_days_to_repay(15, date(2023, 5, 15)) == 5, "Test when repay day is in the same month failed"

    # 测试当还款日在下个月
    assert calculate_days_to_repay(5, date(2023, 5, 25)) == 11, "Test when repay day is in the next month failed"

    # 测试当账单日和还款日是同一天
    assert calculate_days_to_repay(15, date(2023, 5, 15)) == 0, "Test when bill date and repay date are the same failed"

    # 测试当还款日是当月的第一天
    assert calculate_days_to_repay(1, date(2023, 5, 1)) == 0, "Test when repay day is the first day of the month failed"

    # 测试当还款日是当月的最后一天
    assert calculate_days_to_repay(31, date(2023, 5, 31)) == 0, "Test when repay day is the last day of the month failed"

    # 测试当账单日是当月的第一天，还款日在下个月
    assert calculate_days_to_repay(30, date(2023, 5, 1)) == 30, "Test when bill date is the first day and repay day is in the next month failed"

    # 测试当账单日是当月的最后一天，还款日在当月
    assert calculate_days_to_repay(31, date(2023, 5, 30)) == 1, "Test when bill date is the last day and repay day is in the same month failed"

# 可能还需要添加更多的测试用例来涵盖更多的边界情况和可能的错误输入
