import cv2 as cv

img = cv.imread("F:\OpenCV\Learning\Resources\Images\cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cats", gray)

# NOTE: Simple Thresholding
thresh_val, thresh_img = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded Image", thresh_img)

# Simple Inverse Thresholding
thresh_val, thresh_inv_img = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Inverse Thresholded Image", thresh_inv_img)

# NOTE: Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive Thresholded Image", adaptive_thresh)

cv.waitKey(0)