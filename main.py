import time
import tkinter
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
import tkinter as tk

root = Tk()
root.title("Day by Hour Tracker")  # Window Title
root.iconbitmap('C:/Users/joeyf/PycharmProjects/classProject')
root.geometry("600x400")  # Size of window

logo = ImageTk.PhotoImage(Image.open("Parker-Hannifin-Logo.jpg"))
label1 = Label(image=logo)
label1.place(x=0, y=100)

name = Entry(root, width=60, borderwidth=9, font=20)
name.insert(0, "Enter Name")
name.pack()

# Define Variables
shiftTime = time.strftime("%H:%M", time.localtime())
btn_clicks = 0


# Body of functions
def validation():
    entry = name.get()
    msg = ''

    if len(entry) == 0:
        msg = 'name can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in name):
                msg = 'Name can\'t have numbers'
            elif len(entry) <= 2:
                msg = 'name is too short.'
            elif len(entry) > 100:
                msg = 'name is too long.'
            else:
                msg = 'Success!'
        except Exception as ep:
            messagebox.showerror('error', ep)

    messagebox.showinfo('message', msg)


def start():
    top = Toplevel()
    top.title("Day By Hour Dashboard")
    top.geometry("600x400")

    # Image in second window
    top_logo = ImageTk.PhotoImage(Image.open("PARKER-logo.png"))
    label2 = Label(top, image=top_logo)
    label2.place(x=100, y=300)

    # Displays current time
    time_label = Label(top, text="Time: " + shiftTime, font=("Arial", 18), padx=5, pady=5)
    time_label.grid(row=1, column=0)

    # Displays current shift based on time
    shift_label = Label(top, text="Shift: " + str(SHIFT()), font=("Arial", 18), padx=5, pady=5)
    shift_label.grid(row=2, column=0)

    # Displays name of employee
    name_label = Label(top, text=name.get(), font=("Arial", 18))
    name_label.grid(row=0, column=0)

    product_types = StringVar()
    product_label = Label(top, text=product_types.get(), font=("Arial", 18)).grid(row=1, column=4)

    # Array of product sizes with drop down list
    product_size = [
        '6"',
        '4"',
        '12"',
        '2"',
        '2V'
    ]
    product_types.set(product_size[0])
    drop = OptionMenu(top, product_types, *product_size, )
    drop.config(width=5, height=2)
    drop.place(x=190, y=45)
    drop_label = Label(top, font=("Arial", 12), text="Select Filter Size")
    drop_label.place(x=175, y=15)

    def size_targets():
        targets = [23, 28, 17, 19, 15]

    target_label = Label(top, font=("Arial", 18), text=size_targets())
    target_label.grid(row=1, column=5)

    # Function for the 'UP' button
    def up_button():
        global btn_clicks
        btn_clicks += 1
        count_label['text'] = btn_clicks

    # Function for the 'DOWN' button
    def down_button():
        global btn_clicks
        btn_clicks -= 1
        count_label['text'] = btn_clicks

    # UP button detail
    up_button = Button(top, text="UP", font=16, width=5, command=up_button)
    up_button.place(x=325, y=25)

    # Count detail
    count_label = Label(top, font=("Arial", 48), text=0)
    count_label.place(x=480, y=25)

    # Count Header
    count_header = Label(top, font=("Arial", 12), text="Current Filter Count")
    count_header.place(x=435, y=0)

    # Down button detail
    down_button = Button(top, text="DOWN", width=5, font=16, command=down_button)
    down_button.place(x=325, y=70)

    # Quit button detail
    quit_button = Button(top, text="End Shift", width=10, font=8, command=root.quit)
    quit_button.place(x=470, y=350)


btn = Button(root, text="Submit", font=22, command=validation).pack()

btn = Button(root, text="Start Shift", font=22, command=start).pack()


def SHIFT():
    if "0500" <= shiftTime <= "1530":
        shift = "1st Shift"
        return shift
    elif "1800" <= shiftTime:
        shift = "3rd Shift"
        return shift
    elif shiftTime < "0500":
        shift = "3rd Shift"
        return shift
    else:
        shift = input("What shift are you working?")


mainloop()
