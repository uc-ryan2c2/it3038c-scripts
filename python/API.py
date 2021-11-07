import requests
import json

print('Please enter your zip code')
zip = input()

r = requests.get('https://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=5c34c38f3fe13e233c36a2e8a5effb68' % zip)
data = r.json()

print(type(data['weather'][0])) #this will print that data type
print(data['weather'][0]) #this will grab all weather data
