from matplotlib import pyplot as plt
from matplotlib import style
x1=[5,8,10]
y1=[2,5,4]
x2=[6,9,15]
y2=[7,7,14]

plt.plot(x1,y1,'g',label='Team A',linewidth=1)
plt.plot(x2,y2,'c',label='Team B',linewidth=5)

plt.title('Team Performance')
plt.ylabel('Runs')
plt.xlabel('Overs')
#plt.legend()
plt.show()