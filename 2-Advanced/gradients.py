import cv2 as cv
import numpy as np
from numpy.typing import _64Bit

img = cv.imread("F:\OpenCV\Learning\Resources\Images\park.jpg")
cv.imshow("Park", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Park", gray)

# NOTE: Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian Image", lap)

# NOTE: Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow("Sobelx Image", sobelx)
cv.imshow("Sobely Image", sobely)
cv.imshow("Combined Sobel Image", combined_sobel)

canny = cv.Canny(gray, 150, 170)
cv.imshow("Canny Image", canny)

cv.waitKey(0)