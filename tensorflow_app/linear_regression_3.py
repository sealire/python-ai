# -*- coding: utf-8 -*-

__author__ = "代码医生"

"""
    2018-11-08
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
train_X = np.linspace(-1, 1, 100)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.2  # y=2x，但是加入了噪声

# 创建模型
# 占位符
X = tf.placeholder("float")
Y = tf.placeholder("float")
# 模型参数
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.zeros([1]), name="bias")

# 前向结构
z = tf.multiply(X, W) + b

saver = tf.train.Saver()  # 生成saver
savedir = "log/"

# 启动session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver.restore(sess, savedir + "linermodel.cpkt")

    print("W=", sess.run(W), "b=", sess.run(b))
    print("x=0.2，z=", sess.run(z, feed_dict={X: 0.2}))

    # 图形显示
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()
