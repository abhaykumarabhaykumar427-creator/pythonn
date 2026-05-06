import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database setup
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")
conn.commit()

# Functions
def signup():
    username = signup_user.get()
    password = signup_pass.get()

    if username == "Abhay" or password == "dhan":
        messagebox.showerror("Error", "All fields required!")
    else:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Account created!")
        show_login()

def login():
    username = login_user.get()
    password = login_pass.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()

    if result:
        messagebox.showinfo("Success", "Login successful!")
        show_dashboard(username)
    else:
        messagebox.showerror("Error", "Invalid credentials")

def show_login():
    clear_frame()

    tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

    global login_user, login_pass
    login_user = tk.Entry(root)
    login_user.pack(pady=5)
    login_user.insert(0, "Username")

    login_pass = tk.Entry(root, show="*")
    login_pass.pack(pady=5)
    login_pass.insert(0, "Password")

    tk.Button(root, text="Login", command=login).pack(pady=10)
    tk.Button(root, text="Go to Signup", command=show_signup).pack()

def show_signup():
    clear_frame()

    tk.Label(root, text="Signup", font=("Arial", 16)).pack(pady=10)

    global signup_user, signup_pass
    signup_user = tk.Entry(root)
    signup_user.pack(pady=5)
    signup_user.insert(0, "Username")

    signup_pass = tk.Entry(root, show="*")
    signup_pass.pack(pady=5)
    signup_pass.insert(0, "Password")

    tk.Button(root, text="Signup", command=signup).pack(pady=10)
    tk.Button(root, text="Go to Login", command=show_login).pack()

def show_dashboard(username):
    clear_frame()

    tk.Label(root, text=f"Welcome {username}", font=("Arial", 16)).pack(pady=20)
    tk.Button(root, text="Logout", command=show_login).pack()

def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# Main Window
root = tk.Tk()
root.title("Login System")
root.geometry("300x300")

show_login()

root.mainloop()