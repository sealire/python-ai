# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf

# ---------------------------------------------------------------------------------------------
# 输入层，第0层
x = tf.placeholder(tf.float32, shape=[None, 2])
# 第0层到第1层的权重
w1 = tf.Variable(tf.constant([
    [1.0, 4.0, 7.0],
    [2.0, 5.0, 8.0]], tf.float32))
# 第1层的偏置
b1 = tf.Variable(tf.constant([3.0, 6.0, 9.0], tf.float32))
# 第1层的线性组合
l1 = tf.matmul(x, w1) + b1
# 第1层的激活
sigmal = l1

# ---------------------------------------------------------------------------------------------
# 第1层到第2层的权重
w2 = tf.Variable([
    [9.0, 7.0, 3.0],
    [6.0, 4.0, 5.0],
    [5.0, 2.0, 8.0]], tf.float32)
# 第2层的偏置
b2 = tf.Variable(tf.constant([4.0, 1.0, 4.0], tf.float32))
# 第2层的线性组合
l2 = tf.matmul(sigmal, w2) + b2
# 第2层的激活
sigma2 = l2

# ---------------------------------------------------------------------------------------------
# 第2层到第3层的权重
w3 = tf.Variable([
    [1.0, 4.0],
    [6.0, 8.0],
    [8.0, 1.0]], tf.float32)
# 第3层的偏置
b3 = tf.Variable(tf.constant([2.0, 3.0], tf.float32))
# 第3层的线性组合
l3 = tf.matmul(sigma2, w3) + b3

# ---------------------------------------------------------------------------------------------
# 构造函数F
F = tf.pow(tf.reduce_sum(l3), 2.0)

# ---------------------------------------------------------------------------------------------
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# 计算梯度
w1_gra, b1_gra, w2_gra, b2_gra, w3_gra, b3_gra = tf.gradients(F, [w1, b1, w2, b2, w3, b3])
w1_gra_arr, b1_gra_arr, w2_gra_arr, b2_gra_arr, w3_gra_arr, b3_gra_arr = sess.run(
    [w1_gra, b1_gra, w2_gra, b2_gra, w3_gra, b3_gra], feed_dict={x: np.array([[2.0, 3.0]], np.float32)})

# ---------------------------------------------------------------------------------------------
print("关于第1层权重的梯度：")
print(w1_gra_arr)
print("关于第1层偏置的梯度：")
print(b1_gra_arr)

print("关于第2层权重的梯度：")
print(w2_gra_arr)
print("关于第2层偏置的梯度：")
print(b2_gra_arr)

print("关于第3层权重的梯度：")
print(w3_gra_arr)
print("关于第3层偏置的梯度：")
print(b3_gra_arr)
