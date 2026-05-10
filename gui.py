import tkinter as tk

# function
def say_hello():
    name = entry.get()
    label.config(text=f"Hello Mr. {name}!")

# main window
root = tk.Tk()
root.title("My First GUI App")
root.geometry("300x200")

# label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# input box
entry = tk.Entry(root)
entry.pack(pady=5)

# button
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack(pady=10)

# output label
label = tk.Label(root, text="")
label.pack(pady=10)

# run app
root.mainloop()