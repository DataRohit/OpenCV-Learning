import cv2 as cv

# NOTE: Smoothing --> Reducing Noise in the Image by applying Blurring

img = cv.imread("F:\OpenCV\Resources\Images\cats.jpg")
cv.imshow("Cats", img)

# Note 1: Average Blur/Averaging
average = cv.blur(img, (3,3))
cv.imshow("Average Blur", average)

# Note 2: Gaussian Blur
gauss = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Gaussian Blur", gauss)

# Note 3: Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Note 4: Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)