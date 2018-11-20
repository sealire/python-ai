import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# 二元梯度下降

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = tf.Variable(tf.constant([-8, 8], tf.float32), tf.float32)
f = tf.reduce_sum(tf.square(x))

fig = plt.figure()
ax = Axes3D(fig)

# 生成数据
xx = np.linspace(-10, 10, 100)
yy = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(xx, yy)  # XY平面的网格数据
Z = X ** 2 + Y ** 2

# 画3d图
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.jet)

opti = tf.train.GradientDescentOptimizer(0.05).minimize(f)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(30):
        sess.run(opti)

        xv = sess.run(x)
        # print(tf.reduce_sum(tf.square(xv)))
        fv = sess.run(tf.reduce_sum(tf.square(xv)))
        ax.scatter([xv[0]], [xv[1]], [fv], color='r')
        # plt.plot(xv, fv, 'go')
        print(xv)
        print([fv]
)
plt.show()
