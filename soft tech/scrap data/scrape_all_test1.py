from bs4 import BeautifulSoup 
import requests 
import csv
import pandas as pd

team_1 = [] 
result_1=[]
result_2=[]
team_2=[]


pages = list(range(0, 700, 100))
for page in pages:
	req = requests.get("https://www.hltv.org/results?offset={}".format(page)).text  # URL of the website which you want to scrape
  	#content = req.content # Get the content
	soup = BeautifulSoup(req,'html.parser')
  	#print(soup.prettify())
	t1 = soup.find_all('div' , class_='team-won')
	for i in range(len(t1)):
		team_1.append(t1[i].text)
	len(team_1)


print(len(team_1))