"""Tests for the Account class. Run them with:  python -m pytest"""

from decimal import Decimal

import pytest

from bank.account import Account, InsufficientFundsError, InvalidAmountError


def test_deposit_adds_money():
    account = Account("Aavash", 107001, 100)
    account.deposit("50")
    assert account.balance == Decimal("150.00")


def test_withdraw_takes_money_out():
    account = Account("Aavash", 107001, 100)
    account.withdraw(30)
    assert account.balance == Decimal("70.00")


def test_cannot_withdraw_more_than_balance():
    # This was the bug in my old code: the balance could go negative.
    account = Account("Aavash", 107001, 500)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(900)
    assert account.balance == Decimal("500.00")  # balance did not change


@pytest.mark.parametrize("bad_amount", ["abc", "", "-20", "0", "nan"])
def test_bad_amounts_are_rejected(bad_amount):
    account = Account("Aavash", 107001, 100)
    with pytest.raises(InvalidAmountError):
        account.deposit(bad_amount)


def test_money_math_is_exact():
    # With float, 0.1 + 0.2 = 0.30000000000000004. Decimal keeps it exact.
    account = Account("Aavash", 107001)
    account.deposit("0.10")
    account.deposit("0.20")
    assert account.balance == Decimal("0.30")


def test_empty_name_is_rejected():
    with pytest.raises(ValueError):
        Account("   ", 107001)