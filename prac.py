import tkinter as tk
from tkinter import messagebox
import pandas as pd
import random

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("400x400")
        
        self.label = tk.Label(root, text="Welcome to Aavash Development Bank", font=("Arial", 12))
        self.label.pack(pady=10)
        
        self.create_account_button = tk.Button(root, text="Create Account", command=self.create_account)
        self.create_account_button.pack(pady=5)
        
        self.check_details_button = tk.Button(root, text="Check Details", command=self.check_details)
        self.check_details_button.pack(pady=5)
        
        self.deposit_withdraw_button = tk.Button(root, text="Deposit/Withdraw", command=self.deposit_withdraw)
        self.deposit_withdraw_button.pack(pady=5)
    
    def create_account(self):
        create_window = tk.Toplevel(self.root)
        create_window.title("Create Account")
        create_window.geometry("300x250")

        tk.Label(create_window, text="Enter Name:").pack(pady=5)
        name_entry = tk.Entry(create_window)
        name_entry.pack(pady=5)
        
        tk.Label(create_window, text="Initial Deposit:").pack(pady=5)
        deposit_entry = tk.Entry(create_window)
        deposit_entry.pack(pady=5)
        
        def save_account():
            name = name_entry.get()
            deposit = deposit_entry.get()
            if not name or not deposit.isdigit():
                messagebox.showerror("Error", "Invalid input!")
                return
            acc_number = random.randint(107002, 107006)
            new_data = {"name": name, "acc_number": acc_number, "balance": int(deposit)}
            df = pd.DataFrame([new_data])
            df.to_csv("bankdetail.csv", mode='a', index=False, header=False)
            messagebox.showinfo("Success", f"Account Created!\nAccount Number: {acc_number}")
            create_window.destroy()

        submit_button = tk.Button(create_window, text="Submit", command=save_account)
        submit_button.pack(pady=10)
    
    def check_details(self):
        try:
            df = pd.read_csv("bankdetail.csv")
            messagebox.showinfo("Account Details", df.to_string())
        except FileNotFoundError:
            messagebox.showerror("Error", "No account details found!")
    
    def deposit_withdraw(self):
        trans_window = tk.Toplevel(self.root)
        trans_window.title("Deposit/Withdraw")
        trans_window.geometry("300x300")

        tk.Label(trans_window, text="Enter Account Name:").pack(pady=5)
        name_entry = tk.Entry(trans_window)
        name_entry.pack(pady=5)
        
        tk.Label(trans_window, text="Enter Amount:").pack(pady=5)
        amount_entry = tk.Entry(trans_window)
        amount_entry.pack(pady=5)
        
        def update_balance(transaction_type):
            try:
                df = pd.read_csv("bankdetail.csv")
                account_name = name_entry.get()
                amount = amount_entry.get()
                if not amount.isdigit():
                    messagebox.showerror("Error", "Invalid amount!")
                    return
                amount = int(amount)
                for i, row in df.iterrows():
                    if row["name"] == account_name:
                        if transaction_type == "Deposit":
                            df.at[i, "balance"] += amount
                        elif transaction_type == "Withdraw":
                            if row["balance"] >= amount:
                                df.at[i, "balance"] -= amount
                            else:
                                messagebox.showerror("Error", "Insufficient balance!")
                                return
                        df.to_csv("bankdetail.csv", index=False)
                        messagebox.showinfo("Success", f"{transaction_type} successful!\nNew Balance: {df.at[i, 'balance']}")
                        trans_window.destroy()
                        return
                messagebox.showerror("Error", "Account not found!")
            except FileNotFoundError:
                messagebox.showerror("Error", "No account records found!")
        
        deposit_button = tk.Button(trans_window, text="Deposit", command=lambda: update_balance("Deposit"))
        deposit_button.pack(pady=5)
        
        withdraw_button = tk.Button(trans_window, text="Withdraw", command=lambda: update_balance("Withdraw"))
        withdraw_button.pack(pady=5)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()
