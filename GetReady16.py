from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("765x457")
root.title("REVIEW PAGE")

def gogoagone():
    print(f"You have given {slider.get()} points")

    with open("points.txt", "a") as f:
        f.write(f"You have given {slider.get()} points.\n ")


Label(root, text="Rate us!....Your reviews are valuable.").pack()
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider.pack()

Button(root, text="Press to submit", command=gogoagone).pack()

root.mainloop()