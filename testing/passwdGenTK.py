# Python program to generate random
# password using Tkinter module
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
 
# Function for calculation of password
def low():
    entry.delete(0, END)
 
    # Get the length of password
    length = var1.get()
 
    MediumPas = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    StrongPas = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = ""

    # if strength selected is medium
    if var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(MediumPas)
        return password
 
    # if strength selected is strong
    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(StrongPas)
        return password
    else:
        print("Please choose an option")
 
 
# Function for generation of password
def generate():
    password1 = low()
    entry.insert(10, password1)
 
 
# Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
 
 
# Main Function
 
# create GUI window
root = Tk()
var = IntVar()
var1 = IntVar()
 
# Title of your GUI window
root.title("Random Password Generator")
 
# create label and entry to show
# password generated
Random_password = Label(root, text="Password")
Random_password.grid(row=0)
entry = Entry(root)
entry.grid(row=0, column=1)
 
# create label for length of password
c_label = Label(root, text="Length")
c_label.grid(row=1)
 
# create Buttons Copy which will copy
# password to clipboard and Generate
# which will generate the password
copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=0, column=2)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=0, column=3)
 
# Radio Buttons for deciding the
# strength of password
# Default strength is Medium
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0)
radio_middle.grid(row=1, column=2, sticky='E')
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=1, column=3, sticky='E')
combo = Combobox(root, textvariable=var1)

# Combo Box for length of your password
combo['values'] = (8, 9, 10, 11, 12)
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1, row=1)
 
# start the GUI
root.mainloop()