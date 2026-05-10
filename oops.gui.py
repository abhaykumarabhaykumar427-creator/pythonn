from tkinter import *

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def total_salary(self):
        return self.salary

def calculate():
    name = name_entry.get()
    salary = int(salary_entry.get())

    emp = Employee(name, salary)

    result_label.config(
        text=f"{emp.name} Salary: {emp.total_salary()}"
    )

root = Tk()
root.title("Payroll System")
root.geometry("400x300")

Label(root, text="Employee Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Salary").pack()
salary_entry = Entry(root)
salary_entry.pack()

Button(root, text="Calculate Salary", command=calculate).pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=20)

root.mainloop()