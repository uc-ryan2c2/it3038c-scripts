from tkinter import *
from typing import TypedDict

root = Tk() #this has to come first

#creating a lebel widget
myLabel = Label(root, text="hello world!")
myLabel2 = Label(root, text="my name is Connnor Ryan")

#Buttons


def myClick():
    mylabel3=Label(root, text="Look, the button did somthing")
    mylabel3.grid(row=3,column=0)
    
    
myButton = Button(root, text="Click me", padx=25, pady=25, command=myClick, fg="white", bg="black")#this will create a button with size 25.
#formatting
myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)

root.mainloop()
