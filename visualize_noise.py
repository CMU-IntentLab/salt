import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

n00 = np.load('n00.npy')
n01 = np.load('n01.npy')
n03 = np.load('n03.npy')

x0 = n00[:,0]
y0 = n00[:,1]
z0 = n00[:,2]

x1 = n01[:, 0]
y1 = n01[:, 1]
z1 = n01[:, 2]

x3 = n03[:, 0]
y3 = n03[:, 1]
z3 = n03[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x0, y0, z0, c='g', marker='*', s=200, label='No Noise')
ax.scatter(x1, y1, z1, c='r', marker='o', label='Noise 0.1')
ax.scatter(x3, y3, z3, c='b', marker='^', label='Noise 0.3')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Noise lvls')

ax.legend()
plt.show()
plt.savefig('noise_comparison.png')

