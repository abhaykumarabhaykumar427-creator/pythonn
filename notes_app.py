import tkinter as tk
from tkinter import filedialog, messagebox

# Main Window
root = tk.Tk()
root.title("Smart Notes App")
root.geometry("700x500")
root.config(bg="#f0f0f0")

# Functions

# New Note
def new_note():
    text_area.delete(1.0, tk.END)

# Open File
def open_file():
    file = filedialog.askopenfile(
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

# Save File
def save_file():
    file = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file:
        content = text_area.get(1.0, tk.END)
        file.write(content)
        file.close()

        messagebox.showinfo(
            "Saved",
            "Note Saved Successfully!"
        )

# Exit App
def exit_app():
    root.destroy()

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

# Buttons
new_btn = tk.Button(
    button_frame,
    text="New",
    width=12,
    command=new_note
)
new_btn.grid(row=0, column=0, padx=5)

open_btn = tk.Button(
    button_frame,
    text="Open",
    width=12,
    command=open_file
)
open_btn.grid(row=0, column=1, padx=5)

save_btn = tk.Button(
    button_frame,
    text="Save",
    width=12,
    command=save_file
)
save_btn.grid(row=0, column=2, padx=5)

exit_btn = tk.Button(
    button_frame,
    text="Exit",
    width=12,
    command=exit_app
)
exit_btn.grid(row=0, column=3, padx=5)

# Text Area
text_area = tk.Text(
    root,
    font=("Arial", 14),
    wrap="word"
)

text_area.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=10
)

# Run App
root.mainloop()