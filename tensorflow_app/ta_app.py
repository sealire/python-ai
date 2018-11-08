# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:56:26 2017

@author: 代码医生 qq群：40016981，公众号：xiangyuejiqiren
@blog：http://blog.csdn.net/lijin6249
"""

import tensorflow as tf
import numpy as np

X = tf.placeholder("float")
Y = tf.placeholder("float")

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])

mul = tf.matmul(X, Y)

with tf.Session() as sess:
    print(sess.run(mul, feed_dict={X: a, Y: b}))
