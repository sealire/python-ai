import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

# 梯度下降

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = tf.Variable(4.0, tf.float32)
f = tf.pow(x - 1, 2)

v = np.arange(-3, 5, 0.05)
yv = np.power(v - 1, 2.0)
plt.plot(v, yv)

opti = tf.train.GradientDescentOptimizer(0.05).minimize(f)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for i in range(30):
        sess.run(opti)
        xv = sess.run(x)
        print(xv)

        plt.plot(xv, np.power(xv - 1, 2.0), 'go')

plt.show()