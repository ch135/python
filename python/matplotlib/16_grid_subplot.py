import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method1:subbplot2grid
plt.figure()
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot([0, 0], [1, 2])
ax1.set_title("ax1_title")
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel("ax4_x")
ax4.set_ylabel("ax4_y")
ax5 = plt.subplot2grid((3, 3), (2, 1))

# method2: gridppec
plt.figure()
gs = gridspec.GridSpec(3, 3)
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
sx9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

# method3
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])


# 调整子图位置,排除堆叠
plt.tight_layout()
plt.show()