import numpy as np

# 广播函数

a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])

print("a:")
print(a)

print("b:")
print(b)

print("a+b:")
print(a + b)
