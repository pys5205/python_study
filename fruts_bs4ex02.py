from bs4 import BeautifulSoup

html = open("fruits.html", "r", encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
body=soup.select_one("body")
ptag=body.find('p')
print(ptag['class'])

ptag['class'][1] = 'white'

print(ptag['class'])

ptag['id']='apple'
print(ptag['id'])

body_tag = soup.find('body')
print(body_tag)

idx=0
for child in body_tag.children:
    idx+=1
    print(str(idx), child)

mydiv = soup.find("div")
print(mydiv)

mytag = soup.find("p", attrs='hard')
print(mytag)

print(mytag.find_parent())
      
parents=mytag.find_parents()
for p in parents:
    print(p.name)