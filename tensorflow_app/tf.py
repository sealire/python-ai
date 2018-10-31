import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

v = tf.Variable(tf.zeros([2, 3]))
s = tf.Session()

init = tf.global_variables_initializer()
s.run(init)

x = tf.placeholder(tf.float32, shape=[2, 2])
y = tf.identity(x)
xv = np.random.rand(2, 2)
s.run(y, feed_dict={x: xv})
