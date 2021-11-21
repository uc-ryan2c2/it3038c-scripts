from hashlib import scrypt
import random
import os.path
from os import path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Label
import pyperclip

#main window
root = Tk()
root.title("Passcode Generator")
Label1 = Label(root, text="Welcome to the Password Generator application.")

#defining variables
var = IntVar()
var1 = IntVar()

def PasswdGenerator():
      gen = Toplevel()
      Toplevel.title("Password Generator")
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
 



#frame for then main buttons
frame = LabelFrame(root, text="Please Select An Option Below", padx=15, pady=15,)
frame.grid(row=1, column=0, pady=30, padx=30)
#Main Buttons
GenPasswd = Button(frame, text="Generate Password", padx=40, pady=30, fg="white", bg="black")
Bencruypt = Button(frame, text="Generate Password", padx=40, pady=30, fg="white", bg="black")
BDecrypt = Button(frame, text="Generate Password", padx=40, pady=30, fg="white", bg="black")
Bclose = Button(frame, text="Close", padx=40, pady=30, command=root.quit, fg="white", bg="black")
#main button layout
Label1.grid(row=0, column=0)
GenPasswd.grid(row=1, column=0, columnspan=4)
Bencruypt.grid(row=2, column=0, columnspan=4)
BDecrypt.grid(row=3, column=0, columnspan=4)
Bclose.grid(row=4, column=0, columnspan=4)


root.mainloop()




