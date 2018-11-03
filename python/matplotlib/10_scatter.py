import matplotlib.pyplot as plt
import numpy as np

n = 1024
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
T = np.arctan2(y, x)

plt.scatter(x, y, s=75, c=T, alpha=0.5)
plt.xlim(-1, 1)
plt.ylim(-1, 1)
# 去除坐标轴数据
plt.xticks(())
plt.yticks(())

plt.show()