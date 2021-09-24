#This script will output fiix for numbers devisable by three and buzz for number devisable by 5. 

#it will also output fizzbuzz for numbers devisable by both three and five



for num in range(101): #this will generate number from 0-100.
    if (num % 15 == 0 and num != 0):
        print(num, " FiizBuzz")
    elif (num % 3 == 0 and num != 0):
        print(num, " fizz")
    elif (num % 5 == 0 and num != 0):
        print(num, " buzz")



