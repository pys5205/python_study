from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'

mylist=[3,2,4,3,6,5]
myindex=['강','김','이','안','윤','홍']

print(myindex)
print(mylist)

myseries=Series(data=mylist, index=myindex)
myylim=[0, myseries.max() +10]
myseries.plot(title='test score', kind='line', ylim=myylim, grid=True, rot=10, use_index=True)

filename='seriesGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'save finish')
plt.show()