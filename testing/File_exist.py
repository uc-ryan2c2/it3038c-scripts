import os.path
from os import path
 # This will check if you have the required log file
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








