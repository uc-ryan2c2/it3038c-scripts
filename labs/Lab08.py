import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.rookieroad.com/soccer/mls-teams-list/").content
soup = BeautifulSoup(data, 'html.parser')
#details = soup.find(href=re.compile('#'))
for link in soup.find_all('a', href=re.compile('#')):
    print(link['href'])
