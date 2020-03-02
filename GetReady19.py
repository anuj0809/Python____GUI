from tkinter import *

root = Tk()
root.title("Article")
root.geometry("654x567")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill=BOTH)
scrollbar.config(command=txt.yview)
root.mainloop()