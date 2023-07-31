import re
from bs4 import BeautifulSoup

myencoding = 'utf-8'
myparser = 'html.parser'
filename = 'css01.html'

html = open(filename , encoding=myencoding)
soup = BeautifulSoup(html, myparser)


h1 = soup.select_one("div#cartoon > h1").string
print("h1 = ", h1)

li_list = soup.select("div#cartoon > ul.elements > li")
for li in li_list:
    print("li = ", li.string)

choice = lambda x : print(soup.select_one(x).string)

print('\nchoice("#item5"): ', end='')
choice("#item5")

print('\nchoice("li#item4"): ', end='')
choice("li#item4")

print('\nchoice("ul > li#item3"): ', end='')
choice("ul > li#item3")

print('\nchoice("#itemlist #item2"): ', end='')
choice("#itemlist #item2")

print('\nchoice("#itemlist > #item3"): ', end='')
choice("#itemlist > #item3")

print('\nchoice("ul#itemlist > li#item2"): ', end='')
choice("ul#itemlist > li#item2")

print('\nchoice("li[id=item1]"): ', end='')
choice("li[id=item1]")

print('\nchoice("li:nth-of-type(4)"): ', end='')
choice("li:nth-of-type(4)")

print('\nsoup.select("li"[1].string :', end='')
print(soup.select("li")[1].string)

print('\nsoup.find_all("li")[3].string : ', end='')
print(soup.find_all("li")[3].string)

mytag = soup.select_one('div#cartoon > ul.elements')
mystring = mytag.select_one('li:nth-of-type(3)').string
print(mystring)

mytag = soup.select_one('ul#itemlist')
mystring = mytag.select_one('li:nth-of-type(4)').string
print(mystring)

print(soup.select("#vegatables > li[class='us']")[0].string)
print(soup.select("#vegatables > li.us")[1].string)

result = soup.select('a[href$=".com"]')
for item in result:
    print(item['href'])
result = soup.select('a[href*="daum"]')
for item in result:
    print(item['href'])

cond = {"id":"ko", "class":"cn"}
print(soup.find("li", cond).string)

print(soup.find(id="vegatables").find("li", cond).string)

li = soup.find_all(href=re.compile(r"^https://"))
for e in li:
    print(e.attrs['href'])

print('\n# finished')