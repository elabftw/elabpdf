#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2012, 2020)
y = [10, 20, 50, 100, 300, 1400, 5000, 12000]

plt.xkcd()
plt.plot(x, y)
plt.title('Evolution of eLabFTW users over time')
plt.xlabel('Years')
plt.ylabel('Number of users')
plt.show()
