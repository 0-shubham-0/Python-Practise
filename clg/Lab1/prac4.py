from matplotlib import pyplot as plt
import numpy as np

a = np.array([45, 54, 68, 2, 4, 53, 76, 98])
plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
plt.title("Histogram")
plt.show()
