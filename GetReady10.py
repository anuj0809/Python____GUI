from tkinter import *

root = Tk()
canvas_height = 800
canvas_width = 600
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("CANVAS CHECK")
can_widget = Canvas(root, width = canvas_width, height = canvas_height)
can_widget.pack()
can_widget.create_line(400, 300, 800, 600)
can_widget.create_arc(40, 30, 600, 400,fill="red")
can_widget.create_window(7,2)
root.mainloop()