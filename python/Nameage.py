import time

start_time = (time.time())   #this will start to count amount of time the script is running for


print('what is your name?')
myName = input()

##promt for a specific name
#while myName != 'your name':
#   print('this is not "your name", please type "your name"')
#    myName = input()

while True:
    print("please type your name.")
    myName = input()
    if myName == 'your name':
        break
print ("thank you")

print('hello, ' + myName + '. That is a good name. How old are you?')
myAge = str(input())

#determine message based on age
if int(myAge) < 13:
    print("learning young, thats good!")
elif int(myAge) == 13:
    print("You are the teenager now... that is cool I guess")
elif int(myAge) > 13 and int(myAge) < 30:
    print("still young, still learning")
elif int(myAge) >=30 and int(myAge) <= 65:
    print("you are an adult, thats cool")
else:
    print("you have lived a long time")

programAge = str(int(time.time() - start_time))
print(myAge + '? that is funny, I am only ' + programAge + ' seconds old')
print("I wish I was " + str(int(myAge) * 2) + " years old" )

time.sleep(3) #this will pause the program for three seconds.  you will need to import this mmodule
print("I'm tired. I go to sleep now")
