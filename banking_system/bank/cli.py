"""The text menu that the user types into."""

from bank.account import InsufficientFundsError, InvalidAmountError
from bank.storage import AccountStore

MENU = """
==== Aavash Development Bank ====
  1. Create account
  2. Show all accounts
  3. Deposit
  4. Withdraw
  5. Quit
"""


def ask_account_number(store: AccountStore):
    """Ask for an account number and return the account, or None if not found."""
    text = input("Account number: ").strip()
    if not text.isdigit():
        print("Account number should only contain digits.")
        return None
    try:
        return store.get(int(text))
    except KeyError as error:
        print(error.args[0])
        return None


def run(csv_path: str = "accounts.csv") -> None:
    """Show the menu again and again until the user picks Quit."""
    store = AccountStore(csv_path)

    while True:
        print(MENU)
        choice = input("Choose 1 to 5: ").strip()

        try:
            if choice == "1":
                name = input("Your name: ")
                deposit = input("Opening deposit (press Enter to skip): ").strip()
                account = store.create_account(name, deposit or None)
                print(f"Created account {account.number} for {account.name}.")

            elif choice == "2":
                if store.accounts:
                    print(store.to_dataframe().to_string(index=False))
                else:
                    print("No accounts yet.")

            elif choice in ("3", "4"):
                account = ask_account_number(store)
                if account is None:
                    continue
                amount = input("Amount: ")
                if choice == "3":
                    account.deposit(amount)
                else:
                    account.withdraw(amount)
                store.save()
                print(f"Done. New balance: {account.balance}")

            elif choice == "5":
                print("Goodbye!")
                break

            else:
                print("Please type a number from 1 to 5.")

        except (InvalidAmountError, InsufficientFundsError, ValueError) as error:
            # Bad input should show a friendly message, never crash the app.
            print(f"Error: {error}")


if __name__ == "__main__":
    run()