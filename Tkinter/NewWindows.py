
from os import O_APPEND
from tkinter import *

root = Tk()
root.title("Radio buttons")

def open():
    top = Toplevel() #this open a new window
    btn2 = Button(top, text="close", command=top.destroy).pack #this will close the window
    #variables in a function need to be global when they are on a new window
    


btn = Button(root, text="Open Second window", command=open).pack()

top = Toplevel()

root.mainloop()
