import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def empty(a):
    pass

# NOTE: New Window for TrackBars
cv.namedWindow("Track Bars")
cv.resizeWindow("Track Bars", 500, 320)

# Creating TrackBars
cv.createTrackbar("Hue Min", "Track Bars", 7, 179, empty)
cv.createTrackbar("Hue Max", "Track Bars", 30, 179, empty)
cv.createTrackbar("Sat Min", "Track Bars", 51, 255, empty)
cv.createTrackbar("Sat Max", "Track Bars", 255, 255, empty)
cv.createTrackbar("Val Min", "Track Bars", 144, 255, empty)
cv.createTrackbar("Val Max", "Track Bars", 255, 255, empty)

while True:
    # NOTE: Getting the Original Image
    img = cv.imread("F:\OpenCV\Learning-Basics\Resources\Images\lambo.jpg")

    # NOTE: Converting the Image from BGR to HSV
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Get Trackbar Values
    hue_min = cv.getTrackbarPos("Hue Min", "Track Bars")
    hue_max = cv.getTrackbarPos("Hue Max", "Track Bars")
    sat_min = cv.getTrackbarPos("Sat Min", "Track Bars")
    sat_max = cv.getTrackbarPos("Sat Max", "Track Bars")
    val_min = cv.getTrackbarPos("Val Min", "Track Bars")
    val_max = cv.getTrackbarPos("Val Max", "Track Bars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    mask = cv.inRange(img_hsv, lower, upper)

    # Applying the Mask over our Original Image
    masked_img = cv.bitwise_and(img, img, mask=mask)

    hstack_1 = cv.hconcat((img, img_hsv))
    # RGB images cannot be concatenated with Grayscale image
    # The code below solves the problem
    rows_rgb, cols_rgb, channels = img.shape
    rows_gray, cols_gray = mask.shape

    rows_comb = max(rows_rgb, rows_gray)
    cols_comb = cols_rgb + cols_gray
    hstack_2 = np.zeros(shape=(rows_comb, cols_comb, channels), dtype=np.uint8)

    hstack_2[:rows_rgb, cols_rgb:] = masked_img
    hstack_2[:rows_gray, :cols_rgb] = mask[:, :, None]

    # Vertically Concatenating the two horizontal stacks
    one_img = cv.vconcat((hstack_1, hstack_2))
    cv.imshow("Image", one_img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break