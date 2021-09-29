import time
from tkinter import *
import tkinter as tk

root = Tk()
root.title("Day by Hour Tracker")  # Window Title
root.geometry("600x400")  # Size of window

name = Entry(root, width=60, borderwidth=9, font=20)
name.insert(0, "Enter Name")
name.pack()

# Define Variables
shiftTime = time.strftime("%H:%M", time.localtime())
shift_label = ''
hour1 = 0
hour2 = 0
hour3 = 0
hour4 = 0
hour5 = 0
hour6 = 0
hour7 = 0
hour8 = 0
hour9 = 0
hour10 = 0
productSize = ""


# Body of functions

def start():
    top = Toplevel()
    top.title("Day By Hour Dashboard")
    top.geometry("800x600")
    time_label = Label(top, text=shiftTime, font=24)
    time_label.grid(row=0, column=0)
    shift_label = Label(top, text=SHIFT, font=24)
    shift_label.grid(row=0, column=2)


btn = Button(root, text="Start Shift", font=22, command=start).pack()





def SHIFT():

    if "0500" <= shiftTime <= "1530":
        shift = "1st Shift"
        shift_label.config(text=shift)
    elif "1800" <= shiftTime:
        shift = "3rd Shift"
        shift_label.config(text=shift)
    elif shiftTime < "0500":
        shift = "3rd Shift"
        shift_label.config(text=shift)
    else:
        shift = input("What shift are you working?")


mainloop()
