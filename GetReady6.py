from tkinter import *

root = Tk()
root.geometry("633x456")

def name():
    print("Anuj")


def age():
    print("You are 19 years old")


def birth_date():
    print("08 september 2000")


def gender():
    print("male")

frame = Frame(root, borderwidth="7", bg="blue", relief=SUNKEN)
frame.pack(side=RIGHT, anchor="nw")

b1 = Button(frame, fg="brown", text="Tell your name", command=name)
b1.pack(side=RIGHT, padx=33)

b2 = Button(frame, fg="brown", text="Tell your age", command=age)
b2.pack(side=RIGHT, padx=33)

b3 = Button(frame, fg="brown", text="Tell your birth date", command=birth_date)
b3.pack(side=RIGHT, padx=33)

b4 = Button(frame, fg="brown", text="Tell your gender", command=gender)
b4.pack(side=RIGHT, padx=33)
root.mainloop()
