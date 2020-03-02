from tkinter import *

root = Tk()
root.geometry("655x333")
root.title("Welcome to Anuj's dance club")

def getdel():
    print(f"NAME is {nameval.get()}")
    print(f"Age is {ageval.get()}")
    print(f"Gender is {genderval.get()}")
    print(f"School is {schoolval.get()}")
    print(f"Address is {addressval.get()}")


label = Label(text='''ENTER YOUR DETAILS''', bg="black", fg="white", padx=5, pady=5, font="comicsansms 20 bold", borderwidth=6, relief=SUNKEN)
label.grid(row=0, column=5)

name = Label(root, text="ENTER NAME")
age = Label(root, text="ENTER AGE")
gender = Label(root, text="ENTER GENDER")
address = Label(root, text="ENTER ADDRESS")
school = Label(root, text="ENTER SCHOOL")
name.grid(row=3)
age.grid(row=4)
gender.grid(row=5)
address.grid(row=6)
school.grid(row=7)

nameval = StringVar()
ageval = StringVar()
genderval = StringVar()
addressval = StringVar()
schoolval = StringVar()

nameent = Entry(root, textvariable=nameval).grid(row=3, column=1)
ageent = Entry(root, textvariable=ageval).grid(row=4, column=1)
genderent = Entry(root, textvariable=genderval).grid(row=5, column=1)
addressent = Entry(root, textvariable=addressval).grid(row=6, column=1)
schoolent = Entry(root, textvariable=schoolval).grid(row=7, column=1)

Button(text="SUBMIT", command=getdel).grid(row=8, column=1)

root.mainloop()
