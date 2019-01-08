from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# %% Read, Display and write an image
img = cv.imread("dog.jpg", 0)
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow("image", img)
cv.waitKey(0)
cv.destroyAllWindows()
cv.imwrite("dog2.png", img)

# %% Load an image in grayscale and save by pressing 's' or ESC key
cv.namedWindow("image", cv.WINDOW_NORMAL)
cv.imshow("image", img)
k = cv.waitKey(0)

if k == 27:
    cv.destroyAllWindows()
elif k == ord('s'):
    cv.imwrite("dog2.png", img)
    cv.destroyAllWindows()

# %% Using matplotlib
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([])
plt.yticks([])
plt.show()

# %% Resolve OpenCV BGR order because matplotlib follows RGB order
img     = cv.imread("dog.jpg")

b, g, r = cv.split(img)
img2    = cv.merge([r,g,b])
plt.subplot(121)
plt.imshow(img)    # Expects distorted color
plt.subplot(122)
plt.imshow(img2)   # Expects true color
plt.show()

cv.namedWindow("image, cv.WINDOW_NORMAL")
cv.imshow("bgr image", img)
cv.imshow("rgb image", img2)
cv.waitKey(0)
cv.destroyAllWindows()
