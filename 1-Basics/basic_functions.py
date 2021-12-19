import cv2 as cv

# The Image we are importing is a BGR Image
img = cv.imread("F:\OpenCV\Resources\Images\park.jpg")
cv.imshow("Original Image", img)

# NOTE 1 : Converting to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

# NOTE 2: Add Blur to Image
# Increasing the Kernel Size increases the Blur effect i.e use (7, 7) instead of (3, 3)
# The Dimension of the Kernel should be Odd Number
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur Image", blur)

# NOTE 3: Edge Cascade - Edge Detection of Image
# Bluring the Image and then using Canny Edge Detection will reduce the Number of Edges
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edge Detection", canny)

# NOTE 4: Dilating the Image
# This takes in a Canny Image and applies Dilation to it
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow("Dilated Image", dilated)

# NOTE 5: Eroding the Image
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow("Eroded Image", eroded)

# NOTE 6: Resize the Image
# Different interpolations INTER_AREA, INTER_LINEAR and INTER_CUBIC
# INTER_CUBIC is the slowest by gives the best quality Image
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized Image", resize)

# NOTE 6: Cropping the Image
cropped = img[50:200, 200:400]
cv.imshow("Cropped Image", cropped)

cv.waitKey(0)