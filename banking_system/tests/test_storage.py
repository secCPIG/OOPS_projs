"""Tests for saving and loading accounts. tmp_path is a temporary folder pytest gives us."""

from decimal import Decimal

from bank.storage import FIRST_ACCOUNT_NUMBER, AccountStore


def test_account_numbers_are_unique(tmp_path):
    store = AccountStore(tmp_path / "accounts.csv")
    first = store.create_account("Aavash")
    second = store.create_account("Kushal")
    assert first.number == FIRST_ACCOUNT_NUMBER
    assert second.number == FIRST_ACCOUNT_NUMBER + 1


def test_accounts_survive_save_and_load(tmp_path):
    csv_path = tmp_path / "accounts.csv"
    store = AccountStore(csv_path)
    account = store.create_account("Aavash", "250.75")
    account.withdraw("50.25")
    store.save()

    reloaded = AccountStore(csv_path)  # a fresh store reads the same file
    assert reloaded.get(account.number).balance == Decimal("200.50")
    assert reloaded.get(account.number).name == "Aavash"