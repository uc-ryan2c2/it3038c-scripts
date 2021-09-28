import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B' 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
special = ['$', '%', '*', '^', '@']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']



software = input("Applicaiton password is for: ")
SC = input("Would you like special characters in the password? Please press y or n: ")

if SC == 'y':
  characters = [lowercase, uppercase, special, number]
  password = random.choice(uppercase) #this makes the password begin with a uppercase
  password_length = 10
  for x in range(int(password_length)):
    random_set = random.choice(characters)
    random_character = random.choice(random_set)
    password += random_character
  print("----------------")
  print(software + " password: " + password)
  print("----------------")

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

#out-put that password to a txt file





