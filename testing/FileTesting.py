import os.path
from os import path

#function that checks if a file is there
def main():

   print ("File exists:"+str(path.exists('guru99.txt')))

if __name__== "__main__": #boilerplate code that protects users from accidentally invoking the script when they didn't intend to
   main()




#variable that checks if a file is there and if it is not, it will create it
file_exist = str(path.exists('guru99.txt'))
print(file_exist)

if file_exist == 'False':
    f = open('guru99.txt', 'w')
    f.write("PASSCODES")
    f.close
else:
    print("Looks like you already have a stored file :)")



#this will create a file in the current directory and then read the file.
def writeText():
    textFile = open("test.txt","w")
    textFile.write("\n test")
    textFile.close()
def readText():
    textFile = open("test.txt","r")
    store = textFile.readlines()
    print(store)

writeText()
readText()

