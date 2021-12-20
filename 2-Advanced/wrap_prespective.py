import cv2 as cv
import numpy as np

img = cv.imread("F:\OpenCV\Learning-Basics\Resources\Images\cards.jpg")
cv.imshow("Image", img)

width, height = 250, 350 # Normal Playing Card Dimensions

pts1 = np.float32([[356,125], [520,190], [430,400], [240,324]])
pts2 = np.float32([[0,0], [width, 0], [width,height], [0, height]])

matrix = cv.getPerspectiveTransform(pts1, pts2)
imgOutput = cv.warpPerspective(img, matrix, (width, height))
cv.imshow("Wrap Perspective Image", imgOutput)

cv.waitKey(0)