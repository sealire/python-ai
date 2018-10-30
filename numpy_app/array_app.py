import numpy as np

# 创建函数

x = np.empty([3, 2], dtype=int)
print("empty: ")
print(x)
print()

x = np.zeros(5)
print("zeros: ")
print(x)
print()

x = np.zeros((5,), dtype=np.int)
print("zeros 2: ")
print(x)
print()

x = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print("zeros 3: ")
print(x)
print()

x = np.ones(5)
print("ones: ")
print(x)
print()

x = np.ones([2, 2], dtype=int)
print("ones 2: ")
print(x)
print()

x = [1, 2, 3]
a = np.asarray(x)
print("asarray: ")
print(a)
print()

a = np.asarray(x, dtype=float)
print("asarray 2: ")
print(a)
print()

x = (1, 2, 3)
a = np.asarray(x)
print("asarray 3: ")
print(a)
print()

x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print("asarray 4: ")
print(a)
print()

list = range(5)
it = iter(list)
x = np.fromiter(it, dtype=float)
print("fromiter: ")
print(x)
print()

x = np.arange(5)
print("arange: ")
print(x)
print()

x = np.arange(5, dtype=float)
print("arange 2: ")
print(x)
print()

x = np.arange(10, 20, 2)
print("arange 3: ")
print(x)
print()

x = np.linspace(10, 20, 5)
print("linspace: ")
print(x)
print()

x = np.linspace(10, 20, 5, endpoint=False)
print("linspace 2: ")
print(x)
print()

x = np.linspace(1, 2, 5, retstep=True)
print("linspace 3: ")
print(x)
print()

a = np.logspace(1.0, 2.0, num=10)
print("logspace: ")
print(a)
print()

a = np.logspace(1, 10, num=10, base=2)
print("logspace 2: ")
print(a)
print()
