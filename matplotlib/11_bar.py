import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(12)
Y1 = (1-X/float(n))*np.random.uniform(0.5, 1.0, n)
Y2 = (1-X/float(n))*np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor="#9999ff", edgecolor='white')
plt.bar(X, -Y2, facecolor="#ff9999", edgecolor='white')
for x, y in zip(X, Y1):
    # ha: horizontal alignment 水平方向
    # va: vertical alignment 垂直方向
    plt.text(x, y+0.10, "%.2f" % y, ha="center", va="top")
for x, y in zip(X, Y2):
    plt.text(x, -y-0.10, "%.2f" % y, ha="center", va="bottom")
plt.xlim((-.5, n))
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())
plt.show()