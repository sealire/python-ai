from scipy import linalg
import numpy as np

# 线性代数

a = np.array([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

x = linalg.solve(a, b)
print("solve:", x)
print()

A = np.array([[1, 2], [3, 4]])
x = linalg.det(A)
print("det:", x)
print()

A = np.array([[1, 2], [3, 4]])
l, v = linalg.eig(A)
print("eig:")
print(l)
print(v)
print()
