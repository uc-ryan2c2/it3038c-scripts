#Write a ‘guess the number game’ where a random number is generated and the user must guess the number.
#The program says if their number is too high or too low until the right answer is guessed.

import random

num = random.randint(0,20)


print("Hello, I have picked number between 1-20.")
print("Please input your first guess between 0-20.")
guess = int(input())

while num != guess:
    if guess < num:
        print("Looks like your guess was too low, please try again.")
        guess = int(input())
    elif guess > num:
        print("Looks like you guess was too big, please try again")
        guess = int(input())


print("You got it! You guessed my number!")








