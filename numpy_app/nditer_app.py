import numpy as np

# 迭代器函数

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print("a:")
print(a)
print()

print("nditer:")
for x in np.nditer(a):
    print(x, end=", ")
print()

b = a.T
print("nditer 2:")
for x in np.nditer(b):
    print(x, end=", ")
print()

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print("nditer 3:")
print(a)
print()

b = np.array([1, 2, 3, 4], dtype=int)
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=",")
