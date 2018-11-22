import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

I = np.array(np.arange(1, 1 + 20).reshape([1, 10, 2]), dtype=np.float32)
K = np.array(np.arange(1, 1 + 4), dtype=np.float32).reshape([2, 2, 1])
C = tf.nn.conv1d(I, K, 1, "SAME")

i = tf.constant([[[[2], [3], [8]],
                  [[6], [1], [5]],
                  [[7], [2], [-1]]]], tf.float32)
k = tf.constant([[[[4]], [[1]],
                  [[2]], [[3]]]], tf.float32)
c = tf.nn.conv2d(i, k, (1, 1, 1, 1), "SAME")

ii = tf.constant([[[[2], [3], [8], [5], [8]],
                   [[6], [1], [5], [9], [5]],
                   [[3], [7], [5], [1], [5]],
                   [[8], [2], [9], [1], [4]],
                   [[7], [2], [1], [7], [1]]]], tf.float32)
kk = tf.constant([[[[4]], [[8]], [[12]]],
                  [[[5]], [[10]], [[15]]],
                  [[[6]], [[12]], [[18]]]], tf.float32)
k1 = tf.constant([[[[4]]],
                  [[[5]]],
                  [[[6]]]], tf.float32)
k2 = tf.constant([[[[3]], [[2]], [[1]]]], tf.float32)
k2v = tf.reverse(k2, axis=[1])

cc = tf.nn.conv2d(ii, kk, (1, 1, 1, 1), "SAME")
c1 = tf.nn.conv2d(ii, k1, (1, 1, 1, 1), "SAME")
c2 = tf.nn.conv2d(c1, k2v, (1, 1, 1, 1), "SAME")
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print(sess.run(C))
    print(sess.run(c))
    print(sess.run(cc))
    print(sess.run(c2))
