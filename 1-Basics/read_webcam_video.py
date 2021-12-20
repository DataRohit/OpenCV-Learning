import cv2 as cv

capture = cv.VideoCapture(0)
capture.set(3, 640) # Width
capture.set(4, 480) # Height
capture.set(10, 150) # Brightness

while True:
    success, img = capture.read()
    cv.imshow("Video", img)
    
    if cv.waitKey(1) & 0xFF == ord("q"):
        break