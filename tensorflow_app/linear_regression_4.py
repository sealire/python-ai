# -*- coding: utf-8 -*-
"""
    2018-11-08
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 生成模拟数据
train_X = np.float32(np.linspace(-2 * np.pi, 2 * np.pi, 200))
train_Y = 2 * np.sin(train_X) + np.random.randn(*train_X.shape) * 0.2  # y=2x，但是加入了噪声
# 图形显示
# plt.plot(train_X, train_Y, 'ro', label='Original data')
# plt.legend()
# plt.show()

# 创建模型

# 模型参数
W = tf.Variable(tf.random_normal([1]), name="weight")
b = tf.Variable(tf.zeros([1]), name="bias")
# 前向结构
z = tf.multiply(W, tf.sin(train_X)) + b

# 反向优化
cost = tf.reduce_mean(tf.square(train_Y - z))
learning_rate = 0.01
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)  # Gradient descent

# 初始化变量
init = tf.global_variables_initializer()
# 参数设置
training_epochs = 20

# 启动session
with tf.Session() as sess:
    sess.run(init)

    # Fit all training data
    for epoch in range(training_epochs):
        print()
        print("init:", epoch + 1, "W=", sess.run(W), "b=", sess.run(b))

        for step in range(train_X.size):
            sess.run(optimizer)

        # 显示训练中的详细信息
        loss = sess.run(cost)
        print("Epoch:", epoch + 1, "cost=", loss, "W=", sess.run(W), "b=", sess.run(b))

    print(" Finished!")
    print("cost=", sess.run(cost), "W=", sess.run(W), "b=", sess.run(b))

    # 图形显示
    plt.plot(train_X, train_Y, 'ro', label='Original data')
    plt.plot(train_X, sess.run(W) * np.sin(train_X) + sess.run(b), label='Fitted line')
    plt.legend()
    plt.show()
