import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 设置三维坐标
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x, y)  # XY平面的网格数据
Z = X + Y


print(X)
print(Y)
print(Z)
# 画3d图
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.jet)
plt.show()
