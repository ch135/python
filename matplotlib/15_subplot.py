import matplotlib.pyplot as plt

# example one
plt.figure(figsize=(6, 4))
plt.subplot(221)
plt.plot([0, 1], [0, 2])
plt.subplot(222)
plt.plot([0, 1], [0, 3])
plt.subplot(223)
plt.plot([0, 1], [0, 4])
plt.subplot(224)
plt.plot([0, 1], [0, 1])

# example two
plt.figure(figsize=(6, 4))
plt.subplot(211)
plt.plot([0, 1], [0, 2])
plt.subplot(234)
plt.plot([0, 1], [0, 3])
plt.subplot(235)
plt.plot([0, 1], [0, 4])
plt.subplot(236)
plt.plot([0, 1], [0, 1])

plt.tight_layout()
plt.show()