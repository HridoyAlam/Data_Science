import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
count = 0
sum = 0
tags = soup('span')
for tag in tags:
    x = int(tag.text)
    count +=1
    sum +=x
print(f"Count {count}")
print(f"Sum {sum}")

##test link1:: http://py4e-data.dr-chuck.net/comments_42.html
##test link2:: http://py4e-data.dr-chuck.net/comments_1166789.html