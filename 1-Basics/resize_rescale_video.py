import cv2 as cv

capture = cv.VideoCapture("F:\OpenCV\Resources\Videos\dog.mp4")

# Change resolution function
# NOTE: This function works Live Video only
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# The function below scales the frame to given scale value
# NOTE: This function works for Images, Videos and Live Video
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)

    # return the resized frame
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    try:
        # Resizing each frame of the video
        rescaled_frame = rescaleFrame(frame)

        # Show the scaled video frame
        cv.imshow("Resized Video", rescaled_frame)

        if cv.waitKey(20) & 0xFF == ord("d"):
            break
    except:
        break

capture.release()

cv.destroyAllWindows()
