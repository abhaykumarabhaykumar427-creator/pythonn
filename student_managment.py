from tkinter import *

class Student:
    def __init__(self, name, roll, course):
        self.name = name
        self.roll = roll
        self.course = course

students = []

def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    course = course_entry.get()

    s = Student(name, roll, course)
    students.append(s)

    listbox.insert(END, f"{name} | {roll} | {course}")

    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    course_entry.delete(0, END)

root = Tk()
root.title("Student Management System")
root.geometry("500x400")

Label(root, text="Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Roll No").pack()
roll_entry = Entry(root)
roll_entry.pack()

Label(root, text="Course").pack()
course_entry = Entry(root)
course_entry.pack()

Button(root, text="Add Student", command=add_student).pack(pady=10)

listbox = Listbox(root, width=50)
listbox.pack(pady=20)

root.mainloop()