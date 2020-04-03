import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = x**2
y2 = 2*x + 1

plt.figure(figsize=(8, 5))
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
# 设置x, y范围；坐标轴标签
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel("I an X")
plt.ylabel("I am Y")
# 设置坐标轴分块距离
new_ticket = np.linspace(-1, 2, 5)
plt.xticks(new_ticket)
plt.yticks([-2, -1.8, -1, 1.22, 3], ["really bad", "bad", "normal", "good", "really", "good"])
# 设置坐标轴位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()