from scipy.cluster.vq import kmeans, vq, whiten
from numpy import vstack, array
from numpy.random import rand

# 聚类函数

data = vstack((rand(100, 3) + array([.5, .5, .5]), rand(100, 3)))
print("data:")
print(data)
print()

data = whiten(data)
print("whiten:")
print(data)
print()

centroids, _ = kmeans(data, 3)
print("centroids:")
print(centroids)
print()

clx, _ = vq(data, centroids)
print("clx:")
print(clx)
print()
