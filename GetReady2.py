from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1255x955")
# photo = PhotoImage(file="1.png")

#FOR jpg Images
image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()




root.mainloop()