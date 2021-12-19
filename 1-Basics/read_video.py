import cv2 as cv

# Loads the Video from specified
# This function also allows for capturing the video input through from Connected Camera
capture = cv.VideoCapture("F:\OpenCV\Resources\Videos\dog.mp4")

# We use a loop to read the Video frame by frame
while True:
    # The function below return the frame from the video
    # and True/False on if the frame was read successfully or not
    isTrue, frame = capture.read()

    # NOTE: The try-except block is used to avoid the (-215:Assertion failed) error
    # Try to show the video
    try:
        # Display the video
        cv.imshow("Video", frame)

        # Wait 20 milliseconds or wait for "d" key to be pressed
        if cv.waitKey(20) & 0xFF == ord("d"):
            # If the key is pressed break out of the loop
            # and stop displaying the video
            break
    # If there is any error loading the video break the loop
    except:
        break

# We release the capture device
capture.release()

# Destroy the Window as the video frames ended
cv.destroyAllWindows()
