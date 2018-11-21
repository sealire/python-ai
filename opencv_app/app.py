import numpy as np
import cv2

img = cv2.imread("pp.jpg", 0)
shape = np.shape(img)
back = np.mat(np.random.randn(shape[0], shape[1]))
back[:, :] = 200

bimg = back - img

print(np.shape(img))
print(np.shape(bimg))
print(np.shape(back))


cv2.imshow("test", bimg)
cv2.waitKey(0)
