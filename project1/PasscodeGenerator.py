from hashlib import scrypt
import random
import os.path
from os import path


#checks if file has been created in current directory, if not creates it
print("Checking if Log file is in current directory.....")
file_exist = str(path.exists('PassList.txt'))

if file_exist == 'False':
    f = open('PassList.txt', 'w')
    f.write("PASSCODES")
    f.write("\n")
    f.write("------------------------")
    f.write("\n")
    f.close
    print("Log file has been created in current directroy")
else:
  print("Looks like you already have a log file :)")



lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B' 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
special = ['$', '%', '*', '^', '@']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#Function for passcode generator
while True:
  print("Would you like a new password?")
  answer = input("Please type yes or no: ")
  if answer != "yes" and answer != "no":
    print("That is not a valid input, please try again")
  if answer == 'yes':
    SC = ""
    software = input("Applicaiton password is for: ")
    while True:
        SC = input("Would you like special characters in the password? Please press y or n: ")
        if SC != 'y' and SC != 'n':
            print("That is not a valid input, please type in y or n")
        else:
            break

  #This will generate a password with special characters
    if SC == 'y':
      characters = [lowercase, uppercase, special, number]
      password = random.choice(uppercase) #this makes the password begin with a uppercase
      password_length = 10 #this sets the password length
      for x in range(int(password_length)):
        random_set = random.choice(characters)
        random_character = random.choice(random_set)
        password += random_character
      print("----------------")
      print(software + " password: " + password)
      print("----------------")
      while True:
        store = int(input("Press 1 to store this passcode or press 2 to skip: "))
        if store != 1 and store != 2:
          print("Not a valid input, please try again")
        if store == 1:
          f = open('PassList.txt', 'a')
          f.write("\n")
          f.write(software + " -- " + password)
          f.close()
          break
        if store == 2:
          break

  #this will generate a password without special characters
    elif SC == 'n':
      characters = [lowercase, uppercase, number]
      password = random.choice(uppercase)
      password_length = 10
      for x in range(int(password_length)):
        random_set = random.choice(characters)
        random_character = random.choice(random_set)
        password += random_character
      print("----------------")
      print(software + " password: " + password)
      print("----------------")
      while True:
        store = int(input("Press 1 to store this passcode or press 2 to skip: "))
        if store != 1 and store != 2:
          print("Not a valid input, please try again")
        if store == 1:
          f = open('PassList.txt', 'a')
          f.write("\n")
          f.write(software + " -- " + password)
          f.close()
          break
        if store == 2:
          break

  if answer == 'no':
    break

print("Thank you, please come again!")


 





#future steps --------
#make the file encrypted


#create tkinter GUI application for the the passcode generator







