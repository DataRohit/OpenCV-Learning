import cv2 as cv
import numpy as np

# Note: Loading the Image
img = cv.imread("F:\OpenCV\Resources\Images\cats.jpg")
cv.imshow("Cats Image", img)

# Note: Creating a Blank Image to display Contours
blank = np.zeros(img.shape, dtype=np.uint8)
cv.imshow("Blank Image", blank)

# Note: Converting a RGB Image to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Cats Image", gray)

# Note: Adding Blur to Image to reduce Edges
blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("Blur Cats Image", blur)

# Note: Creating a Edge Detection Image using Canny Edge Detection
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edge Detection - Cats Image", canny)

# Note: Instead of using Blur and then Canny we can use threshold function
# Pixels intensity below specified value --> Set's Pixel intensity to 0 --> Black
# Pixels intensity above specified value --> Set's Pixel intensity to 1 --> White
# cv.threshold function Binarizes the Image
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold Cats Image", thresh)

# Note: Finding the contours and displaying them on the Blank Image
# Modes: 
# # cv.RETR_TREE --> Only Hierarchical Contours
# # cv.RETR_EXTERNAL --> Only External Contours
# # cv.RETR_LIST --> All the Contours

# Methods:
# # cv.CHAIN_APPROX_NONE --> Give all the Points of contour
# # cv.CHAIN_APPROX_SIMPLE --> Compresses and Gives the end points of the contour
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("Contours Drawn", blank)
print(f"{len(contours)} contour(s) found!")

cv.waitKey(0)