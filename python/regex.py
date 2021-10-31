import requests, re

data = "Hello, my emial is ryan2c2@mail.cu.edu.  Please contect me!"
email = re.compile('[A-Za-z0-9_%.-]+@[A-z0-9_%.-]+\.[A-z0-9]{2,}')
print(email.search(data).group())
