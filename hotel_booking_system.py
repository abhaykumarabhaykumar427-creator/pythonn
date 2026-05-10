from tkinter import *

rooms = {
    101: "Available",
    102: "Available",
    103: "Available"
}

def book_room():
    room_no = int(entry.get())

    if rooms.get(room_no) == "Available":
        rooms[room_no] = "Booked"
        status_label.config(text=f"Room {room_no} Booked")
    else:
        status_label.config(text="Room Not Available")

root = Tk()
root.title("Hotel Reservation")
root.geometry("400x300")

Label(root, text="Enter Room Number").pack()

entry = Entry(root)
entry.pack()

Button(root, text="Book Room", command=book_room).pack(pady=10)

status_label = Label(root, text="")
status_label.pack(pady=20)

root.mainloop()