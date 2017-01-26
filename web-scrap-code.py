import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.timesofindia.com')

soup = BeautifulSoup(r.text)

for d in soup.find_all('h2'):
	print d