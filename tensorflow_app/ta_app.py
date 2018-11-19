import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

c = tf.constant([[1, 2, 3], [4, 5, 6]], tf.float32, name='c')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    print(sess.run(c))
    print(sess.run(tf.transpose(c, perm=[1, 0])))
    print(sess.run(tf.slice(c, [0, 1], [2, 2])))
