from tkinter import *

def abhishek(event):
    print(f"You clicked on the button at {event.x}, {event.y}")


root = Tk()
root.title("EVENT HANDELER")
root.geometry("600x600")

widget = Button(root, text="Click me please")
widget.pack()

widget.bind('<Button-1>', abhishek)
widget.bind('<Double-1>', quit)

root.mainloop()