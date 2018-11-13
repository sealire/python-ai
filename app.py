import numpy as np

train_X = np.linspace(-1, 1, 100)
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.2

print(train_X.shape)
print(*train_X.shape)
