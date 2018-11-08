import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

x = [[1.1], [1.9], [3.1], [3.9], [5]]
y = [3, 4, 5, 6, 7]
xt = [[6], [7], [8], [9]]

regr = linear_model.LinearRegression()
regr.fit(x, y)
print('Coefficients: \n', regr.coef_, regr.intercept_)

yt = regr.predict(xt)
print(yt)

plt.scatter(xt, yt, color='black')
plt.plot(xt, yt, color='blue', linewidth=1)

# plt.xticks(())
# plt.yticks(())

plt.show()

xx = [[1.1, 0.9], [1.9, 2.1], [3.1, 2.9], [3.9, 4.1], [5, 5]]
yy = [2, 4, 6, 8, 10]
xxyy = np.array([[6, 6], [7, 7], [8, 8], [9, 9]])

regr = linear_model.LinearRegression()
regr.fit(xx, yy)
print('Coefficients: \n', regr.coef_, regr.intercept_)

zz = regr.predict(xxyy)
print(zz)

