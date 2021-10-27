from hashlib import scrypt
import random
import os.path
from os import path

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B' 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
special = ['$', '%', '*', '^', '@']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

print("Checking is log file is in current directory....")

#Check for item existence and type
PassList_exist = str(path.exists("PassList.txt"))
EC_PassList_exist = str(path.isfile("EC-PassList.txt"))

print("PassList exists: " + PassList_exist)
print("Encrypted Password List: " + EC_PassList_exist)

if PassList_exist == 'False' or EC_PassList_exist == 'True':
    print("Log exist")
    if PassList_exist == 'False' and EC_PassList_exist == 'False' :
        f = open('PassList.txt', 'w')
        f.write("PASSCODES")
        f.write("\n")
        f.write("------------------------")
        f.write("\n")
        f.close
        print("Log file has been created in current directroy")

#Function for passcode generator
def PasscodeGenerator():
  while True:
    print("Would you like a new password?")
    answer = input("Please type yes or no: ")
    if answer != "yes" and answer != "no":
      print("That is not a valid input, please try again")
    if answer == 'yes':
      SC = ""
      software = input("Applicaiton password is for: ")
      while True:
          print("Would you like special characters in the password?")
          print("1. yes")
          print("2. No")
          SC = int(input())
          if SC != 1 and SC != 2:
              print("That is not a valid input, please type in y or n")
          else:
              break

  #This will generate a password with special characters
      if SC == 1:
        characters = [lowercase, uppercase, special, number]
        password = random.choice(uppercase) #this makes the password begin with a uppercase
        password_length = 10 #this sets the password length
        for x in range(int(password_length)):
          random_set = random.choice(characters)
          random_character = random.choice(random_set)
          password += random_character
        print("---------------------------------")
        print(software + " password: " + password)
        print("---------------------------------")
        while True:
          print("Would you like to store this passcode to your password file?")
          print("1. Store Passcode")
          print("2. Skip and don't store password")
          store = int(input())
          if store != 1 and store != 2:
            print("Not a valid input, please try again")
          if store == 1:
            PassList_exist = str(path.exists("PassList.txt"))
            if PassList_exist =='False':
              f = open('EC-PassList.txt', 'a')
              f.write('\n')
              f.write(software + " -- " + password)
              f.close()
            if PassList_exist == 'True':
              f = open('PassList.txt', 'a')
              f.write("\n")
              f.write(software + " -- " + password)
              f.close()
            break
          if store == 2:
            break
      

  #this will generate a password without special characters
      elif SC == 2:
        characters = [lowercase, uppercase, number]
        password = random.choice(uppercase)
        password_length = 10
        for x in range(int(password_length)):
          random_set = random.choice(characters)
          random_character = random.choice(random_set)
          password += random_character
        print("---------------------------------")
        print(software + " password: " + password)
        print("---------------------------------")
        while True:
          print("Would you like to store this passcode to your password file?")
          print("1. Store Passcode")
          print("2. Skip and don't store password")
          store = int(input())
          if store != 1 and store != 2:
            print("Not a valid input, please try again")
          if store == 1:
            PassList_exist = str(path.exists("PassList.txt"))
            if PassList_exist =='False':
              f = open('EC-PassList.txt', 'a')
              f.write('\n')
              f.write(software + " -- " + password)
              f.close()
            if PassList_exist == 'True':
              f = open('PassList.txt', 'a')
              f.write("\n")
              f.write(software + " -- " + password)
              f.close()
            break
          if store == 2:
              break
    if answer == 'no':
      print("Thank you!")
      break


# File encryption
def Encrypt(filename, key):
  PassList_exist = str(path.exists("PassList.txt"))
  if PassList_exist == 'True':
    filename = "PassList.txt"
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open("EC-" + filename, "wb")
    file.write(data)
    file.close()
    os.remove(filename)
  if PassList_exist == 'False':
    filename = "EC-PassList.txt"
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()

choice = ""
while choice != "3":
    print("Please select an option.")
    print("1. Generate Password")
    print("2. Encrypt File")
    print("3. Decrypt File")
    print("4. Quit")
    choice = input()
    if choice == "1":
      PasscodeGenerator()
    if choice == "2" or choice == "3":
      print("Please enter a key to encrypt or decrypt your password file.")
      print("Key need to be between 1-255.")
      print("NOTE - PLEASE MAKE SURE TO REMEBER YOUR KEY TO DECRYPT YOUR PASSWORD FILE")
      key = int(input("Key: "))
    if choice == "2":
      PassList_exist = str(path.exists("PassList.txt"))
      if PassList_exist == 'False':
        filename = 'EC-PassList.txt'
        Encrypt(filename, key)
        print("File has been encrypted, Please make sure to remember your key to decrypt your password.")
      else:
        filename = 'PassList.txt'
        Encrypt(filename, key)
        print("File has been encrypted, Please make sure to remember your key to decrypt your password.")
    if choice == "3":
        filename = "EC-PassList.txt"
        Decrypt(filename, key)
        print("File has been decrypted!")
    if choice == "4":
      break

print("Thank you, please come again!")


 





#future steps --------
# Make this a GUI experience




