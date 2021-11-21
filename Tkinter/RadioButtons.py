
from tkinter import *

root = Tk()
root.title("Radio buttons")

r = IntVar()

def click():
    myLabel= Label(root, text=value)
    myLabel.pack()
    

Radiobutton(root, text="option 1", variable=r, value=1).pack()
Radiobutton(root, text="option 2", variable=r, value=1).pack()

myLabel= Label(root, text=r.get())
myLabel.pack()


root.mainloop()

