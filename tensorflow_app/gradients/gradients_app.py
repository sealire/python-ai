import tensorflow as tf
import numpy as np
import os

# 计算梯度

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x = tf.placeholder(tf.float32, [2, 1])
w = tf.constant([[3, 4]], tf.float32)

y = tf.matmul(w, x)

f = tf.pow(y, 2)

grads = tf.gradients(f, x)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print(sess.run(grads, {x: np.array([[2], [3]])}))
