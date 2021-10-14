from tkinter import *
import tkinter

#canvas
root = Tk()
canvas = tkinter.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#Check Button
var1 = IntVar()
Checkbutton(root, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(root, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()

#User entry
#Label(root, text='First Name').grid(row=0)
#Label(root, text='Last Name').grid(row=1)
#entry1 = Entry(root)
#entry2 = Entry(root)
#entry1.grid(row=0, column=1)
#entry2.grid(row=1, column=1)
#mainloop()

#creates a list
#lb = Listbox(canvas)
#lb.insert(1, 'python')
#lb.insert(2, 'java')
#lb.insert(3, 'c++')
#lb.insert(4, 'other coding languahe')
#lb.pack()
#root.mainloop()
