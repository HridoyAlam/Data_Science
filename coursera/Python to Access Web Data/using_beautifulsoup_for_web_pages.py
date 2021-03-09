import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from bs4.builder import HTML


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter- ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))