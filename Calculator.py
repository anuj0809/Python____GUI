from tkinter import *

root = Tk()
root.geometry("300x1000")
root.title("Anuj's Calculator")
root.configure(background="brown")

def click(event):

    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, text=scvalue, font="lucida 40 bold")
screen.pack(fill=X, padx=5, pady=5, ipadx=10)

f = Frame(root, bg="grey")

b = Button(f, text="9", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="8", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="7", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind("<Button-1>", click)

f.pack()



f = Frame(root, bg="grey")

b = Button(f, text="6", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx=3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="5", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="4", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 3, pady=2)
b.bind("<Button-1>", click)

f.pack()



f = Frame(root, bg="grey")

b = Button(f, text="3", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="2", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="1", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 3, pady=2)
b.bind("<Button-1>", click)

f.pack()



f = Frame(root, bg="grey")

b = Button(f, text="/", padx=5, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text="*", padx=1, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind('<Button-1>', click)

b = Button(f, text="%", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx=4, pady=4)
b.bind("<Button-1>", click)

f.pack()



f = Frame(root, bg="grey")

b = Button(f, text="+", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="-", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 3, pady=2)
b.bind('<Button-1>', click)

b = Button(f, text="=", padx=2, pady=3, font="lucida 33 bold")
b.pack(side=LEFT, padx= 9, pady=2)
b.bind("<Button-1>", click)

f.pack()

f = Frame(root, bg="grey")

b = Button(f, text="C", padx=2, pady=3, font="lucida 33 bold")
b.pack(padx=3, pady=2)
b.bind('<Button-1>', click)
f.pack()


root.mainloop()
