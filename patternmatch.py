import re
mylist=['ab123', 'cd456', 'ef789', 'abc12']

regex='[a-z]{2}\d{3}'
pattern=re.compile(regex)

totallist=[]
for i in mylist:
    if pattern.match(i):
        totallist.append(i)
        print(i)
    else:
        print(i, "not")
print(totallist)