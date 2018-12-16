from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pylab as plt
import numpy as np

data = make_blobs(n_samples=200, centers=2, random_state=8)
X, y = data
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
plt.show()

clf = KNeighborsClassifier()
clf.fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

plt.scatter(6.75, 4.82, marker='*', c='red', s=200)
plt.show()
print('新数据分类:', clf.predict([[6.75, 4.82]]))
