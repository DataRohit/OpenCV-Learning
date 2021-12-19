# Import OpenCV Module
import cv2 as cv

# Reading the Image
img = cv.imread("F:\OpenCV\Resources\Images\cat.jpg")

# # The Image used below has dimensions greater than the size of the screen
# # OpenCV currenty has no solution to deal with over sized images
# img = cv.imread("F:\OpenCV\Resources\Images\cat_large.jpg")

# Showing the Image in a New Window
cv.imshow("Cat", img)

# waitKey(0) -> Wait infinitely for a Key to be pressed
cv.waitKey(0)
