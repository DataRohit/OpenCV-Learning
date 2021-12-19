import cv2 as cv

img = cv.imread("F:\\OpenCV\\Learning\\Resources\\Images\\group 1.jpg")
cv.imshow("Person", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Person", gray)

haarcascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_rect = haarcascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+w), (0,255,0), thickness=2)

cv.imshow("Detected Faces", img)

cv.waitKey(0)