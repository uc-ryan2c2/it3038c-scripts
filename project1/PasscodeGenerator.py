from hashlib import scrypt
import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B' 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
special = ['$', '%', '*', '^', '@']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def PasscodeGenerator():
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
  print("would you like a password?")
  answer = input("Please type yes or no: ")
  if answer != "yes" and answer != "no":
    print("That is not a valid input, please try again")
  if answer == 'yes':
    PasscodeGenerator()
  if answer == 'no':
    print("thank you for using this generator! Please come again")
    break
  



 





#future steps --------

#ask the user if they want another passcode and then go through the loop

#out-put that password to a txt file that is encrypted and only they can access

#create tkinter GUI application for the the passcode generator







