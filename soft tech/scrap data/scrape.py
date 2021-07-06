import requests
import csv

from bs4 import BeautifulSoup
 
result_page = requests.get('https://www.hltv.org/results').text

soup = BeautifulSoup(result_page, 'html.parser')
 
channels = soup.find("div", {"class": "results"}).find_all('div', recursive=False)[4:]
file = open('results.csv', 'wb')
writer = csv.writer(file)
 
# write title row
writer.writerow(['team1', 'result1', 'result2','team2'])
 
for channel in channels:
	team1 = channel.find('div', {'class':'team1'}).a.text.strip()
	result1 =  channel.find('div', {'class':'score-won'}).a.text.strip()
	result2 = channel.find('div', {'class':'team-lost'}).a.text.strip()
	team2 = channel.find('div', {'class':'team2'}).a.text.strip()

    #username = channel.find('div', attrs={'style': 'float: left; width: 350px; line-height: 25px;'}).a.text.strip()
    #uploads = channel.find('div', attrs={'style': 'float: left; width: 80px;'}).span.text.strip()
    #views = channel.find_all('div', attrs={'style': 'float: left; width: 150px;'})[1].span.text.strip()
    #writer.writerow([team1.encode('utf-8'), result1.encode('utf-8'), result2.encode('utf-8'), team2.encode('utf-8')])
 
file.close()