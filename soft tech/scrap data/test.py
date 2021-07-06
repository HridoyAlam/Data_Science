import requests
from bs4 import BeautifulSoup

import re
import os


agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'

def getPage(link):
    f_res = requests.get(link, headers={'User-Agent': agent}, timeout=10)
    if f_res.status_code == 200:
        return f_res.text
    else:
        # print(f_res.status_code)
        return None

link = 'https://www.hltv.org/results'


soup = BeautifulSoup(getPage(link), 'html.parser')
res = soup.find('div', {'class': 'results'})
#print(res)
items= res.find_all('div', {'class': 'result'})
print(items[0])
#print(items[0].find('div', {'class': 'team1'}).get_text())