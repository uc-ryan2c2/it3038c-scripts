from tkinter import *

root = Tk()
root.title("frames")

frame = LabelFrame(root, text="this is a frame", padx=5, pady=5)
frame.pack(pady=10, padx=10)

b = Button(frame, text="this a a button")
b.pack()
#you can use grid inside of a frame to organize the contents of a frame


root.mainloop()
