import pandas as pd
from requests_html import HTMLSession

from bs4 import BeautifulSoup

s = HTMLSession()

url = 'https://www.hltv.org/results'

def getData(url):
	r = s.get(url)
	r.html.render(sleep = 1)
	soup = BeautifulSoup(r.html.html, 'html.parser')
	return soup

p = list(range(1,600))
def getNextPage(soup):
	pages = soup.find('span', {'class': 'pagination-data'})

	for i in p:
		url = 'https://www.hltv.org' + str(pages.find('a', {'class': 'pagination-next'}).find('a')['href'])
		
		return url

while True:
	data = getData(url)
	url = getNextPage(data)
	if not url:
		break

	print(url)