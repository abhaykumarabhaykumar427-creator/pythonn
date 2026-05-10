from tkinter import *

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

account = BankAccount()

def deposit_money():
    amount = int(amount_entry.get())
    account.deposit(amount)
    balance_label.config(text=f"Balance: {account.balance}")

def withdraw_money():
    amount = int(amount_entry.get())
    account.withdraw(amount)
    balance_label.config(text=f"Balance: {account.balance}")

root = Tk()
root.title("Bank System")
root.geometry("400x300")

Label(root, text="Enter Amount").pack()

amount_entry = Entry(root)
amount_entry.pack()

Button(root, text="Deposit", command=deposit_money).pack(pady=5)
Button(root, text="Withdraw", command=withdraw_money).pack(pady=5)

balance_label = Label(root, text="Balance: 0")
balance_label.pack(pady=20)

root.mainloop()