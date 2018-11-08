import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

####################################################################
# 设置三维坐标
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)  # XY平面的网格数据
Z = X ** 2 + Y ** 2

# 画3d图
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.jet)
plt.show()

####################################################################
# 设置三维坐标
fig = plt.figure()
ax = Axes3D(fig)

# 定义x, y
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X ** 2 + Y ** 2)

# 计算Z轴的高度
Z = np.sin(R)

# 绘制3D曲面
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# 绘制从3D曲面到底部的投影
ax.contour(X, Y, Z, zdim='z', offset=-2, cmap='rainbow')

# 设置z轴的维度
ax.set_zlim(-2, 2)

plt.show()

####################################################################
# 设置三维坐标
fig = plt.figure()
ax = Axes3D(fig)

# 生成数据
x = np.arange(0, 100)
y = np.arange(0, 100)
x, y = np.meshgrid(x, y)
z = np.random.randint(0, 100, size=(100, 100))
y3 = np.arctan2(x, y)

ax.scatter(x, y, z, marker='.', s=50, label='')
plt.show()

####################################################################
# 设置三维坐标
fig = plt.figure()
ax = fig.gca(projection='3d')

# 正文体顶点和面
verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]
faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [1, 2, 6, 5], [2, 3, 7, 6], [0, 3, 7, 4]]
# 四面体顶点和面
# verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 0, 1)]
# faces = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
# 获得每个面的顶点
poly3d = [[verts[vert_id] for vert_id in face] for face in faces]
# print(poly3d)

# 绘制顶点
x, y, z = zip(*verts)
ax.scatter(x, y, z)
# 绘制多边形面
ax.add_collection3d(Poly3DCollection(poly3d, facecolors='w', linewidths=1, alpha=0.3))
# 绘制对变形的边
ax.add_collection3d(Line3DCollection(poly3d, colors='k', linewidths=0.5, linestyles=':'))

# 设置图形坐标范围
ax.set_xlabel('X')
ax.set_xlim3d(-0.5, 1.5)
ax.set_ylabel('Y')
ax.set_ylim3d(-0.5, 1.5)
ax.set_zlabel('Z')
ax.set_zlim3d(-0.5, 1.5)
plt.show()

####################################################################
# 设置三维坐标
fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.5, color='b')
cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)
plt.show()

####################################################################
# 设置三维坐标
fig = plt.figure()
ax = fig.gca(projection='3d')

n_angles = 200
n_radii = 40
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2 * np.pi, n_angles, endpoint=False)
angles = np.repeat(angles[..., np.newaxis], n_radii, axis=1)
x = np.append(0, (radii * np.cos(angles)).flatten())
y = np.append(0, (radii * np.sin(angles)).flatten())
z = np.sin(-x * y)
ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.2)
plt.show()
