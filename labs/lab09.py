from ast import Index
import requests
import json

r = requests.get("http://localhost:3000")
data = r.json()

#print(type(data['name'][0])) #this will print that data type
#print(data['name'][0]) #this will grab all weather data

print(data[0]["name"], "is", data[0]["color"])
print(data[1]["name"], "is",  data[1]["color"])
print(data[2]["name"], "is",  data[2]["color"])
