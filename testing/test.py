import random
import os.path
from os import error, path
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Label
import pyperclip
from cryptography.fernet import Fernet

#Checks for item existence
PassList_exist = str(path.exists("PassList.txt"))
print("PassList exists: " + PassList_exist)

#this will create a file if the file does not already exist
if PassList_exist == 'False':
  f = open('PassList.txt', 'w')
  f.write("PASSCODES")
  f.write("\n")
  f.write("-------------------------------------------")
  f.write("\n")
  f.close
  print("Log file has been created in current directroy")

#main window
if __name__=="__main__":
  root = Tk()
  root.title("Passcode Generator")
  Label1 = Label(root, text="Welcome to the Password Generator application.")

#defining variables
var = IntVar()
var1 = IntVar()

def PasswdGenerator():
      TLroot = Toplevel()
      TLroot.title("Password Generator")
      TLroot.geometry("500x150")
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
      
      #Function to save password to file
            
      # create label and entry to show
      # password generated
      Random_password = Label(TLroot, text="Password")
      Random_password.grid(row=0)
      entry = Entry(TLroot)
      entry.grid(row=0, column=1)
 
      # create label for length of password
      c_label = Label(TLroot, text="Length")
      c_label.grid(row=1)
 
      # create Buttons Copy which will copy
      # password to clipboard and Generate
      # which will generate the password
      copy_button = Button(TLroot, text="Copy", command=copy1)
      copy_button.grid(row=0, column=2)
      generate_button = Button(TLroot, text="Generate", command=generate)
      generate_button.grid(row=0, column=3)
 
      # Radio Buttons for deciding the
      # strength of password
      # Default strength is Medium
      radio_middle = Radiobutton(TLroot, text="No Symbols", variable=var, value=0)
      radio_middle.grid(row=1, column=2, sticky='E')
      radio_strong = Radiobutton(TLroot, text="Can Include Symbols", variable=var, value=3)
      radio_strong.grid(row=1, column=3, sticky='E')
      combo = Combobox(TLroot, textvariable=var1)

      # Combo Box for length of your password
      combo['values'] = (8, 9, 10, 11, 12)
      combo.current(0)
      combo.bind('<<ComboboxSelected>>')
      combo.grid(column=1, row=1)

def Encrypt():
  response = messagebox.askyesno("Password file Encryption", "Would you like to Encrypt your Password file?")
  if response == 1:
    # key generation
    key = Fernet.generate_key()
  
    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
      filekey.write(key)

    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
  
    # using the generated key
    fernet = Fernet(key)
  
    # opening the original file to encrypt
    with open('PassList.txt', 'rb') as file:
        original = file.read()
      
    # encrypting the file
    encrypted = fernet.encrypt(original)
  
    # opening the file in write mode and 
    # writing the encrypted data
    with open('PassList.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    Label3 = Label(root, text="Password file has been ecrypted")
    Label3.grid(row=5, column=0)
  else:
    Label4 = Label(root, text="Password file has not been ecrypted") 
    Label4.grid(row=5, column=0)
    
#window for Decryption
def Decrypt():
  response1 = messagebox.askyesno("Password File Decryption", "Would you like to decrypt your password file?")
  if response1 == 1:
    #initializing the key
    with open('filekey.key', 'rb') as filekey:
      key = filekey.read()
    # using the key
    fernet = Fernet(key)
  
    # opening the encrypted file
    with open('PassList.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
  
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
  
    # opening the file in write mode and
    # writing the decrypted data
    with open('PassList.txt', 'wb') as dec_file:
        dec_file.write(decrypted)
    Label6 = Label(root, text="File has been decrypted")
    Label6.grid(row=5, column=0)
  else:
    Label5 = Label(root, text="File was not decrypted")
    Label5.grid(row=5, column=0)

  

#frame for then main buttons
frame = LabelFrame(root, text="Please Select An Option Below", padx=15, pady=15,)
frame.grid(row=1, column=0, pady=30, padx=30)
#Main Buttons
GenPasswd = Button(frame, text="Generate Password", padx=67, pady=15, fg="black", bg="white", command=PasswdGenerator)
Bencrypt = Button(frame, text="Encrypt Password File", padx=60, pady=15, fg="black", bg="white", command=Encrypt)
BDecrypt = Button(frame, text="Decrypt Password File", padx=59, pady=15, fg="black", bg="white", command=Decrypt)
Bclose = Button(frame, text="Close", padx=60, pady=15, command=root.quit, fg="black", bg="white")
#main button layout
Label1.grid(row=0, column=0)
GenPasswd.grid(row=1, column=0, columnspan=4)
Bencrypt.grid(row=2, column=0, columnspan=4)
BDecrypt.grid(row=3, column=0, columnspan=4)
Bclose.grid(row=4, column=0, columnspan=4)


root.mainloop()




