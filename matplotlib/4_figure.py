import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = x**2
y2 = 2*x + 1

plt.figure()
plt.plot(x, y1)
plt.figure(num=2, figsize=(8, 5))
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=1.0, linestyle='--')
plt.show()