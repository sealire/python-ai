import numpy as np

# 数组操作

a = np.arange(8)
print("a:")
print(a)
print()

b = a.reshape(4, 2)
print("b:")
print(b)
print()

print("flat:")
print(a.flat[:])
print()

print("flatten:")
print(a.flatten())
print()

print("ravel:")
print(a.ravel())
print()

print("transpose:")
print(np.transpose(b))
print()

print("b.T:")
print(b.T)
print()

a = np.arange(120).reshape(2, 3, 4, 5)
print("rollaxis:")
print(np.rollaxis(a, 2))
print()

print("rollaxis 2:")
print(np.rollaxis(a, 2, 1))
print()

a = np.arange(24).reshape(2, 3, 4)
print("swapaxes:")
print(np.swapaxes(a, 2, 1))
print()

a = np.arange(4).reshape(1, 4)
print("broadcast_to:")
print(np.broadcast_to(a, (4, 4)))
print()
