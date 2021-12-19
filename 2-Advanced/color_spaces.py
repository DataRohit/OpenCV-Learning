import cv2 as cv

# BGR is the default color space used by OpenCV
# But most of the apps out there uses RGB format to Read Images
img = cv.imread("F:\OpenCV\Resources\Images\park.jpg")
cv.imshow("BGR Park Image", img)

# Note: BGR --> Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Park Image", gray)

# Note: BGR --> HSV (Hue, Saturation, Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Park Image", hsv)

# Note: BGR --> L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow("LAB Park Image", lab)

# Note: BGR --> RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB Park Image", rgb)

# Note: Grayscale --> BGR
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow("Grayscale --> BGR Park Image", gray_bgr)

# Note: HSV --> BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR Park Image", hsv_bgr)

# Note: L*a*b --> BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("L*a*b --> BGR Park Image", lab_bgr)

# Note: RGB --> BGR
rgb_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow("RGB --> BGR Park Image", rgb_bgr)

cv.waitKey(0)