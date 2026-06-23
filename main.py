import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 1)
y = x ** 2

plt.plot(x, y)
plt.title("Square Numbers")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
import sys
print(sys.executable)