import matplotlib.pyplot as plt

figure = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

left, bottom, width, height = .1, .1, .8, .8
ax1 = figure.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_xlabel("ax1_x")
ax1.set_ylabel("ax1_y")
ax1.set_title("ax1_title")

ax2 = figure.add_axes([.2, .6, .25, .25])
ax2.plot(y, x, 'b')
ax2.set_xlabel("ax2_x")
ax2.set_ylabel("ax2_y")
ax2.set_title("title inside 1")

plt.axes([.6, .2, .25, .25])
plt.plot(y[::-1], x, 'g')
plt.xlabel("x")
plt.ylabel("y")
plt.title("title inside 2")

plt.show()
