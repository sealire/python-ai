import scipy.integrate
from numpy import exp
from math import sqrt

# 积分

f = lambda x: exp(-x ** 2)
i = scipy.integrate.quad(f, 0, 1)
print("quad:")
print(i)
print()

f = lambda x, y: 16 * x * y
g = lambda x: 0
h = lambda y: sqrt(1 - 4 * y ** 2)
i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
print("dblquad:")
print(i)
print()
