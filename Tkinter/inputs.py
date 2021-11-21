from tkinter import *
from typing import TypedDict

root = Tk()

e = Entry(root, width=50)
e.pack()
e.insert(0, "enter your name: ")


def myClick():
    mylabel3=Label(root, text="Look, my name is" + e.get())
    mylabel3.pack()
    
    
myButton = Button(root, text="Please enter your name", padx=25, pady=25, command=myClick, fg="white", bg="black")#this will create a button with size 25.
#formatting
myButton.pack()

root.mainloop()