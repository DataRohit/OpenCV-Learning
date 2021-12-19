import cv2 as cv

img = cv.imread("F:\OpenCV\Resources\Images\cat_large.jpg")

# The function below takes the frame and rescale's it to the given scale value
# By defalut the scale value is 0.75
# NOTE: This function works for Images, Videos and Live Video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    # return the resized frame
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

scaled_img = rescaleFrame(img, scale=0.3)

cv.imshow("Resized Image", scaled_img)

cv.waitKey(0)
