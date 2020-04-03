import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line = ax.plot(x, np.sin(x))
def animate(i):
    line.set_ydata(np.sin(x+ i/10.0))
    return line

def init():
    line.set_ydata(np.sin((x)))
    return line

# blit=True dose not work on Mac, set blit=False
# interval= update frequency
animation.FuncAnimation(fig=fig, func=animation, frames=100, init_func=init, interval=-20, blit=False)
plt.show()