from matplotlib import pyplot as plt

x1 = [2005, 2008, 2010]
y1 = [2000, 5000, 4000]
x2 = [2006, 2009, 2011]
y2 = [1000, 2000, 1400]

plt.bar(x1, y1, color='g', align='center', label='India')
plt.bar(x2, y2, color='c', align='center', label='SriLanka')
plt.title('Population')
plt.ylabel('Count')
plt.xlabel('Year')
plt.legend()
plt.show()
