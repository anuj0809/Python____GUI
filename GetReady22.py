from tkinter import *

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.geometry("744x377")
        self.title("Hi...Welcome the OOP's GUI")

    def status(self):
        self.val = StringVar()
        self.val.set("Let's Begin")
        self.statusbar = Label(self, textval=self.val, relief=SUNKEN, anchor="w")
        self.statusbar.pack(side=BOTTOM, fill=X)


if __name__ == '__main__':
    window = GUI()
    window = status()
    window.mainloop()
