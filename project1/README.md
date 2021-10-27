<h1>Passcode Generator Project</h1>
<b>
This script will generate a password for any application that you need a password for.
After the password is generated, you will then be able to store it in a text file and then encrypt that file so it is secure!
</b>

<h3>How the scripts run</h3>
<b>
First, Copy and paste the code into your perfered Python IDE so that you are able to run it.
You do not need anything pre-installed but made sure you have Python version 3.5 and up.
</b>

<b>
when you first run the code, it will check if the required log file to store the passwords is on your computer in the current directroy that you are in.
If the file is not there, the script will generate a log file in the current directory.
</b>
<b>
Next, the script will ask you if you want to generate a password, Encrypt your passsword file, Decrypt your password file, or quit.
Below is what the options will look like, Please press either 1, 2, 3, or 4.
```
Please select an option.     
1. Generate Password
2. Encrypt File
3. Decrypt File
4. Quit
```
</b>
<b>
By selecting 1, it will ask you if you want to generate a new password.  Please type in yes or no and then follow to the next prompt.
Next, it will ask you what applicaiton this password is for so you will easily be able to know what application you generated that password for.
The script will then ask if you want special characters in the password.  Sometimes, applications has password criteria whether it needs special characters or it does not. Please select either 1 or 2.  1 for special characters, 2 for none.
Next, it will generate and show you your password along with asking if you want to store this password in your password file.
Please select 1 to store the password or 2 to skip and not store the password.
Finally it will ask if you want a new password again.  If you do not, please select no and it will bring you back to the four begining options.
Your Password file will be in the same directory that you are running the Python code in. To see the file, head to that directory and find the file named PassList.txt

NOTE - For some reason, the first time you run this code it might not generate the passwords in the file.  If that happens, run it again and you will be good to go from then on.
</b>
<b>
Next, you will want to encode the text file storing your passwords to make it much safer.  Either run the script again and select 2 to encrypt the password file or select 2 if the script is still running.
Below is what the script will look like when you select encrypt.
```
Please enter a key to encrypt or decrypt your password file.
Key neede to be between 1-255.
NOTE - PLEASE MAKE SURE TO REMEBER YOUR KEY TO DECRYPT YOUR PASSWORD FILE
Key: 32
```
The script will ask for a key between 1-255.  This key will be the key that will encrypt your password file.  each key will encrypt the file a different way.
PLEASE NOTE, DO NOT FORGET THIS KEY BECAUSE YOU WILL NEED IT TO DECRYPT YOUR FILE
Once the key is entered, your password file will change from PassList.txt -> EC-PassList.txt.  This is to show you that the file is now encrypted.

PLEASE NOTE - If you want to add another password to this encrypted file, you will first have to decrypt the file. The new password will then be added to the next line in EC-PassList.txt.

once PassList.txt has changed to EC-PassList.txt, that will be your permanent new file name.  Running the script again will not generate a new file, it will simply add on to EC-PassList.txt
</b>
<b>
Finally, We will want to decrypt the file to access the password wihtin it.  Run the script and select option 3 to decrypt the file.  Below is the prompt that will show up.  Please enter the Key that you FIRST used to decrypt the password.
```
Please enter a key to encrypt or decrypt your password file.
Key need to be between 1-255.
NOTE - PLEASE MAKE SURE TO REMEBER YOUR KEY TO DECRYPT YOUR PASSWORD FILE
Key: 32
```
The file will then be decrypted and you will be able to see the contents within the file.

That is the whole script! Thank you!
</b>
