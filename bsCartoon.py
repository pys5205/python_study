from urllib.request import urlopen
from bs4 import BeautifulSoup

myurl = 'http://comic.naver.com/webtoon/weekday'

response = urlopen(myurl)

print(type(response))

soup = BeautifulSoup(response, 'html.parser')

title =soup.find("title").string
print(title)

