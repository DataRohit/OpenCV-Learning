import cv2 as cv
import numpy as np

img = cv.imread("F:\OpenCV\Resources\Images\park.jpg")

cv.imshow("Original Park Image", img)

# NOTE 1: Translation - Shifting the Image to given x and y value
def translate(img, x, y):
    transMatx = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatx, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
translated = translate(img, 100, 100)
cv.imshow("Translated Park Image", translated)

# NOTE 2: Rotation - Rotation by Angle
# The function below rotates the Image Anti-Clockwise for +ve Angles and vice-versa
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMatx = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMatx, dimensions)

# Rotating the Normal Image
rotated = rotate(img, -90)
cv.imshow("Rotated Park Image", rotated)

# NOTE 3: Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized Park Image", resized)

# NOTE 4: Flipping
# 0 --> Vertical Flip
# 1 --> Horizontal Flip
# -1 --> Vertical and Horizontal Flip
flipped = cv.flip(img, 1)
cv.imshow("Flipped Park Image", flipped)

# NOTE 5: Cropping
cropped = img[0:300, 0:300]
cv.imshow("Cropped Park Image", cropped)

cv.waitKey(0)