str = "test python for"
mystr = str.split()
print(mystr)

for i in range(len(mystr)):
    if i%2==0:
        mystr[i]=mystr[i].upper()
    else:
        mystr[i]=mystr[i].lower()
print(mystr)

#join mystr#
res = '#'.join(mystr)
print(res)