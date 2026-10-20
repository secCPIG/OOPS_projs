# Banking System Backend

A command line banking app written in object oriented Python. It creates accounts,
handles deposits and withdrawals, and saves records to a CSV file with pandas.

This is a rebuilt version of my earlier `bankacc.py` (in the main folder of this repo).
I rewrote it to fix bugs I found and to make the code cleaner and testable.

## Project structure

```
banking_system/
    bank/
        account.py    # Account class and money rules
        storage.py    # loading and saving accounts to CSV with pandas
        cli.py        # the text menu
    tests/            # pytest tests
```

## How to run

```
cd banking_system
python -m pip install -r requirements.txt
python -m bank.cli
```

## How to test

```
python -m pytest
```

## What I fixed from the old version

* **Negative balances:** the old code subtracted first and checked after, so you could withdraw more than you had. Now the check happens before any money moves.
* **Duplicate account numbers:** numbers were picked randomly from a short list. Now each new account gets the next unused number.
* **Crashes on bad input:** typing letters or negative amounts crashed the app or was accepted. Now every amount is validated and the user sees a clear message.
* **Money rounding:** balances use `Decimal` instead of `float`, so cents are always exact.
* **Untestable code:** the menu ran as soon as the file was imported. Now the logic, storage, and menu are separate, and the logic is covered by tests.

## Concepts used

Classes, encapsulation (read only balance through `@property`), custom exceptions,
type hints, pandas for CSV storage, and pytest for testing.