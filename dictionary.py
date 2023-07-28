dic1 = {'a':1, 'b':2, 'c':3}
print(dic1)

#for문 dictionary keys, value, items
for i in dic1.keys():
    print(i)
for j in dic1.values():
    print(j)
for i, j in dic1.items():
    print('{} , {}'.format(i, j))

#dictionary find
findkey = 'b'
if findkey in dic1:
    print('{}, Y'.format(findkey))
else:
    print('{}, N'.format(findkey))

# key pop
res = dic1.pop('b')
print(dic1)
print(res)