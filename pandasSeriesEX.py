from pandas import Series
import numpy as np

mylist = [10, 20, 30]
myindex = ['a', 'b', 'c']

myseries = Series(mylist)
print(myseries)

myseries = Series(data = mylist)
print(myseries)

myseries = Series(data=mylist, index=myindex)
print(myseries)

myseries = Series(data=mylist, index=myindex, dtype=np.float64)
print(myseries)

