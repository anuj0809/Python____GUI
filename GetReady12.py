'''
from tkinter import *

root = Tk()
root.title("WINDOE SIZE CHANGER")
window_width = 600
window_height = 600
root.geometry(f"{window_height}x{window_height}")
def call(event):
    window_width -= 200
    window_height -= 200
    root.geometry(f"{window_height}x{window_height}")


button = Button(root, text="click to decrese window size")
button.pack()
button.bind('<Button-1>', call)
root.mainloop()
'''
# Cheating
from tkinter import *

root = Tk()
root.geometry("250x200")

def resize():
    width_value = width.get()
    height_value = height.get()
    root.geometry(f"{width_value}x{height_value}")

root.title("Window Resizer")
Label(text="Window Resizer", font="comicsansms 11 bold", pady=20).grid(column=2)

Label(text="Width: ", font="comicsansms 11").grid(row=1, column=1)
Label(text="Height: ", font="comicsansms 11").grid(row=2, column=1)

width = StringVar()
height = StringVar()

width_entry = Entry(root, textvariable=width).grid(row=1, column=2)
height_entry = Entry(root, textvariable=height).grid(row=2, column=2)

Button(text="Apply", command=resize, pady=2, font="comicsansms 11").grid(column=2)

root.mainloop()