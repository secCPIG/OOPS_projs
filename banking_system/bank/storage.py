"""Saving and loading accounts from a CSV file using pandas."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from bank.account import Account

COLUMNS = ["name", "number", "balance"]
FIRST_ACCOUNT_NUMBER = 107001


class AccountStore:
    """Keeps all accounts in memory and saves them to a CSV file."""

    def __init__(self, csv_path: str | Path):
        self.csv_path = Path(csv_path)
        self.accounts: dict[int, Account] = {}
        self.load()

    def load(self) -> None:
        """Read the CSV file. If it does not exist yet, start empty."""
        self.accounts = {}
        if not self.csv_path.exists():
            return

        df = pd.read_csv(self.csv_path, dtype={"name": str, "balance": str})
        for row in df.itertuples(index=False):
            account = Account(row.name, int(row.number), row.balance)
            self.accounts[account.number] = account

    def save(self) -> None:
        """Write every account back to the CSV file."""
        rows = [
            {"name": a.name, "number": a.number, "balance": str(a.balance)}
            for a in self.accounts.values()
        ]
        pd.DataFrame(rows, columns=COLUMNS).to_csv(self.csv_path, index=False)

    def next_account_number(self) -> int:
        """Give the next unused number, so two accounts never share one."""
        if not self.accounts:
            return FIRST_ACCOUNT_NUMBER
        return max(self.accounts) + 1

    def create_account(self, name: str, opening_deposit=None) -> Account:
        """Make a new account, optionally with an opening deposit, and save it."""
        account = Account(name, self.next_account_number())
        if opening_deposit is not None:
            account.deposit(opening_deposit)
        self.accounts[account.number] = account
        self.save()
        return account

    def get(self, number: int) -> Account:
        """Find an account by number, or raise KeyError if it does not exist."""
        if number not in self.accounts:
            raise KeyError(f"No account with number {number}.")
        return self.accounts[number]

    def to_dataframe(self) -> pd.DataFrame:
        """All accounts as a pandas table, handy for printing."""
        rows = [
            {"name": a.name, "number": a.number, "balance": a.balance}
            for a in self.accounts.values()
        ]
        return pd.DataFrame(rows, columns=COLUMNS)