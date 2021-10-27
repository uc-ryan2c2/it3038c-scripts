## this file will output a list of IP addresses based on a host name

import socket

host = ['www.uc.edu', 'www.google.com', 'www.8451.com', 'www.twitter.com', 'www.youtube.com', 'www.shawfloors.com']

print("working from host: " + socket.getfqdn()) #this will get the host name of the machine this script is running on

for name in host:
    print(name + " -- " + socket.gethostbyname(name)) #this will get the IP of the host