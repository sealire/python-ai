import numpy as np

# 基础函数

a = np.array([1, 2, 3])
print(a)
print()

a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)
print()

a = np.array([1, 2, 3, 4, 5], ndmin=2)
print(a)
print()

a = np.array([1, 2, 3], dtype=complex)
print(a)
print()

dt = np.dtype(np.int32)
print(dt)
print()

dt = np.dtype('i8')
print(dt)
print()

# <意味着编码是小端(最小有效字节存储在最小地址中)。>意味着编码是大端(最大有效字节存储在最小地址中)
dt = np.dtype('>i4')
print(dt)
print()

dt = np.dtype([('age', np.int8)])
print(dt)
print()

dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)
print()

dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])
print()

student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
print()

a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(a)
print(b)
a.shape = (3, 2)
print(a)
print()

a = np.arange(24)
b = a.reshape(2, 4, 3)
print(b)
print(b.ndim)
print(b.itemsize)
print()
