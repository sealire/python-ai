import tensorflow as tf
import numpy as np
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

sess = tf.Session()

zeros = tf.zeros([3, 4])
print("zeros: ")
print(sess.run(zeros))
print()

ones = tf.ones([5, 4])
print("ones: ")
print(sess.run(ones))
print()

fill = tf.fill([3, 4], 9)
print("fill: ")
print(sess.run(fill))
print()

cons = tf.constant([1, 2, 3])
print("cons: ")
print(sess.run(cons))
print()

cons1 = tf.constant(2, shape=[2])
print("cons1: ")
print(sess.run(cons1))
print()

cons2 = tf.constant(2, shape=[2, 2])
print("cons2:")
print(sess.run(cons2))
print()

cons3 = tf.constant([1, 2, 3], shape=[6])
print("cons3: ")
print(sess.run(cons3))
print()

cons4 = tf.constant([1, 2, 3], shape=[3, 2])
print("cons4: ")
print(sess.run(cons4))
print()

cons5 = tf.constant(3, shape=[4, 2])
print("cons5: ")
print(sess.run(cons5))
print()

zeros_like = tf.zeros_like(zeros)
print("zeros_like: ")
print(sess.run(zeros_like))
print()

ones_like = tf.ones_like(ones)
print("ones_like: ")
print(sess.run(ones_like))
print()

linear = tf.linspace(start=1.0, stop=2.0, num=5, name="linspace")
print("linear: ")
print(sess.run(linear))
print()

int_ran = tf.range(start=3, limit=9, delta=2)
print("int_ran: ")
print(sess.run(int_ran))
print()

randunif = tf.random_uniform([4, 3], minval=4, maxval=10)
print("rand: ")
print(sess.run(randunif))
print()

randnorm = tf.random_normal([4, 3], mean=0.0, stddev=1.0)
print("randnorm: ")
print(sess.run(randnorm))
print()

shuffled = tf.random_shuffle(randnorm)
print("shuffled: ")
print(sess.run(shuffled))
print()

cropped = tf.random_crop(randnorm, [3, 2])
print("cropped: ")
print(sess.run(cropped))
print()

v = tf.Variable(zeros)
init = tf.global_variables_initializer()
sess.run(init)
print("var: ")
print(sess.run(v))
print()

one = tf.placeholder(tf.float32)
two = tf.placeholder(tf.float32)
three = tf.add(one, two)
print("placeholder: ")
print(sess.run(three, feed_dict={one: 10, two: 30}))
print()

x = tf.placeholder(tf.float32, shape=[4, 4])
y = tf.identity(x)
xv = np.random.rand(4, 4)
print("placeholder: ")
print(sess.run(y, feed_dict={x: xv}))

mat = tf.diag([1.0, 1.0, 1.0])
print("diag: ")
print(sess.run(mat))
print()

ctt = tf.convert_to_tensor(np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]]))
print("convert_to_tensor: ")
print(sess.run(ctt))
print()

A = tf.constant([1.0, 2., 3., 4., 1., 6., 7., 1., 9.], shape=[3, 3])
print("matrix add, multiply: ")
print(sess.run(A))
print(sess.run(A + A))
print(sess.run(tf.matmul(A, A)))
print()

print("transpose: ")
print(sess.run(tf.transpose(A)))
print()

print("matrix_determinant: ")
print(sess.run(tf.matrix_determinant(A)))
print()

print("matrix_inverse: ")
print(sess.run(tf.matrix_inverse(A)))
print()

print("cholesky:")
print(sess.run(tf.cholesky(mat)))
print()

print("self_adjoint_eig: ")
print(sess.run(tf.self_adjoint_eig(A)))
print()

print("div: 3 / 4 = ", sess.run(tf.div(3, 4)))
print("truediv: 3 / 4 = ", sess.run(tf.truediv(3, 4)))
print("floordiv: 3 / 4 = ", sess.run(tf.floor_div(3.0, 4.0)))
print("mod: 22 % 5 = ", sess.run(tf.mod(22, 5)))
print("cross: ", sess.run(tf.cross([1., 0., 0.], [0., 1., 0.])))

print(sess.run(tf.nn.relu([-3, 3, 10])))
print(sess.run(tf.nn.relu6([-3, 3, 10])))
print(sess.run(tf.nn.sigmoid([-1., 0, 1.])))
