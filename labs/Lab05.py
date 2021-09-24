from typing import AsyncGenerator
import math
from datetime import date, datetime

#today = datetime.now()
#print("todays date is " + str(today))   this will print todays date along with the seconds

print("this will output how old you are in seconds")

while True:
    try:
        print("please enter the year you were born: ")
        year = int(input())
        if year < 1920 or year >= 2021:
                print("this is not a realistic date")
                continue
        else:
            break
    except (ValueError) as err:
        print("That is not a correct date dummy")

while True:
    try:
        print("Please input the month you were born (1-12): ")
        month = int(input())
        if month < 1 or month > 12:
            print("not a vaild month")
            continue
        else:
            break
    except ValueError:
        print("That is not a integer for a month dummy")

while True:
    try:
        print("please input the day you were born: ")
        Day = int(input())
        if Day < 1 or Day > 31:
            print("this is not a valid day")
            continue
        else:
            break
    except ValueError:
        print("that is not an Integer for a day of the month you were born")

print("You were born on " + str(month) + "/" + str(Day) + "/" + str(year))


timeAlive = (datetime.today() - datetime(year, month, Day))  #this will give you time alive in days and seconds

dayAlive = timeAlive.days #this pulls days from the above equestion
secondsAlive = timeAlive.seconds#this pulls seconds from the above equestion


secondsAge = ((dayAlive * 86400) + secondsAlive)
print("you are " + str(secondsAge) + " seconds old")
