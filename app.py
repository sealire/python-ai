import numpy as np

x = np.array([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
y = 1 / (1 + np.e ** -x) - 0.5

print(x)
print(y)
