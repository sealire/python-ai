import numpy as np

# 切片和索引函数

a = np.arange(10)
s = slice(2, 7, 2)
print("slice: ")
print(a[s])
print()

print("slice 2: ")
b = a[2:7:2]
print(b)
print()

print("slice 3: ")
print(a[5])
print(a[4:])
print(a[3:6])
print()

a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print("a: ")
print(a)
print()

print("第二列：")
print(a[..., 1])
print("第二行：")
print(a[1, ...])
print('第二列及其剩余元素：')
print(a[..., 1:])

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print("高级索引：")
print("x: ")
print(x)
print("y: ")
print(y)

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print("高级索引 2：")
print("x: ")
print(x)
print("y: ")
print(y)

z = x[1:4, 1:3]
y = x[1:4, [1, 2]]
print("高级索引 3：")
print("z: ")
print(z)
print("y: ")
print(y)
print()

print("布尔索引:")
print(x[x > 5])
print()

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print("布尔索引 2: ")
print(a[~np.isnan(a)])
print()

a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print("布尔索引 3: ")
print(a[np.iscomplex(a)])
