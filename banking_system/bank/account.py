"""The Account class holds the money rules for one bank account."""

from decimal import Decimal, InvalidOperation


class InvalidAmountError(ValueError):
    """Raised when an amount is not a positive number."""


class InsufficientFundsError(ValueError):
    """Raised when a withdrawal is bigger than the balance."""


def to_amount(value) -> Decimal:
    """Turn user input like "50" or 50.5 into a safe, positive money amount."""
    try:
        amount = Decimal(str(value).strip())
    except InvalidOperation:
        raise InvalidAmountError(f"'{value}' is not a valid number.")

    if not amount.is_finite() or amount <= 0:
        raise InvalidAmountError("Amount must be greater than 0.")

    return amount.quantize(Decimal("0.01"))  # round to cents


class Account:
    """One bank account with a name, an account number, and a balance."""

    def __init__(self, name: str, number: int, balance=0):
        name = name.strip()
        if not name:
            raise ValueError("Account name cannot be empty.")

        self.name = name
        self.number = number
        self._balance = Decimal(str(balance)).quantize(Decimal("0.01"))

    @property
    def balance(self) -> Decimal:
        """Read only balance. It can only change through deposit or withdraw."""
        return self._balance

    def deposit(self, value) -> Decimal:
        """Add money and return the new balance."""
        amount = to_amount(value)
        self._balance += amount
        return self._balance

    def withdraw(self, value) -> Decimal:
        """Take money out and return the new balance.

        We check the balance BEFORE subtracting, so it can never go negative.
        """
        amount = to_amount(value)
        if amount > self._balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}. Balance is only {self._balance}."
            )
        self._balance -= amount
        return self._balance

    def __repr__(self) -> str:
        return f"Account(name={self.name!r}, number={self.number}, balance={self._balance})"