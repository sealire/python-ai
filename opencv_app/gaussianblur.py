import numpy as np
import cv2

img = np.mat(np.random.randn(300, 300))
img[:, 10] = 255
img[10, :] = 255
cv2.imshow("test", img)
cv2.waitKey(0)

img = cv2.imread("dog.jpg", 0)
cv2.imshow("test", img)
cv2.waitKey(0)

blur = cv2.GaussianBlur(img, (11, 11), 0)
gauss = img - blur

cv2.imshow("test", gauss)
cv2.waitKey(0)
