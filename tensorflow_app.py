import tensorflow as tf

# 首先，创建一个TensorFlow常量=>2
const = tf.constant(2.0, name='const')

# 创建TensorFlow变量b和c
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, dtype=tf.float32, name='c')

print(const)
print(b)
print(c)
