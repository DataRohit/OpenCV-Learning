import numpy as np
import cv2 as cv

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

haarcascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

features = np.load("./3-FaceDetection/features.npy", allow_pickle=True)
labels = np.load("./3-FaceDetection/labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("./3-FaceDetection/face_detection_trained.yml")

img = cv.imread("F:\\OpenCV\\Learning\\3-FaceDetection\\Faces\\val\\elton_john\\5.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

faces_rect = haarcascade.detectMultiScale(gray, 1.1, 40)
for (x, y, w, h) in faces_rect:
    face_roi = gray[y:y+h, x:x+h]
    
    label, confidence = face_recognizer.predict(face_roi)
    print(f"Label = {people[label]} with confidence of {confidence}")

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+w), (0,255,0), thickness=2)
    cv.imshow("Detected Faces", img)

cv.waitKey(0)