import matplotlib.pyplot as ply
import numpy as np

x = np.arange(0, 5 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
x1 = np.arange(0, 10)
y1 = x1 + 2 * x1

ply.subplot(1, 3, 1)

ply.plot(x, y_sin)
ply.title('Sine')

ply.subplot(1, 3, 2)
ply.plot(x, y_cos)
ply.title('Cosine')

ply.show()
