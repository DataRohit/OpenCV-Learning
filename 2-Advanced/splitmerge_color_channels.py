import cv2 as cv
import numpy as np

img = cv.imread("F:\OpenCV\Resources\Images\park.jpg")
cv.imshow("BGR Park Image", img)

blank = np.zeros(img.shape[:2], dtype=np.uint8)

# Note: Splitting B,G,R components from the Image
# Default Image Color Scale of OpenCV is BGR
# Splitting and getting each component individually
b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

# Viewing the shapes of the Image and the Components
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Note: Merging the Individual Components and viewing them
merged = cv.merge([b,g,r])
cv.imshow("Merged Park Image", merged)

cv.waitKey(0)