
import requests
from bs4 import BeautifulSoup
import re
import os
import pandas as pd

cookies = None

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'} 
baseurl = 'https://www.hltv.org/results'

session = requests.session()

for i in range(0, 700, 100):
    if i > 0:
        baseurl = baseurl + '?offset=' + str(i)

    if cookies is not None:
        session.cookies = cookies
        # check if already logged in by visiting the site
    result_page = session.request('GET', baseurl, headers=headers, verify=False).text

    if cookies is None:
        cookies = session.cookies
    #result_page = requests.get(verify=False).text
    #print(result_page)
    soup = BeautifulSoup(result_page, 'html.parser')
    res = soup.find('div', {'class': 'results-all'})
    #print(res)
    items= res.find_all('div', {'class': 'result'})
    print(items[0])
    #print(items[0].find('div', {'class': 'team1'}).get_text())

    team_1 = [item.find('div', {'class': 'team-won'}).get_text() for item in items]
    result_1 = [item.find('span', {'class': 'score-won'}).text.strip() for item in items]
    result_2 = [item.find('span', {'class': 'score-lost'}).text.strip() for item in items]
    team_2 = [item.find('div', {'class': 'team'}).get_text() for item in items]

    result_stuff = pd.DataFrame(
        {
        'team_1': team_1,
        'result_1': result_1,
        'result_2': result_2,
        'team_2': team_2
        })

    result_stuff.to_csv('results_all.csv')


