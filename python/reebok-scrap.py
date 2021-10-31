import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.microcenter.com/product/637200/lenovo-legion-5-17ach6h-173-gaming-laptop-computer-platinum-collection-blue").content
soup = BeautifulSoup(data, 'html.parser')
details = soup.find("h1")
print(details)

