from pandas import DataFrame
import numpy as np

mydata=np.arange(9).reshape((3,3))
myframe = DataFrame(data=mydata, index=['a', 'b', 'c'])
columns=['ㄱ', 'ㄴ', 'ㄷ']

print(myframe)

sdata = {'용': {2020:10, 2021:20}}, {'마':{2020:30, 2021:40, 2022:50}}
myframe= DataFrame(sdata)
print(myframe)

sdata = {'지':['용','용','용','마','마'], '연':[2019, 2020, 2021, 2020, 2021], '실':[20, 30, 35, 25, 45]}
myframe = DataFrame(sdata)
print(myframe)

myframe.columns.name = 'c1'
print(myframe.columns)

myframe.index.name='i1'
print(myframe.index)

print(type(myframe.values))
print(myframe.values) 
    
 