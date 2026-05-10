from tkinter import *

books = []

def add_book():
    book = entry.get()
    books.append(book)
    listbox.insert(END, book)
    entry.delete(0, END)

def issue_book():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

root = Tk()
root.title("Library Management")
root.geometry("400x350")

Label(root, text="Book Name").pack()

entry = Entry(root)
entry.pack()

Button(root, text="Add Book", command=add_book).pack(pady=5)
Button(root, text="Delete Book", command=issue_book).pack(pady=5)

listbox = Listbox(root, width=40)
listbox.pack(pady=20)

root.mainloop()