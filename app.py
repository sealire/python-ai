import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from matplotlib.colors import colorConverter, ListedColormap

# 对于上面的fit可以这么扩展变成动态的
from sklearn.preprocessing import OneHotEncoder


def onehot(y, start, end):
    ohe = OneHotEncoder()
    a = np.linspace(start, end - 1, end - start)
    b = np.reshape(a, [-1, 1]).astype(np.int32)
    ohe.fit(b)
    c = ohe.transform(y).toarray()
    return c


#

def generate(sample_size, num_classes, diff, regression=False):
    np.random.seed(10)
    mean = np.random.randn(2)
    cov = np.eye(2)

    # len(diff)
    samples_per_class = int(sample_size / num_classes)

    X0 = np.random.multivariate_normal(mean, cov, samples_per_class)
    Y0 = np.zeros(samples_per_class)

    for ci, d in enumerate(diff):
        X1 = np.random.multivariate_normal(mean + d, cov, samples_per_class)
        Y1 = (ci + 1) * np.ones(samples_per_class)

        X0 = np.concatenate((X0, X1))
        Y0 = np.concatenate((Y0, Y1))
        # print(X0, Y0)

    if regression == False:  # one-hot  0 into the vector "1 0
        Y0 = np.reshape(Y0, [-1, 1])
        # print(Y0.astype(np.int32))
        Y0 = onehot(Y0.astype(np.int32), 0, num_classes)
        # print(Y0)
    X, Y = shuffle(X0, Y0)
    # print(X, Y)
    return X, Y


# Ensure we always get the same amount of randomness
np.random.seed(10)

input_dim = 2
num_classes = 3
X, Y = generate(20, num_classes, [[3.0], [3.0, 0]], False)
aa = [np.argmax(l) for l in Y]
colors = ['r' if l == 0 else 'b' if l == 1 else 'y' for l in aa[:]]

print(np.argmax(1))
print(np.shape(X))
print(np.shape(Y))
print(X)
print(Y)

plt.scatter(X[:, 0], X[:, 1], c=colors)
plt.xlabel("Scaled age (in yrs)")
plt.ylabel("Tumor size (in cm)")
plt.show()
