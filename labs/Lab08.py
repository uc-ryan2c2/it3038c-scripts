import requests, re
from bs4 import BeautifulSoup

#this will scrape a website and output a list of the current major league soccer teams
data = requests.get("https://www.rookieroad.com/soccer/mls-teams-list/").content
soup = BeautifulSoup(data, 'html.parser')
#details = soup.find(href=re.compile('#'))
for link in soup.find_all('a', href=re.compile('#')):
    print(link['href'])
