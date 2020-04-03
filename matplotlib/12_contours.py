import matplotlib.pyplot as  plt
import numpy as np

# 计算等高线数据
def count(x,y):
    result = (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    return result

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# meshgrid函数将两个输入的数组x和y进行扩展，前一个的扩展与后一个有关，后一个的扩展与前一个有关，前一个是竖向扩展，后一个是横向扩展
X, Y = np.meshgrid(x, y)

# contourf：填充等高线之间的空隙
plt.contourf(X, Y, count(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

# contour：填充等高线
C = plt.contour(X, Y, count(X, Y), 8, c='black', lw=.5)
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()