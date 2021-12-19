import cv2 as cv
import numpy as np

img = cv.imread("F:\OpenCV\Learning\Resources\Images\cats 2.jpg")
cv.imshow("Cats", img)

width = img.shape[1]
height = img.shape[0]

# NOTE: Mask's are created and added to blank image
# The size of the mask should be same as the image
blank = np.zeros((height, width), np.uint8)
# cv.imshow("Blank Image", blank)

# NOTE: Simple Shape Mask --> Circle
circle_mask = cv.circle(blank.copy(), (width//2, height//2), 100, 255, -1)
# cv.imshow("Circle Mask", circle_mask)

# NOTE: Simple Shape Mask --> Rectangle
rectangle_mask = cv.rectangle(blank.copy(), (width//2-80, height//2-80), (width//2+80, height//2+80), 255, -1)
# cv.imshow("Rectangle Mask", rectangle_mask)

# NOTE: Bitwise Operated Shape Mask
bitwise_mask = cv.bitwise_and(circle_mask, rectangle_mask)
# cv.imshow("Bitwise Mask", bitwise_mask)

# NOTE: Circle Masked Image
circle_masked_img = cv.bitwise_and(img, img, mask=circle_mask)
cv.imshow("Circle Masked Image", circle_masked_img)

# NOTE: Rectangle Masked Image
rectangle_masked_img = cv.bitwise_and(img, img, mask=rectangle_mask)
cv.imshow("Rectangle Masked Image", rectangle_masked_img)

# NOTE: Bitwise Operated Shape Masked Image
bitwise_masked_img = cv.bitwise_and(img, img, mask=bitwise_mask)
cv.imshow("Bitwise Masked Image", bitwise_masked_img)

cv.waitKey(0)