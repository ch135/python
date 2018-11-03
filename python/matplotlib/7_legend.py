import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = x**2
y2 = 2*x + 1

plt.figure(figsize=(8, 5))
# l1,l2之后一定要加,
l1, = plt.plot(x, y1, label="l1")
l2, = plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--', label='l2')
# plt.legend() #默认输出
plt.legend(handles=[l1, l2], labels=['up', 'down'], loc='best')
plt.show()
"""
The *loc* location codes are::
          'best' : 0,          (currently not supported for figure legends)
          'upper right'  : 1,
          'upper left'   : 2,
          'lower left'   : 3,
          'lower right'  : 4,
          'right'        : 5,
          'center left'  : 6,
          'center right' : 7,
          'lower center' : 8,
          'upper center' : 9,
          'center'       : 10,"""
