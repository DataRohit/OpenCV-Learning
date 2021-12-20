import cv2 as cv
import numpy as np
from numpy.core.shape_base import hstack

# NOTE: The below function joins RGB Image to Grayscale Image Horizontally
def hstack_rgb_gray(rgb_img, gray_img):
    rows_rgb, cols_rgb, channels = rgb_img.shape
    rows_gray, cols_gray = gray_img.shape

    rows_comb = max(rows_rgb, rows_gray)
    cols_comb = cols_rgb + cols_gray
    hstack = np.zeros(shape=(rows_comb, cols_comb, channels), dtype=np.uint8)

    hstack[:rows_rgb, :cols_rgb] = rgb_img
    hstack[:rows_gray, cols_rgb:] = gray_img[:, :, None]
    return hstack

# NOTE: The below function joins RGB Image to Grayscale Image Vertically
def vstack_rgb_gray(rgb_img, gray_img):
    rows_rgb, cols_rgb, channels = rgb_img.shape
    rows_gray, cols_gray = gray_img.shape

    rows_comb = rows_rgb + rows_gray
    cols_comb = max(cols_rgb, cols_gray)
    vstack = np.zeros(shape=(rows_comb, cols_comb, channels), dtype=np.uint8)

    vstack[:rows_rgb, :] = rgb_img
    vstack[rows_rgb:, :cols_rgb] = gray_img[:, :, None]
    return vstack

def getContours(img, imgCanny):
    contours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    cv.drawContours(img, contours, -1, (255, 0, 0), 3)

while True:
    img = cv.imread("F:\OpenCV\Learning-Basics\Resources\Images\shapes.jpg")
    blank = np.zeros((img.shape[1], img.shape[0]), dtype=np.uint8)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv.Canny(imgBlur, 50, 50)

    imgContours = img.copy()
    getContours(imgContours, imgCanny)
    cv.imshow("Contorus", imgContours)

    hstack1 = hstack_rgb_gray(img, imgGray)
    hstack2 = cv.hconcat((imgBlur, imgCanny))

    vstack = vstack_rgb_gray(hstack1, hstack2)
    cv.imshow("All Images", vstack)

    if cv.waitKey(0) & 0xFF == ord("q"):
        break

cv.waitKey(0)