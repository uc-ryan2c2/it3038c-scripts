
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Radio buttons")

#below is a list of all the message boxes that can be used
# showinfo   showwarning   askquestion   showerror   askokcancel   askyesno

def popup():
    response = messagebox.askyesno("this is my popup", "hello world")
    #Label(root, text=response).pack()
    if response == 1:
        Label(root, text="you clicked yes").pack()
    else:
        Label(root, text="you clicked no").pack()

Button(root, text="popup", command=popup).pack()

root.mainloop()
