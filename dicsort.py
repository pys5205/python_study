info = {'a':1, 'b':2, 'c':3, 'd':4}

myxticks = sorted(info, key=info.get, reverse=True)
print(myxticks)
reverse_key = sorted(info.keys(), reverse=True)
print(reverse_key)

#lambda
def nolambda(x, y):
    return 3*x+2*y
x, y = 3, 5

res = nolambda(x, y)
print(res)

yeslambda = lambda x, y:3*x+2*y
lamres = yeslambda(x, y)
print(lamres)