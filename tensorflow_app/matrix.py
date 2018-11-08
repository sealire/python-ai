import tensorflow as tf
import numpy as np

X = tf.placeholder("int32")
Y = tf.placeholder("int32")

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[1, 2], [3, 4], [5, 6]])

mul = tf.matmul(X, Y)
nmul = tf.multiply(X, 5)

with tf.Session() as sess:
    print("mul: ")
    print(sess.run(mul, feed_dict={X: a, Y: b}))
    print("nmul: ")
    print(sess.run(nmul, feed_dict={X: a}))
